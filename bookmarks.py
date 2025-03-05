#!/usr/bin/env python3

# Bookmarks.py
# Copyright (C) 2024 Ray Mentose. 
# Latest source can be found at: https://github.com/ryt/bookmarks.py

v = '0.0.1'
c = 'Copyright (C) 2024 Ray Mentose.'
man = """
Bookmarks.py: A tool that creates a portable, optimized html bookmarks bar from your bookmark exports.
Copyright (C) 2024 Ray Mentose. Latest source: https://github.com/ryt/bookmarks.py

Usage:

  Run on exported bookmarks html file.

  Run               Input                   Output (optional)
  -----------------------------------------------------------
  ./bookmarks.py    (bookmark_file.html)    bookmarks.py.html


  Help manual and version.
  ---------------------------------------
  ./bookmarks.py     (man|help|-h|--help)
  ./bookmarks.py     (-v|--version)

"""

import os
import re
import sys
import json


def parse_bookmarks(html):
  bookmarks = []
  stack = []
  headers = []

  html = re.sub(r'\n', '', html)
  html = re.sub(r'\s+', ' ', html)
  html = re.sub(r'>\s+<', '><', html)
  html = re.sub(r'<([pP])>', r'<\1>\n', html)
  html = re.sub(r'</(h1|H1|h3|H3|a|A)>', r'</\1>\n', html)

  html = html.split('\n')

  for line in html:

    if line.startswith('<DL><p>'):
      fold_name = headers[-1]['title'] if headers else ''
      fold_attr = headers[-1]['attrs'] if headers else {}
      new_folder = {
        'name'     : fold_name,
        'type'     : 'folder',
        'attrs'    : fold_attr,
        'children' : []
      }
      if stack:
        stack[-1]['children'].append(new_folder)
      else:
        bookmarks.append(new_folder)
      stack.append(new_folder)

    elif line.startswith('<DT><H3'):
      title = re.sub(r'<DT><H3.*?>(.*?)</H3>', r'\1', line)
      attrs_raw = re.sub(r'<DT><H3(.*?)>.*?</H3>', r'\1', line).strip().split(' ')
      attrs = {}
      for a in attrs_raw:
        a = a.split('=', 1)
        if len(a) > 1:
          attrs[ a[0].lower() ] = a[1].strip('"')
      headers.append({
        'title' : title,
        'attrs' : attrs
      })

    elif line.startswith('<DT><A'):
      title = re.sub(r'<DT><A.*?>(.*?)</A>', r'\1', line)
      attrs_raw = re.sub(r'<DT><A(.*?)>.*?</A>', r'\1', line).strip().split(' ')
      attrs = {}
      for a in attrs_raw:
        a = a.split('=', 1)
        if len(a) > 1:
          attrs[ a[0].lower() ] = a[1].strip('"')
      new_child = {
        'name'  : title,
        'type'  : 'link',
        'attrs' : attrs,
      }
      if stack:
        stack[-1]['children'].append(new_child)

    elif line.startswith('</DL>'):
      if stack:
        stack.pop()

  return bookmarks



def process_nested_bookmarks(parent):
  """Recursively process nested bookmarks"""

  bookmarks_html = ''

  for elem in parent:
    if elem['type'] == 'link':
      el_name = elem['name']
      el_href = elem['attrs']['href']
      el_icon = elem['attrs']['icon'] if 'icon' in elem['attrs'] else ''
      bookmarks_html += f'<a href="{el_href}"><img src="{el_icon}" />{el_name}</a>\n'
    elif elem['type'] == 'folder':
      el_name = elem['name']
      bookmarks_html += '<div class="parent">'
      bookmarks_html += f'<span class="folder-button"><i class="folder"></i>{el_name}</span>\n'
      if elem['children'] and len(elem['children']) > 0:
        bookmarks_html += '<div class="holder" style="display:none;">' + process_nested_bookmarks(elem['children']) + '</div>'
      bookmarks_html += '</div>'

  return bookmarks_html


def process_bookmarks_file(input, output='bookmarks.py.html', third=''):

  with open(input, 'r', encoding='utf-8') as file:
    html_content = file.read()
  bookmarks = parse_bookmarks(html_content)
  bookmarks_html = ''

  if bookmarks:
    start = bookmarks[0]['children'][0]['children']
    bookmarks_html = process_nested_bookmarks(start)

  final_html = f'''<!DOCTYPE html>
<html>
<head>
  <title>Bookmarks.py</title>
  <style>
     body {{ padding:0;margin:0; }}
    .bookmarks-bar {{ padding:3px;border-bottom:1px solid #ccc; }}
    .bookmarks-bar a,
    .bookmarks-bar span {{ text-decoration:none;display:inline-block;padding:3px 8px 3px 4px;font:12px arial;color:#333;border-radius:5px; }}
    .bookmarks-bar a:hover,
    .bookmarks-bar span:hover {{ background:#eee; }}
    .bookmarks-bar a img {{ margin-right:5px;vertical-align:middle; }}
    .bookmarks-bar span {{ cursor:pointer; }}
    .bookmarks-bar .parent {{ display:inline-block;position:relative; }}
    .bookmarks-bar .holder {{ position:absolute;top:25px;left:0px;z-index:1;background:#fff;width:250px;padding:8px;border:1px solid #ccc;border-radius:5px; }}
    .bookmarks-bar .holder a,
    .bookmarks-bar .holder span {{ display:block;margin:0 0 2px; }}
    .folder {{ width:16px;height:8px;margin-right:5px;position:relative;margin-bottom:-3px;border:1px solid #999;border-radius:0 2px 2px 2px;display:inline-block; }}
    .folder:before {{ content:'';width:80%;height:3px;border-radius:0 2px 0 0;background-color:#ccc;position: absolute;top:-4px;left:-1px; }}
  </style>
</head>
<body>
<div class="bookmarks-bar">
{bookmarks_html}
</div>
<script>

  const folder_btns = document.querySelectorAll(".folder-button");
  let one_opened = false;

  if ( folder_btns.length ) {{
    for ( var i = 0; i < folder_btns.length; i++ ) {{

      folder_btns[i].addEventListener("click", function(){{
        const parent = this.parentElement;
        const holder = parent.querySelector(".holder");
        if ( holder.style.display == "none" ) {{
          holder.style.display = "block";
          one_opened = true;
        }} else {{
          holder.style.display = "none";
          one_opened = false;
        }}
      }});


      folder_btns[i].addEventListener("mouseover", function(){{
        const parent = this.parentElement;
        const holder = parent.querySelector(".holder");
        if ( one_opened == true ) {{
          const all_holders = document.querySelectorAll(".holder");
          for ( var j = 0; j < all_holders.length; j++ ) {{
            if ( all_holders[j] !== holder && all_holders[j].contains(holder) ) {{
              // keep parent visible
            }} else {{
              all_holders[j].style.display = "none";
            }}
          }}
          if ( holder.style.display == "none" ) {{
            holder.style.display = "block";
            one_opened = true;
          }} else {{
            holder.style.display = "none";
            one_opened = false;
          }}
        }}
      }});


    }}
  }}

</script>
</body>
</html>
'''
  
  out_file = re.sub(r'[\w_-]+\.html', output, input)
  
  with open(out_file, 'w', encoding='utf-8') as f:
    f.writelines(final_html)

  # out_json = json.dumps(bookmarks, indent=2)
  # print(out_json)

  print(f'Writing to file "{out_file}" successful.')




def main():

  if len(sys.argv) == 1:
    return print(f'{man.strip()}\n')

  elif sys.argv[1] in ('-v','--version'):
    return print(f'Version: {v}')

  elif sys.argv[1] in ('man','help','-h','--help'):
    return print(f'{man.strip()}\n')

  elif sys.argv[1]:
    process_bookmarks_file(
      sys.argv[1], 
      sys.argv[2] if len(sys.argv) > 2 else False, 
      sys.argv[3] if len(sys.argv) > 3 else False
    )

  else:
    return print(f'{man.strip()}\n')


if __name__ == '__main__':
  main()




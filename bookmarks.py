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

  Run             Input                   Output (optional)
  ---------------------------------------------------------
  ./bookmarks.py  (bookmark_file.html)    bookmarks.py.html


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
      fold_name = headers[-1] if headers else ''
      new_folder = {
        'name'     : fold_name,
        'type'     : 'folder',
        'children' : []
      }
      if stack:
        stack[-1]['children'].append(new_folder)
      else:
        bookmarks.append(new_folder)
      stack.append(new_folder)

    elif line.startswith('<DT><H3'):
      title = re.sub(r'<DT><H3.*?>(.*?)</H3>', r'\1', line)
      headers.append(title)

    elif line.startswith('<DT><A'):
      title = re.sub(r'<DT><A.*?>(.*?)</A>', r'\1', line)
      new_child = {
        'name' : title,
        'type' : 'link',
      }
      if stack:
        stack[-1]['children'].append(new_child)

    elif line.startswith('</DL>'):
      if stack:
        stack.pop()

  return bookmarks



def process_bookmarks_file(input, output='', third=''):

  final_html = f'''<!DOCTYPE html>
  <html>
  <head>
    <title>Bookmarks.py</title>
    <script>
      const Bookmarks = {{ {input} {output} {third}  }};
    </script>
    <style>

    </style>
  </head>
  <body>

  </body>
  </html>'''


  with open(input, 'r', encoding='utf-8') as file:
    html_content = file.read()
  bookmarks = parse_bookmarks(html_content)
  
  out_json = json.dumps(bookmarks, indent=2)
  out_file = re.sub(r'[\w_-]+\.html', 'bookmarks.py.html', input)

  
  with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(bookmarks, f, indent=2, ensure_ascii=False)

  print(out_json)
  print(f'Written to file {out_file}.')



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




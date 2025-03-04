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
import sys



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

  print(final_html)




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




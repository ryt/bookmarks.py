#!/usr/bin/env python3


# Bookmarks.py
# Copyright (C) 2024 Ray Mentose. 
# Latest source can be found at: https://github.com/ryt/bookmarks.py


v = '0.0.1'
c = 'Copyright (C) 2024 Ray Mentose.'
man = """
Bookmarks.py: A tool that creates a portable mobile optimized html based bookmarks bar from your bookmark export.
Copyright (C) 2024 Ray Mentose. Latest source: https://github.com/ryt/bookmarks.py

Usage:

  Run on exported bookmarks html file.
  -------------------------------------------------------
  Run           Input                   Output (optional)
  -------------------------------------------------------
  bookmarks.py  (bookmark_file.html)    bookmarks.py.html

"""


final_html = '''
<!DOCTYPE html>
<html>
<head>
  <title>Bookmarks.py</title>
  <script>
    const Bookmarks = {{}};
  </script>
  <style>

  </style>
</head>
<body>

</body>
</html>'''


print(final_html)


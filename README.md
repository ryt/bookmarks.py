# bookmarks.py
A tool that creates a portable, optimized html bookmarks bar from your bookmark exports.

#### Install

After downloading, you can call the script directly at `./bookmarks.py`.

If you prefer to create an alias, you can add it to your bash aliases:

```bash
alias bookmarks='{install}/bookmarks/bookmarks.py'
```

#### Usage


##### Run on exported bookmarks html file. Output name is optional.

> bookmarks.py {input}  

```console
./bookmarks.py bookmark_file.html
```

> bookmarks.py {input} {output}

```console
./bookmarks.py bookmark_file.html bookmarks.py.html
```

The new `bookmarks.py.html` or custom named file will be created in the same directory as your input file. If output name is specified and the path is different, it will be created in the output path.



##### Show the help manual.

```console
bookmarks.py
bookmarks.py  man|help
```



###### 

<sub><sup>Copyright (C) 2024 Ray Mentose.</sup></sub>


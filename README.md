# bookmarks.py
A tool that creates a portable, optimized html bookmarks bar from your bookmark exports.

#### Install

After downloading, you can call the script directly at `./bookmarks.py`.

You can also create an alias for faster access. If you're using bash, add the following to your aliases:

```console
alias bookmarks.py='{install}/bookmarks.py/bookmarks.py'
```

> Note: Depending on your system, aliases may be found in `~/.bashrc`, `~/.bash_aliases` or `~/.bash_profile`. For other shells, use the corresponding config file: e.g. `~/.zshrc`.

#### Usage


##### Run on exported bookmarks html file. Output name is optional.

> bookmarks.py {input}  

```console
bookmarks.py bookmark_file.html
```

> bookmarks.py {input} {output}

```console
bookmarks.py bookmark_file.html bookmarks.py.html
```

The new `bookmarks.py.html` or custom named file will be created in the same directory as your input file. If output name is specified and the path is different, it will be created in the output path.



##### Show the help manual.

```console
bookmarks.py
bookmarks.py  man|help
```



###### 

<sub><sup>Copyright (C) 2024 Ray Mentose.</sup></sub>


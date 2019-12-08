######
snipco
######

Copies the contents of a saved register, a file, or stdin to the clipboard, or
manipulates the registry.

Usage
=====

::

    snipco [-h] [-g [name_or_path]] [-s [name]] [-x [name]] [-l]
           [-p [name]] [-f [path]] [-v]

Arguments
---------

+-----------------------------------------+-------------------------------------------------+
| -h, --help                              | show this help message and exit                 |
+-----------------------------------------+-------------------------------------------------+
| -g [name_or_path], --get [name_or_path] | Copy the contents of the saved register or file |
|                                         | (--file) is specified.                          |
+-----------------------------------------+-------------------------------------------------+
| -s [name], --set [name]                 | Save the input to a named register.             |
+-----------------------------------------+-------------------------------------------------+
| -x [name], --unset [name]               | Unset the named register.                       |
+-----------------------------------------+-------------------------------------------------+
| -l, --list                              | List the existing registers                     |
+-----------------------------------------+-------------------------------------------------+
|  -p [name], --print [name]              | Print the contents of the named register.       |
+-----------------------------------------+-------------------------------------------------+
| -f [path], --file [path]                | Specify a file to use instead of stdin.         |
+-----------------------------------------+-------------------------------------------------+
| -v, --version                           | show program's version number and exit          |
+-----------------------------------------+-------------------------------------------------+

All arguments are optional, but *at least one* argument must be provided!


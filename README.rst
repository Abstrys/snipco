######
snipco
######

Copies the contents of a saved register, a file, or stdin to the clipboard, or
manipulates the registry.

Installing it
=============

To install from pypi::

    pip install snipco

From source, there are two ways:

* If you have ``make``, run::

     make install

* Otherwise, run::

    ./setup.py install --user


Usage
=====

::

   snipco [-h] [-g [name_or_path]] [-s [name]] [-x [name]] [-l]
          [-p [name]] [-f [path]] [-t [text]] [-v]


::

    snipco [-h] [-g [name_or_path]] [-s [name]] [-x [name]] [-l]
           [-p [name]] [-f [path]] [-v]


For command-line help, just run::

    snipco --help


Arguments
---------

All arguments are optional; if no arguments are provided, then snipco will copy the contents of
stdin to the clipboard. If --file or --text is the sole argument given, then the contents of the
file or quoted text, respectively, will be copied to the clipboard.

+---------------------------+--------------------------------------------------------------------+
| -h, --help                | show help and exit                                                 |
+---------------------------+--------------------------------------------------------------------+
| -g [name_or_path],        | Copy the contents of the saved register. The named                 |
| --get [name_or_path]      | key must exist.                                                    |
+---------------------------+--------------------------------------------------------------------+
| -s [register_name],       | Save the input to a named register.                                |
| --set [register_name]     | Uses stdin as input unless either --file or --text is              |
|                           | specified.                                                         |
+---------------------------+--------------------------------------------------------------------+
| -f [path], --file [path]  | Specify a file to use instead of stdin for --set. If  no other     |
|                           | arguments are supplied, copies the contents of the given file      |
|                           | directly to the clipboard.                                         |
+---------------------------+--------------------------------------------------------------------+
| -t "text to save",        | Specify quote-delimited text on the command-line instead of stdin. |
| --text "text to save"     | If no other arguments are supplied, copies the text directly to    |
|                           | the clipboard.                                                     |
+---------------------------+--------------------------------------------------------------------+
| -l, --list                | List the existing registers                                        |
+---------------------------+--------------------------------------------------------------------+
| -p [name], --print [name] | Print the contents of the named register.  The registry key must   |
|                           | exist.                                                             |
+---------------------------+--------------------------------------------------------------------+
| -x [register_name],       | Unset the named register.                                          |
| --unset [register_name]   |                                                                    |
+---------------------------+--------------------------------------------------------------------+
| -v, --version             | show program's version number and exit                             |
+---------------------------+--------------------------------------------------------------------+

Examples
--------

Save text from a file dirctly to the clipboard::

    snipco --file path/to/file.txt

or::

    cat path/to/file.txt | snipco

Save text to a named register::

    snipco --set myregister --text "Hello, world!"

Copy text from the register to the clipboard::

    snipco --get myregister

Print text in the register to stdout::

    snipco --print myregister

Unset the register::

    snipco --unset myregister

List the registers you've saved::

    snipco --list


#!/usr/bin/env python3
# ~~ coding=utf-8 ~~
from argparse import ArgumentParser
from abstrys.app_settings import AppSettings
import sys, os
from tkinter import Tk

APP_NAME = "snipco"
VERSION = "0.2.1"
DESCRIPTION = """
Copies the contents of a saved register, a file, or stdin to the clipboard, or
manipulates the registry.
"""
EPILOG = """
All arguments are optional; if no arguments are provided, then snipco will copy
the contents of stdin to the clipboard.

If --file or --text is the sole argument given, then the contents of the file or
quoted text, respectively, will be copied to the clipboard.
"""

class SnipCollection:
    """
    Implements a collection of snippets, saved in a .json file.

    Snippets can be copied to the clipboard (default behavior) or printed to
    stdout.
    """

    def __init__(self):
        self.tk = Tk()
        self.tk.withdraw()
        self.tk.clipboard_clear()


    def __del__(self):
        self.tk.update()
        self.tk.destroy()


    def _set_clipboard(self, text):
        """
        Set the current clipboard value, courtesy of tkinter
        """
        self.tk.clipboard_append(text)


    def _parse_args(self):
        """
        Sets up the command-line arguments using argparse.
        """
        parser = ArgumentParser(prog=APP_NAME, description=DESCRIPTION, epilog=EPILOG)
        parser.add_argument(
           "-g", "--get",
           help="Copy the contents of the saved register. The named key must exist.",
           nargs="?",
           metavar="name_or_path",
           default=None)
        parser.add_argument(
           "-s", "--set",
           help="Save the input (stdin, unless --file or --text are specified) to a named register.",
           nargs="?",
           metavar="name",
           default=None)
        parser.add_argument(
           "-x", "--unset",
           help="Unset the named register.",
           nargs="?",
           metavar="name",
           default=None)
        parser.add_argument(
           "-l", "--list",
           help="List the existing registers.",
           action="store_const",
           const=True,
           default=None)
        parser.add_argument(
           "-p", "--print",
           help="Print the contents of the named register. The registry key must exist.",
           nargs="?",
           metavar="name",
           default=None)
        parser.add_argument(
           "-f", "--file",
           help="Specify a file to use instead of stdin for --set. If no other arguments are supplied, copies the contents of the given file directly to the clipboard.",
           nargs="?",
           metavar="path",
           default=None)
        parser.add_argument(
           "-t", "--text",
           help="Specify quote-delimited text on the command-line instead of stdin. If no other arguments are supplied, copies the text directly to the clipboard.",
           nargs="?",
           metavar="text",
           default=None)
        parser.add_argument(
           "-v", "--version",
           action="version",
           version=(APP_NAME + " v" + VERSION))
        return parser.parse_args()


    def run(self):
        """
        This is the main script...
        """
        args = self._parse_args()

        registry = AppSettings(APP_NAME)
        registry.load()

        fd = sys.stdin
        if args.file != None:
            # if --file was specified, use that instead of stdin (for use with either the --get or --set
            # flags).
            if os.path.isfile(args.file):
                fd = open(args.file, 'r')
            else:
                sys.stderr.write("%s Error: file path '%s' does not exist!\n" % (APP_NAME, args.file))
                sys.exit()

        if args.set != None:
            # set a value in the registry
            if args.text != None:
                # if --text was specified, use that text as the value
                registry[args.set] = args.text
            else:
                # otherwise, get the value from the configured file descriptor (either a system file or
                # stdin)
                registry[args.set] = fd.read()
            registry.save()
        elif args.unset != None:
            # unset a value (remove its entry)
            if args.unset in registry:
                del(registry[args.unset])
                registry.save()
                sys.stderr.write("registry key '%s' cleared.\n" % args.unset)
            else:
                sys.stderr.write("The registry key '%s' doesn't exist!\n" % args.unset)
        elif args.get != None:
            # copy a saved value to the clipboard (or None if the value doesn't exist.
            contents = registry[args.get]
            if contents == None:
                sys.stderr.write("The registry key '%s' doesn't exist!\n" % args.unset)
                sys.exit(1)
            self._set_clipboard(contents)
        elif args.print != None:
            # print a saved value to stdout.
            contents = registry.get(args.print)
            if contents == None:
                sys.stderr.write("The registry key '%s' doesn't exist!\n" % args.print)
                sys.exit(1)
            else:
                print(contents)
        elif args.list != None:
            # list the saved keys
            if len(registry.keys()) == 0:
                print("No registry keys stored!")
            else:
                print("Current registry keys:")
                for key in registry.keys():
                    print("* " + key)
        else:
            # if no argument was provided, then copy either the passed in file descriptor or text.
            if args.text != None:
                self._set_clipboard(args.text)
                print("Copied text to clipboard!")
            else:
                self._set_clipboard(fd.read())
                print("Copied contents of %s to the clipboard!" % fd.name)


def main():
    app = SnipCollection()
    app.run()

if __name__ == "__main__":
    main()
    

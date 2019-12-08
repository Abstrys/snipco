#!/usr/bin/env python3
# ~~ coding=utf-8 ~~
from argparse import ArgumentParser
from abstrys.app_settings import AppSettings
import sys, os
from tkinter import Tk

APP_NAME = "snipco"
VERSION = "0.1"
DESCRIPTION = """
Copies the contents of a saved register, a file, or stdin to the clipboard, or manipulates the
registry.
"""
EPILOG = """
All arguments are optional, but *at least one* argument must be provided!
"""

def set_clipboard(value):
    """
    Set the current clipboard value, courtesy of tkinter
    """
    tk = Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(value)
    tk.update()
    tk.destroy()

def main():

    parser = ArgumentParser(prog=APP_NAME, description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument(
       "-g", "--get",
       help="Copy the contents of the saved register or file (if --file) is specified.",
       nargs="?",
       metavar="name_or_path",
       default=None)
    parser.add_argument(
       "-s", "--set",
       help="Save the input to a named register.",
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
       help="List the existing registers",
       action="store_const",
       const=True,
       default=None)
    parser.add_argument(
       "-p", "--print",
       help="Print the contents of the named register.",
       nargs="?",
       metavar="name",
       default=None)
    parser.add_argument(
       "-f", "--file",
       help="Specify a file to use instead of stdin.",
       nargs="?",
       metavar="path",
       default=None)
    parser.add_argument(
       "-v", "--version",
       action="version",
       version=(APP_NAME + " v" + VERSION))
    args = parser.parse_args()

    registry = AppSettings(APP_NAME)
    registry.load()

    fd = sys.stdin
    if args.file != None:
        if os.path.isfile(args.file):
            fd = open(args.file, 'r')
        else:
            sys.stderr.write("%s Error: file path '%s' does not exist!\n" % (APP_NAME, args.file))
            sys.exit()

    if args.set != None:
        registry[args.set] = fd.read()
        registry.save()
        sys.exit()
    elif args.unset != None:
        if args.unset in registry:
            del(registry[args.unset])
            registry.save()
            sys.stderr.write("registry key '%s' cleared.\n" % args.unset)
        else:
            sys.stderr.write("The registry key '%s' doesn't exist!\n" % args.unset)
        sys.exit()
    elif args.get != None:
        contents = registry[args.get]
        set_clipboard(contents)
        sys.exit()
    elif args.print != None:
        contents = registry.get(args.print)
        if contents == None:
            sys.stderr.write("The registry key '%s' doesn't exist!\n" % args.print)
            sys.exit(1)
        else:
            print(contents)
        sys.exit()
    elif args.list != None:
        if len(registry.keys()) == 0:
            print("No registry keys stored!")
        else:
            print("Current registry keys:")
            for key in registry.keys():
                print("* " + key)
        sys.exit()
    else:
        sys.stderr.write("%s Error: no arguments provided!\n\nRun 'snipco --help' for usage information.\n" % APP_NAME)

        

if __name__ == "__main__":
    main()


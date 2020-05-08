#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Hayden"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse


def test_cmd(args):
    print('test_cmd run!', args.testarg_int * -1)


def debug_cmd(args):
    print('Entering debug_cmd')
    print('Exiting debug_cmd')

def add_cmd(args):
    print('Entering add_cmd')
    print('args.item_name = ', args.item_name)
    print('args.start_time = ', args.start_time)
    print('args.end_time = ', args.end_time)
    print('args.item_notes = ', args.item_notes)
    print('Exiting add_cmd')


# TODO: rename rm to 'remove' everywhere and set rm as an alias
def rm_cmd(args):
    print('Entering rm_cmd')
    print('args.item_name = ', args.item_name)
    print('Exiting rm_cmd')


def edit_cmd(args):
    print('Entering edit_cmd')
    print('TODO')
    print('Exiting edit_cmd')


def list_cmd(args):
    print('Entering list_cmd')
    print('args.date_slice = ', args.date_slice)
    print('Exiting list_cmd')


def attr_cmd(args):
    print('Entering attr_cmd')
    print('args.item_name = ', args.item_name)
    print('args.attr_name = ', args.attr_name)
    print('Exiting attr_cmd')



def main(args):
    """ Main entry point of the app """

    # if args.add:
    #     print('add command called')
    # elif args.rm:
    #     print('rm command called')
    # elif args.edit:
    #     print('edit command called')
    # elif args.list:
    #     print('list command called')
    # elif args.repl:
    #     print('repl command called')
    # elif args.debug:
    #     print('debug command called')
    # elif args.test:
    #     print('test command called')
    # else:
    #     print('Enter a command')






if __name__ == "__main__":
    """ This is executed when run from the command line """
    # parser = argparse.ArgumentParser()

    # # Required positional argument
    # parser.add_argument("arg", help="Required positional argument")

    # # Optional argument flag which defaults to False
    # parser.add_argument("-f", "--flag", action="store_true", default=False)

    # # Optional argument which requires a parameter (eg. -d test)
    # parser.add_argument("-n", "--name", action="store", dest="name")

    # # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    # parser.add_argument(
    #     "-v",
    #     "--verbose",
    #     action="count",
    #     default=0,
    #     help="Verbosity (-v, -vv, etc)")

    # # Specify output of "--version"
    # parser.add_argument(
    #     "--version",
    #     action="version",
    #     version="%(prog)s (version {version})".format(version=__version__))

    # args = parser.parse_args()



    # --------------------------------------------------
    # Create parser and subparsers for sub-commands
    # --------------------------------------------------

    parser = argparse.ArgumentParser(description='A simple command-line based calender.')

    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='TODO: subcommands help')
    # TODO: add descriptions to subparsers if possible
    parser_add = subparsers.add_parser('add', aliases=['a'])
    parser_rm = subparsers.add_parser('rm', aliases=['r'])
    parser_edit = subparsers.add_parser('edit', aliases=['e'])
    parser_list = subparsers.add_parser('list', aliases=['l', 'ls'])
    parser_attr = subparsers.add_parser('attr')
    parser_debug = subparsers.add_parser('debug')
    parser_test = subparsers.add_parser('test')


    # --------------------------------------------------
    # add Args and options
    # --------------------------------------------------

    # Create `add` positional arg slots
    parser_add.add_argument('item_name', default='$UNTITLED_ITEM')
    parser_add.add_argument('start_time')
    parser_add.add_argument('end_time')
    parser_add.add_argument('item_notes', default='')

    # Set function for `add` command to point to
    parser_add.set_defaults(func=add_cmd)


    # --------------------------------------------------
    # rm Args and options
    # --------------------------------------------------

    # Create `rm` positional arg slots
    # TODO: implement ability to specify int item ID to delete instead (as a flag) option
    parser_rm.add_argument('item_name')

    # Set function for `add` command to point to
    parser_rm.set_defaults(func=rm_cmd)



    # --------------------------------------------------
    # edit Args and options
    # --------------------------------------------------

    # TODO: implement the edit command like so:
    # scal edit "curr item name" --name "new item name" --notes "newitem notes"



    # --------------------------------------------------
    # list Args and options
    # --------------------------------------------------

    # Create `list` positional arg slots
    parser_list.add_argument('date_slice')

    # Set function for `list` command to point to
    parser_list.set_defaults(func=list_cmd)


    # --------------------------------------------------
    # attr Args and options
    # --------------------------------------------------

    # Create `attr` positional arg slots
    # TODO: implement getting attribute by ID as well
    parser_attr.add_argument('item_name')
    parser_attr.add_argument('attr_name')

    # Set function for `attr` command to point to
    parser_attr.set_defaults(func=attr_cmd)




    # --------------------------------------------------
    # debug Args and options
    # --------------------------------------------------

    # Set function for `debug` command to point to
    parser_add.set_defaults(func=debug_cmd)


    # --------------------------------------------------
    # test Args and options
    # --------------------------------------------------


    parser_test.add_argument('testarg_int', type=int, default=1)
    parser_test.set_defaults(func=test_cmd)

    # --------------------------------------------------
    # Parse args and run program
    # --------------------------------------------------


    args = parser.parse_args()
    args.func(args)

    main(args)

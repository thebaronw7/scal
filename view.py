#!/usr/bin/env python3
"""
Module Docstring TODO
"""

__author__ = "Hayden"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import controller
import scalendar

# TODO: add help descriptions for all commands

def do_add_cmd(args, controller):
    controller.add_cmd(args)

    # Print output to the console
    # TODO

def do_remove_cmd(args, controller):
    controller.remove_cmd(args)

    # Print output to the console
    # TODO

def do_edit_cmd(args, controller):
    controller.edit_cmd(args)

    # Print output to the console
    # TODO

def do_list_cmd(args, controller):
    controller.list_cmd(args)

    # Print output to the console
    # TODO


def do_getattr_cmd(args, controller):
    controller.getattr_cmd(args)

    # Print output to the console
    # TODO


def do_test_cmd(args, controller):
    controller.test_cmd(args)

    # Print output to the console
    # TODO


def do_debug_cmd(args, controller):
    controller.debug_cmd(args)

    # Print output to the console
    # TODO


def main(args):
    """ Main entry point of the app """
    pass


if __name__ == "__main__":

    # --------------------------------------------------
    # Create parser and subparsers for sub-commands
    # --------------------------------------------------

    parser = argparse.ArgumentParser(description='A simple command-line based calender.')

    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='TODO: subcommands help')
    # TODO: add descriptions to subparsers if possible
    parser_add = subparsers.add_parser('add', aliases=['a'])
    parser_remove = subparsers.add_parser('remove', aliases=['r', 'rm'])
    parser_edit = subparsers.add_parser('edit', aliases=['e'])
    parser_list = subparsers.add_parser('list', aliases=['l', 'ls'])
    parser_attr = subparsers.add_parser('attr')
    parser_debug = subparsers.add_parser('debug')
    parser_test = subparsers.add_parser('test')

    # Create a controller and its corresponding calendar
    controller = controller.Controller(scalendar.Scalendar())

    # --------------------------------------------------
    # add Args and options
    # --------------------------------------------------

    # Create `add` positional arg slots
    parser_add.add_argument('item_name', default='$UNTITLED_ITEM')
    parser_add.add_argument('start_time')
    parser_add.add_argument('end_time')
    parser_add.add_argument('item_notes', default='')

    # Set function for `add` command to point to
    parser_add.set_defaults(func=do_add_cmd)


    # --------------------------------------------------
    # remove Args and options
    # --------------------------------------------------

    # Create `remove` positional arg slots
    # TODO: implement ability to specify int item ID to delete instead (as a flag) option
    parser_remove.add_argument('item_name')

    # Set function for `add` command to point to
    parser_remove.set_defaults(func=do_remove_cmd)



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
    parser_list.set_defaults(func=do_list_cmd)


    # --------------------------------------------------
    # attr Args and options
    # --------------------------------------------------

    # Create `attr` positional arg slots
    # TODO: implement getting attribute by ID as well
    parser_attr.add_argument('item_name')
    parser_attr.add_argument('attr_name')

    # Set function for `attr` command to point to
    parser_attr.set_defaults(func=do_getattr_cmd)


    # --------------------------------------------------
    # debug Args and options
    # --------------------------------------------------

    # Set function for `debug` command to point to
    parser_add.set_defaults(func=do_debug_cmd)


    # --------------------------------------------------
    # test Args and options
    # --------------------------------------------------


    parser_test.add_argument('testarg_int', type=int, default=1)
    parser_test.set_defaults(func=do_test_cmd)

    # --------------------------------------------------
    # Parse args and run program
    # --------------------------------------------------


    args = parser.parse_args()
    args.func(args, controller)

    main(args)

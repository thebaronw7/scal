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

    subparsers = parser.add_subparsers(title='subcommands', description='Valid subcommands.', help='TODO: subcommands help')
    # TODO: add descriptions to subparsers if possible
    parser_add = subparsers.add_parser('add',
                                       description='Add a calendar item.', aliases=['a'])
    parser_remove = subparsers.add_parser('remove',
                                          description='Remove a calendar item.', aliases=['r', 'rm'])
    parser_edit = subparsers.add_parser('edit',
                                        description='Edit a calendar item.', aliases=['e'])
    parser_list = subparsers.add_parser('list',
                                        description='List calendar items.', aliases=['l', 'ls'])
    parser_getattr = subparsers.add_parser('getattr',
                                           description='Get the value of a calendar item attribute.')
    parser_debug = subparsers.add_parser('debug',
                                         description='For debug purposes.')
    parser_test = subparsers.add_parser('test',
                                        description='Reserved for experimentation.')

    # Create a controller and its corresponding calendar
    controller = controller.Controller(scalendar.Scalendar('TODO:DEFAULT_CAL_NAME'))

    # --------------------------------------------------
    # add Args and options
    # --------------------------------------------------

    # Create `add` positional arg slots
    parser_add.add_argument('item_name', help='Name of the calendar item to add', default='$UNTITLED_ITEM')
    parser_add.add_argument('start_time', help='Start time of the calendar item to add in [yyyy-mm-dd hh:mm] format.')
    parser_add.add_argument('end_time', help='End time of the calendar item to add in [yyyy-mm-dd hh:mm] format.')
    parser_add.add_argument('item_notes', help='Notes to be associated with the new calendar item.', default='')

    # Set function for `add` command to point to
    parser_add.set_defaults(func=do_add_cmd)

    # --------------------------------------------------
    # remove Args and options
    # --------------------------------------------------

    # Create `remove` positional arg slots
    # TODO: implement ability to specify int item ID to delete instead (as a flag) option. Int should actually be default and the name version a flag.
    parser_remove.add_argument('item_id', help='Unique string id of calendar item to be removed.')

    # Set function for `add` command to point to
    parser_remove.set_defaults(func=do_remove_cmd)


    # --------------------------------------------------
    # edit Args and options
    # --------------------------------------------------

    # scal edit "curr item name" --name "new item name" --notes "newitem notes"

    parser_edit.add_argument('item_id', help='Unique string ID of the item to edit.')
    parser_edit.add_argument('-n', '--name', help='Edit name')
    parser_edit.add_argument('-s', '--starttime', help='Edit start time')
    parser_edit.add_argument('-e', '--endtime', help='Edit end time')
    parser_edit.add_argument('-N', '--notes', help='Edit notes')

    parser_edit.set_defaults(func=do_edit_cmd)

    # --------------------------------------------------
    # list Args and options
    # --------------------------------------------------

    # Create `list` positional arg slots
    parser_list.add_argument('date_slice', help='An interval representing a date. Choices --\n [\',\' (for all calendar items),\n \'yyyy-mm-dd\' (for calendar items that begin or end ON the specified day),\n \'yyyy-mm-dd,\' (for calendar items that begin or end AFTER the specified day), \n \',yyyy-mm-dd\' (for calendar items that begin ore end BEFORE the specified day), \n \'yyyy-mm-dd,yyyy-mm-dd\' (for calendar items that begin or end ON THE CLOSED INTERVAL.)]')  # TODO: make sure date slice is comma separated to allow for time/date slice in the future.

    # Set function for `list` command to point to
    parser_list.set_defaults(func=do_list_cmd)

    # --------------------------------------------------
    # attr Args and options
    # --------------------------------------------------

    # Create `attr` positional arg slots
    # TODO: implement getting attribute by ID as well
    parser_getattr.add_argument('item_id', help='The id of a calendar item.')
    parser_getattr.add_argument('attr_name', help='The name of the attribute to get.')

    # Set function for `attr` command to point to
    parser_getattr.set_defaults(func=do_getattr_cmd)

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

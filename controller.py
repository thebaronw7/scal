"""
Module docstring TODO
"""


class Controller:
    """
    An instance of Controller is in charge of parsing arg data given to
    it by the View into input suitable for Model functions, before updating
    the Model.
    """

    def __init__(self, calendar):
        self.cal = calendar

    def add_cmd(self, args):
        print('Entering do_add_cmd')
        print('args.item_name = ', args.item_name)
        print('args.start_time = ', args.start_time)
        print('args.end_time = ', args.end_time)
        print('args.item_notes = ', args.item_notes)
        print('Exiting do_add_cmd')

    def remove_cmd(self, args):
        print('Entering do_remove_cmd')
        print('args.item_id = ', args.item_id)
        print('Exiting do_remove_cmd')

    def edit_cmd(self, args):
        print('args', args)
        print('Entering do_edit_cmd')
        print('TODO')
        print('Exiting do_edit_cmd')

    def list_cmd(self, args):
        print('Entering do_list_cmd')
        print('args.date_slice = ', args.date_slice)
        print('Exiting do_list_cmd')

    def getattr_cmd(self, args):
        print('Entering do_getattr_cmd')
        print('args.item_id = ', args.item_id)
        print('args.attr_name = ', args.attr_name)
        print('Exiting do_getattr_cmd')

    def test_cmd(self, args):
        print('do_test_cmd run!', args.testarg_int * -1)

    def debug_cmd(self, args):
        print('Entering do_debug_cmd')
        print('Exiting do_debug_cmd')

    def debugprint(self):
        print('This is the controller', self)

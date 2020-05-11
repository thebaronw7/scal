"""
Module docstring TODO
"""

import scalendar


class Controller:
    """
    An instance of Controller is in charge of parsing arg data given to
    it by the View into input suitable for Model functions, before updating
    the Model.
    """

    def __init__(self, scalendar):
        self.scal = scalendar

    def add_cmd(self, args):
        print('Entering do_add_cmd')
        print('args = ', args)

        # TODO: load vars with correct values from args
        name = None
        start_datetime = None
        end_datetime = None
        notes = None

        return self.scal.add_item(name, start_datetime,
                                  end_datetime, notes)

    def remove_cmd(self, args):
        print('Entering do_remove_cmd')
        print('args = ', args)

        # TODO: load vars with correct values from args
        calitem_id = None
        return self.scal.remove_item(calitem_id)

    def edit_cmd(self, args):
        print('Entering do_edit_cmd')
        print('args = ', args)

        # TODO: load vars with correct values from args
        calitem_id = None
        name = None
        start_time = None
        end_time = None
        notes = None
        return self.scal.edit_item(calitem_id, name,
                                   start_time, end_time, notes)

    def list_cmd(self, args):
        print('Entering do_list_cmd')
        print('args = ', args)

        # TODO: load vars with correct values from args
        start_time = None
        end_time = None
        calitem_id = None

        return self.scal.list_items(start_time,
                                    end_time, calitem_id)

    def getattr_cmd(self, args):
        print('Entering do_getattr_cmd')
        print('args = ', args)
        # TODO: implement later (low priority)
        print('Exiting do_getattr_cmd')

    def test_cmd(self, args):
        print('args = ', args)
        pass

    def debug_cmd(self, args):
        print('Entering do_debug_cmd')
        print('args = ', args)
        print('Exiting do_debug_cmd')






"""
TODO: Module Doctring
"""

import constants

import calendar
import datetime


class Scalendar:
    """
    A representation of a simple calendar.
    Monday is the first day of the week (European standard).
    """

    class CalItem:
        """
        A representation of a calendar item.
        """

        def __init__(self, item_id, name,
                     start_datetime_, end_datetime_, notes_):
            self.id = item_id
            self.start_datetime = start_datetime_
            self.end_datetime = end_datetime_
            self.notes = notes_

    def __init__(self, cal_name):

        self.name = cal_name

        self._pycal = calendar.Calendar()
        #self._pytxtcal = calendar.TextCalendar()  # TODO: move this to view if possible (it is a view concern)
        self._startdatetime_to_calitem = {}
        self._enddatetime_to_calitem = {}
        self._id_to_calitem = {}

        # Item IDs
        self._item_id_set = set()
        self._id_1_ctr = 0  # 1st (least-sig) char bit [0,25]
        self._id_2_ctr = 0  # 2nd char 26it [0,25]
        self._id_3_ctr = 0  # 3rd char 26it [0,25]
        self._id_4_ctr = 0  # 4th char 26it [0,25]
        self._num_to_char26 = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                              4: 'e', 5: 'f', 6: 'g', 7: 'h',
                              8: 'i', 9: 'j', 10: 'k', 11: 'l',
                              12: 'm', 13: 'n', 14: 'o',
                              15: 'p', 16: 'q', 17: 'r',
                              18: 's', 19: 't', 20: 'u',
                              21: 'v', 22: 'w', 23: 'x',
                              24: 'y', 25: 'z'}

    def _gen_calitem_id(self):
        """
        Generates a 4 character string ID that is unique among
        the set of id's found in this scal. The characters
        of the ID can be any lowercase letter making
        for 26^4 = 456,976 possible calendar ID's. Assigns
        the id to this CalItem's id field
        """

    def add_item(self, name, start_time, end_time, notes):

        # Add to text file
        # TODO

        # Add to dictionaries  (if in REPL)
        # TODO

        # Return a calitem object representing the new item added
        pass

    def remove_item(self, calitem_id):

        # Remove from text file
        # TODO

        # Remove from dictionaries (if in REPL)
        # TODO

        # return a calitem object representing the removed item
        pass

    def edit_item(self, calitem_id, name=None,
                  start_time=None, end_time=None, notes=None):
        # TODO: implement function

        # Save existing calendar item state temporarily

        # Delete existing item from text file -- keeping track of where it was

        # Delete existing item from dictionaries

        # Create new calendar item using new info when specified and old info when not

        # Add new calendar item to text file

        # Add new calendar item to dictionaries (if in REPL)

        # Return the calitem object representing the updated edited item

        pass

    def list(self, start_time=constants.MIN_DATE,
             end_time=constants.MAX_DATE, calitem_id=None):

        # If calitem_id isn't None, return the calendar item with the specified ID

        # Else, return a list of calendar items on the given interval sorted by date/time past->future

        pass

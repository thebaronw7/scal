"""
TODO: Module docstring
"""


class CalItem:

    def __init__(self):
        self.id = None

    def gen_calitem_id(self, scal):
        """
        Generates a 4 character string ID that is unique among
        the set of id's found in the given scal. The characters
        of the ID can be any lowercase letter making
        for 26^4 = 456,976 possible calendar ID's. Assigns
        the id to this CalItem's id field
        """
        self.id = None  # TODO: change
        pass



"""Lists all supported OS categories for this cloud."""
from baseCmd import *
from baseResponse import *
class listOsCategoriesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list Os category by id"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """list os category by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listOsCategoriesResponse (baseResponse):
    def __init__(self):
        """the ID of the OS category"""
        self.id = None
        """the name of the OS category"""
        self.name = None


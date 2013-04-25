
"""Lists all supported OS types for this cloud."""
from baseCmd import *
from baseResponse import *
class listOsTypesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list os by description"""
        self.description = None
        """list by Os type Id"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """list by Os Category id"""
        self.oscategoryid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listOsTypesResponse (baseResponse):
    def __init__(self):
        """the ID of the OS type"""
        self.id = None
        """the name/description of the OS type"""
        self.description = None
        """the ID of the OS category"""
        self.oscategoryid = None


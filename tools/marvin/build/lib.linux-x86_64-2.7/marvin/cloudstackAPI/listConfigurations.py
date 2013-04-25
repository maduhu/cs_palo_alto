
"""Lists all configurations."""
from baseCmd import *
from baseResponse import *
class listConfigurationsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """lists configurations by category"""
        self.category = None
        """List by keyword"""
        self.keyword = None
        """lists configuration by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listConfigurationsResponse (baseResponse):
    def __init__(self):
        """the category of the configuration"""
        self.category = None
        """the description of the configuration"""
        self.description = None
        """the name of the configuration"""
        self.name = None
        """the value of the configuration"""
        self.value = None


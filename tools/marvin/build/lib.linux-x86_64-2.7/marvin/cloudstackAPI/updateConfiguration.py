
"""Updates a configuration."""
from baseCmd import *
from baseResponse import *
class updateConfigurationCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the name of the configuration"""
        """Required"""
        self.name = None
        """the value of the configuration"""
        self.value = None
        self.required = ["name",]

class updateConfigurationResponse (baseResponse):
    def __init__(self):
        """the category of the configuration"""
        self.category = None
        """the description of the configuration"""
        self.description = None
        """the name of the configuration"""
        self.name = None
        """the value of the configuration"""
        self.value = None


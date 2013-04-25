
"""lists all available apis on the server, provided by the Api Discovery plugin"""
from baseCmd import *
from baseResponse import *
class listApisCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """API name"""
        self.name = None
        self.required = []

class listApisResponse (baseResponse):
    def __init__(self):
        """description of the api"""
        self.description = None
        """true if api is asynchronous"""
        self.isasync = None
        """the name of the api command"""
        self.name = None
        """comma separated related apis"""
        self.related = None
        """version of CloudStack the api was introduced in"""
        self.since = None
        """the list params the api accepts"""
        self.params = []
        """api response fields"""
        self.response = []

class params:
    def __init__(self):
        """"description of the api parameter"""
        self.description = None
        """"length of the parameter"""
        self.length = None
        """"the name of the api parameter"""
        self.name = None
        """"comma separated related apis to get the parameter"""
        self.related = None
        """"true if this parameter is required for the api request"""
        self.required = None
        """"version of CloudStack the api was introduced in"""
        self.since = None
        """"parameter type"""
        self.type = None

class response:
    def __init__(self):
        """"description of the api response field"""
        self.description = None
        """"the name of the api response field"""
        self.name = None
        """"response field type"""
        self.type = None


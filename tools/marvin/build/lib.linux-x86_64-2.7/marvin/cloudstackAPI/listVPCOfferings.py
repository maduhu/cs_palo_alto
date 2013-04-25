
"""Lists VPC offerings"""
from baseCmd import *
from baseResponse import *
class listVPCOfferingsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list VPC offerings by display text"""
        self.displaytext = None
        """list VPC offerings by id"""
        self.id = None
        """true if need to list only default VPC offerings. Default value is false"""
        self.isdefault = None
        """List by keyword"""
        self.keyword = None
        """list VPC offerings by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list VPC offerings by state"""
        self.state = None
        """list VPC offerings supporting certain services"""
        self.supportedservices = []
        self.required = []

class listVPCOfferingsResponse (baseResponse):
    def __init__(self):
        """the id of the vpc offering"""
        self.id = None
        """the date this vpc offering was created"""
        self.created = None
        """an alternate display text of the vpc offering."""
        self.displaytext = None
        """true if vpc offering is default, false otherwise"""
        self.isdefault = None
        """the name of the vpc offering"""
        self.name = None
        """state of the vpc offering. Can be Disabled/Enabled"""
        self.state = None
        """the list of supported services"""
        self.service = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class service:
    def __init__(self):
        """"the service name"""
        self.name = None
        """"the service provider name"""
        self.provider = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None



"""Updates VPC offering"""
from baseCmd import *
from baseResponse import *
class updateVPCOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the display text of the VPC offering"""
        self.displaytext = None
        """the id of the VPC offering"""
        self.id = None
        """the name of the VPC offering"""
        self.name = None
        """update state for the VPC offering; supported states - Enabled/Disabled"""
        self.state = None
        self.required = []

class updateVPCOfferingResponse (baseResponse):
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


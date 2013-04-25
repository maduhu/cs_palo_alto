
"""Lists capabilities"""
from baseCmd import *
from baseResponse import *
class listCapabilitiesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class listCapabilitiesResponse (baseResponse):
    def __init__(self):
        """true if regular user is allowed to create projects"""
        self.allowusercreateprojects = None
        """version of the cloud stack"""
        self.cloudstackversion = None
        """maximum size that can be specified when create disk from disk offering with custom size"""
        self.customdiskofferingmaxsize = None
        """If invitation confirmation is required when add account to project"""
        self.projectinviterequired = None
        """true if security groups support is enabled, false otherwise"""
        self.securitygroupsenabled = None
        """true if region supports elastic load balancer on basic zones"""
        self.supportELB = None
        """true if user and domain admins can set templates to be shared, false otherwise"""
        self.userpublictemplateenabled = None


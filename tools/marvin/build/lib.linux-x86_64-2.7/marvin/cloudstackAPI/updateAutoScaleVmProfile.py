
"""Updates an existing autoscale vm profile."""
from baseCmd import *
from baseResponse import *
class updateAutoScaleVmProfileCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale vm profile"""
        """Required"""
        self.id = None
        """the ID of the user used to launch and destroy the VMs"""
        self.autoscaleuserid = None
        """counterparam list. Example: counterparam[0].name=snmpcommunity&counterparam[0].value=public&counterparam[1].name=snmpport&counterparam[1].value=161"""
        self.counterparam = []
        """the time allowed for existing connections to get closed before a vm is destroyed"""
        self.destroyvmgraceperiod = None
        """the template of the auto deployed virtual machine"""
        self.templateid = None
        self.required = ["id",]

class updateAutoScaleVmProfileResponse (baseResponse):
    def __init__(self):
        """the autoscale vm profile ID"""
        self.id = None
        """the account owning the instance group"""
        self.account = None
        """the ID of the user used to launch and destroy the VMs"""
        self.autoscaleuserid = None
        """the time allowed for existing connections to get closed before a vm is destroyed"""
        self.destroyvmgraceperiod = None
        """the domain name of the vm profile"""
        self.domain = None
        """the domain ID of the vm profile"""
        self.domainid = None
        """parameters other than zoneId/serviceOfferringId/templateId to be used while deploying a virtual machine"""
        self.otherdeployparams = None
        """the project name of the vm profile"""
        self.project = None
        """the project id vm profile"""
        self.projectid = None
        """the service offering to be used while deploying a virtual machine"""
        self.serviceofferingid = None
        """the template to be used while deploying a virtual machine"""
        self.templateid = None
        """the availability zone to be used while deploying a virtual machine"""
        self.zoneid = None


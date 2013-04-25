
"""Creates a profile that contains information about the virtual machine which will be provisioned automatically by autoscale feature."""
from baseCmd import *
from baseResponse import *
class createAutoScaleVmProfileCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the service offering of the auto deployed virtual machine"""
        """Required"""
        self.serviceofferingid = None
        """the template of the auto deployed virtual machine"""
        """Required"""
        self.templateid = None
        """availability zone for the auto deployed virtual machine"""
        """Required"""
        self.zoneid = None
        """the ID of the user used to launch and destroy the VMs"""
        self.autoscaleuserid = None
        """counterparam list. Example: counterparam[0].name=snmpcommunity&counterparam[0].value=public&counterparam[1].name=snmpport&counterparam[1].value=161"""
        self.counterparam = []
        """the time allowed for existing connections to get closed before a vm is destroyed"""
        self.destroyvmgraceperiod = None
        """parameters other than zoneId/serviceOfferringId/templateId of the auto deployed virtual machine"""
        self.otherdeployparams = None
        self.required = ["serviceofferingid","templateid","zoneid",]

class createAutoScaleVmProfileResponse (baseResponse):
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


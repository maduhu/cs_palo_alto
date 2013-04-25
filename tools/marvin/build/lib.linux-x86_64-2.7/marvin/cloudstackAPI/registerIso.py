
"""Registers an existing ISO into the CloudStack Cloud."""
from baseCmd import *
from baseResponse import *
class registerIsoCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the display text of the ISO. This is usually used for display purposes."""
        """Required"""
        self.displaytext = None
        """the name of the ISO"""
        """Required"""
        self.name = None
        """the URL to where the ISO is currently being hosted"""
        """Required"""
        self.url = None
        """the ID of the zone you wish to register the ISO to."""
        """Required"""
        self.zoneid = None
        """an optional account name. Must be used with domainId."""
        self.account = None
        """true if this ISO is bootable. If not passed explicitly its assumed to be true"""
        self.bootable = None
        """the MD5 checksum value of this ISO"""
        self.checksum = None
        """an optional domainId. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        """true if the iso or its derivatives are extractable; default is false"""
        self.isextractable = None
        """true if you want this ISO to be featured"""
        self.isfeatured = None
        """true if you want to register the ISO to be publicly available to all users, false otherwise."""
        self.ispublic = None
        """the ID of the OS Type that best represents the OS of this ISO. If the iso is bootable this parameter needs to be passed"""
        self.ostypeid = None
        """Register iso for the project"""
        self.projectid = None
        self.required = ["displaytext","name","url","zoneid",]

class registerIsoResponse (baseResponse):
    def __init__(self):
        """the template ID"""
        self.id = None
        """the account name to which the template belongs"""
        self.account = None
        """the account id to which the template belongs"""
        self.accountid = None
        """true if the ISO is bootable, false otherwise"""
        self.bootable = None
        """checksum of the template"""
        self.checksum = None
        """the date this template was created"""
        self.created = None
        """true if the template is managed across all Zones, false otherwise"""
        self.crossZones = None
        """additional key/value details tied with template"""
        self.details = None
        """the template display text"""
        self.displaytext = None
        """the name of the domain to which the template belongs"""
        self.domain = None
        """the ID of the domain to which the template belongs"""
        self.domainid = None
        """the format of the template."""
        self.format = None
        """the ID of the secondary storage host for the template"""
        self.hostid = None
        """the name of the secondary storage host for the template"""
        self.hostname = None
        """the hypervisor on which the template runs"""
        self.hypervisor = None
        """true if the template is extractable, false otherwise"""
        self.isextractable = None
        """true if this template is a featured template, false otherwise"""
        self.isfeatured = None
        """true if this template is a public template, false otherwise"""
        self.ispublic = None
        """true if the template is ready to be deployed from, false otherwise."""
        self.isready = None
        """the template name"""
        self.name = None
        """the ID of the OS type for this template."""
        self.ostypeid = None
        """the name of the OS type for this template."""
        self.ostypename = None
        """true if the reset password feature is enabled, false otherwise"""
        self.passwordenabled = None
        """the project name of the template"""
        self.project = None
        """the project id of the template"""
        self.projectid = None
        """the date this template was removed"""
        self.removed = None
        """the size of the template"""
        self.size = None
        """the template ID of the parent template if present"""
        self.sourcetemplateid = None
        """true if template is sshkey enabled, false otherwise"""
        self.sshkeyenabled = None
        """the status of the template"""
        self.status = None
        """the tag of this template"""
        self.templatetag = None
        """the type of the template"""
        self.templatetype = None
        """the ID of the zone for this template"""
        self.zoneid = None
        """the name of the zone for this template"""
        self.zonename = None
        """the list of resource tags associated with tempate"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None



"""List template visibility and all accounts that have permissions to view this template."""
from baseCmd import *
from baseResponse import *
class listTemplatePermissionsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the template ID"""
        """Required"""
        self.id = None
        self.required = ["id",]

class listTemplatePermissionsResponse (baseResponse):
    def __init__(self):
        """the template ID"""
        self.id = None
        """the list of accounts the template is available for"""
        self.account = None
        """the ID of the domain to which the template belongs"""
        self.domainid = None
        """true if this template is a public template, false otherwise"""
        self.ispublic = None
        """the list of projects the template is available for"""
        self.projectids = None


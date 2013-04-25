
"""Lists projects and provides detailed information for listed projects"""
from baseCmd import *
from baseResponse import *
class listProjectsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list projects by display text"""
        self.displaytext = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """list projects by project ID"""
        self.id = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """list projects by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list projects by state"""
        self.state = None
        """List projects by tags (key/value pairs)"""
        self.tags = []
        self.required = []

class listProjectsResponse (baseResponse):
    def __init__(self):
        """the id of the project"""
        self.id = None
        """the account name of the project's owner"""
        self.account = None
        """the displaytext of the project"""
        self.displaytext = None
        """the domain name where the project belongs to"""
        self.domain = None
        """the domain id the project belongs to"""
        self.domainid = None
        """the name of the project"""
        self.name = None
        """the state of the project"""
        self.state = None
        """the list of resource tags associated with vm"""
        self.tags = []

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


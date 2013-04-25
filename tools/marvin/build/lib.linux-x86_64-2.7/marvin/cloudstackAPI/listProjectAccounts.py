
"""Lists project's accounts"""
from baseCmd import *
from baseResponse import *
class listProjectAccountsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """id of the project"""
        """Required"""
        self.projectid = None
        """list accounts of the project by account name"""
        self.account = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list accounts of the project by role"""
        self.role = None
        self.required = ["projectid",]

class listProjectAccountsResponse (baseResponse):
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


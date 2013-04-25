
"""Suspends a project"""
from baseCmd import *
from baseResponse import *
class suspendProjectCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of the project to be suspended"""
        """Required"""
        self.id = None
        self.required = ["id",]

class suspendProjectResponse (baseResponse):
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


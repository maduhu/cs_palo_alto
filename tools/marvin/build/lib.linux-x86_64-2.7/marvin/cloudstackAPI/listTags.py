
"""List resource tag(s)"""
from baseCmd import *
from baseResponse import *
class listTagsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list by customer name"""
        self.customer = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """list by key"""
        self.key = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list objects by project"""
        self.projectid = None
        """list by resource id"""
        self.resourceid = None
        """list by resource type"""
        self.resourcetype = None
        """list by value"""
        self.value = None
        self.required = []

class listTagsResponse (baseResponse):
    def __init__(self):
        """the account associated with the tag"""
        self.account = None
        """customer associated with the tag"""
        self.customer = None
        """the domain associated with the tag"""
        self.domain = None
        """the ID of the domain associated with the tag"""
        self.domainid = None
        """tag key name"""
        self.key = None
        """the project name where tag belongs to"""
        self.project = None
        """the project id the tag belongs to"""
        self.projectid = None
        """id of the resource"""
        self.resourceid = None
        """resource type"""
        self.resourcetype = None
        """tag value"""
        self.value = None


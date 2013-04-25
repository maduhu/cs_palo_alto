
"""Lists resource limits."""
from baseCmd import *
from baseResponse import *
class listResourceLimitsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """Lists resource limits by ID."""
        self.id = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
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
        """Type of resource to update. Values are 0, 1, 2, 3, and 4. 0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create."""
        self.resourcetype = None
        self.required = []

class listResourceLimitsResponse (baseResponse):
    def __init__(self):
        """the account of the resource limit"""
        self.account = None
        """the domain name of the resource limit"""
        self.domain = None
        """the domain ID of the resource limit"""
        self.domainid = None
        """the maximum number of the resource. A -1 means the resource currently has no limit."""
        self.max = None
        """the project name of the resource limit"""
        self.project = None
        """the project id of the resource limit"""
        self.projectid = None
        """resource type. Values include 0, 1, 2, 3, 4. See the resourceType parameter for more information on these values."""
        self.resourcetype = None


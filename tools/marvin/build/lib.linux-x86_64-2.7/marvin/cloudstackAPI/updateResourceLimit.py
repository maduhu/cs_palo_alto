
"""Updates resource limits for an account or domain."""
from baseCmd import *
from baseResponse import *
class updateResourceLimitCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Type of resource to update. Values are 0, 1, 2, 3, and 4. 0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create."""
        """Required"""
        self.resourcetype = None
        """Update resource for a specified account. Must be used with the domainId parameter."""
        self.account = None
        """Update resource limits for all accounts in specified domain. If used with the account parameter, updates resource limits for a specified account in specified domain."""
        self.domainid = None
        """Maximum resource limit."""
        self.max = None
        """Update resource limits for project"""
        self.projectid = None
        self.required = ["resourcetype",]

class updateResourceLimitResponse (baseResponse):
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



"""Recalculate and update resource count for an account or domain."""
from baseCmd import *
from baseResponse import *
class updateResourceCountCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """If account parameter specified then updates resource counts for a specified account in this domain else update resource counts for all accounts & child domains in specified domain."""
        """Required"""
        self.domainid = None
        """Update resource count for a specified account. Must be used with the domainId parameter."""
        self.account = None
        """Update resource limits for project"""
        self.projectid = None
        """Type of resource to update. If specifies valid values are 0, 1, 2, 3, and 4. If not specified will update all resource counts0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create."""
        self.resourcetype = None
        self.required = ["domainid",]

class updateResourceCountResponse (baseResponse):
    def __init__(self):
        """the account for which resource count's are updated"""
        self.account = None
        """the domain name for which resource count's are updated"""
        self.domain = None
        """the domain ID for which resource count's are updated"""
        self.domainid = None
        """the project name for which resource count's are updated"""
        self.project = None
        """the project id for which resource count's are updated"""
        self.projectid = None
        """resource count"""
        self.resourcecount = None
        """resource type. Values include 0, 1, 2, 3, 4. See the resourceType parameter for more information on these values."""
        self.resourcetype = None


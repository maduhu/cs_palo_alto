
"""Updates a vm group"""
from baseCmd import *
from baseResponse import *
class updateInstanceGroupCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Instance group ID"""
        """Required"""
        self.id = None
        """new instance group name"""
        self.name = None
        self.required = ["id",]

class updateInstanceGroupResponse (baseResponse):
    def __init__(self):
        """the id of the instance group"""
        self.id = None
        """the account owning the instance group"""
        self.account = None
        """time and date the instance group was created"""
        self.created = None
        """the domain name of the instance group"""
        self.domain = None
        """the domain ID of the instance group"""
        self.domainid = None
        """the name of the instance group"""
        self.name = None
        """the project name of the group"""
        self.project = None
        """the project id of the group"""
        self.projectid = None


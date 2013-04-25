
"""Lists LBStickiness policies."""
from baseCmd import *
from baseResponse import *
class listLBStickinessPoliciesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the load balancer rule"""
        """Required"""
        self.lbruleid = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = ["lbruleid",]

class listLBStickinessPoliciesResponse (baseResponse):
    def __init__(self):
        """the account of the Stickiness policy"""
        self.account = None
        """the description of the Stickiness policy"""
        self.description = None
        """the domain of the Stickiness policy"""
        self.domain = None
        """the domain ID of the Stickiness policy"""
        self.domainid = None
        """the LB rule ID"""
        self.lbruleid = None
        """the name of the Stickiness policy"""
        self.name = None
        """the state of the policy"""
        self.state = None
        """the id of the zone the Stickiness policy belongs to"""
        self.zoneid = None
        """the list of stickinesspolicies"""
        self.stickinesspolicy = []

class stickinesspolicy:
    def __init__(self):
        """"the LB Stickiness policy ID"""
        self.id = None
        """"the description of the Stickiness policy"""
        self.description = None
        """"the method name of the Stickiness policy"""
        self.methodname = None
        """"the name of the Stickiness policy"""
        self.name = None
        """"the params of the policy"""
        self.params = None
        """"the state of the policy"""
        self.state = None


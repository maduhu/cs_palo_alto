
"""Creates a Load Balancer stickiness policy"""
from baseCmd import *
from baseResponse import *
class createLBStickinessPolicyCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the load balancer rule"""
        """Required"""
        self.lbruleid = None
        """name of the LB Stickiness policy method, possible values can be obtained from ListNetworks API"""
        """Required"""
        self.methodname = None
        """name of the LB Stickiness policy"""
        """Required"""
        self.name = None
        """the description of the LB Stickiness policy"""
        self.description = None
        """param list. Example: param[0].name=cookiename&param[0].value=LBCookie"""
        self.param = []
        self.required = ["lbruleid","methodname","name",]

class createLBStickinessPolicyResponse (baseResponse):
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


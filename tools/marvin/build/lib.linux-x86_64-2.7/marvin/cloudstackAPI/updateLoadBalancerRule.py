
"""Updates load balancer"""
from baseCmd import *
from baseResponse import *
class updateLoadBalancerRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the id of the load balancer rule to update"""
        """Required"""
        self.id = None
        """load balancer algorithm (source, roundrobin, leastconn)"""
        self.algorithm = None
        """the description of the load balancer rule"""
        self.description = None
        """the name of the load balancer rule"""
        self.name = None
        self.required = ["id",]

class updateLoadBalancerRuleResponse (baseResponse):
    def __init__(self):
        """the load balancer rule ID"""
        self.id = None
        """the account of the load balancer rule"""
        self.account = None
        """the load balancer algorithm (source, roundrobin, leastconn)"""
        self.algorithm = None
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        """the description of the load balancer"""
        self.description = None
        """the domain of the load balancer rule"""
        self.domain = None
        """the domain ID of the load balancer rule"""
        self.domainid = None
        """the name of the load balancer"""
        self.name = None
        """the private port"""
        self.privateport = None
        """the project name of the load balancer"""
        self.project = None
        """the project id of the load balancer"""
        self.projectid = None
        """the public ip address"""
        self.publicip = None
        """the public ip address id"""
        self.publicipid = None
        """the public port"""
        self.publicport = None
        """the state of the rule"""
        self.state = None
        """the id of the zone the rule belongs to"""
        self.zoneid = None
        """the list of resource tags associated with load balancer"""
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


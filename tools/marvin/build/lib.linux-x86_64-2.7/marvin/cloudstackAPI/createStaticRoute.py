
"""Creates a static route"""
from baseCmd import *
from baseResponse import *
class createStaticRouteCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """static route cidr"""
        """Required"""
        self.cidr = None
        """the gateway id we are creating static route for"""
        """Required"""
        self.gatewayid = None
        self.required = ["cidr","gatewayid",]

class createStaticRouteResponse (baseResponse):
    def __init__(self):
        """the ID of static route"""
        self.id = None
        """the account associated with the static route"""
        self.account = None
        """static route CIDR"""
        self.cidr = None
        """the domain associated with the static route"""
        self.domain = None
        """the ID of the domain associated with the static route"""
        self.domainid = None
        """VPC gateway the route is created for"""
        self.gatewayid = None
        """the project name of the static route"""
        self.project = None
        """the project id of the static route"""
        self.projectid = None
        """the state of the static route"""
        self.state = None
        """VPC the static route belongs to"""
        self.vpcid = None
        """the list of resource tags associated with static route"""
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


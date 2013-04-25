
"""Creates a ACL rule the given network (the network has to belong to VPC)"""
from baseCmd import *
from baseResponse import *
class createNetworkACLCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """The network of the vm the ACL will be created for"""
        """Required"""
        self.networkid = None
        """the protocol for the ACL rule. Valid values are TCP/UDP/ICMP."""
        """Required"""
        self.protocol = None
        """the cidr list to allow traffic from/to"""
        self.cidrlist = []
        """the ending port of ACL"""
        self.endport = None
        """error code for this icmp message"""
        self.icmpcode = None
        """type of the icmp message being sent"""
        self.icmptype = None
        """the starting port of ACL"""
        self.startport = None
        """the traffic type for the ACL,can be Ingress or Egress, defaulted to Ingress if not specified"""
        self.traffictype = None
        self.required = ["networkid","protocol",]

class createNetworkACLResponse (baseResponse):
    def __init__(self):
        """the ID of the ACL"""
        self.id = None
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        """the ending port of ACL's port range"""
        self.endport = None
        """error code for this icmp message"""
        self.icmpcode = None
        """type of the icmp message being sent"""
        self.icmptype = None
        """the protocol of the ACL"""
        self.protocol = None
        """the starting port of ACL's port range"""
        self.startport = None
        """the state of the rule"""
        self.state = None
        """the traffic type for the ACL"""
        self.traffictype = None
        """the list of resource tags associated with the network ACLs"""
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



"""Lists all network ACLs"""
from baseCmd import *
from baseResponse import *
class listNetworkACLsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """Lists network ACL with the specified ID."""
        self.id = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """list network ACLs by network Id"""
        self.networkid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list objects by project"""
        self.projectid = None
        """List resources by tags (key/value pairs)"""
        self.tags = []
        """list network ACLs by traffic type - Ingress or Egress"""
        self.traffictype = None
        self.required = []

class listNetworkACLsResponse (baseResponse):
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


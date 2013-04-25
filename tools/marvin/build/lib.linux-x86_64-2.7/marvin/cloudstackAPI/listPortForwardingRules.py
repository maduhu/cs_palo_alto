
"""Lists all port forwarding rules for an IP address."""
from baseCmd import *
from baseResponse import *
class listPortForwardingRulesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """Lists rule with the specified ID."""
        self.id = None
        """the id of IP address of the port forwarding services"""
        self.ipaddressid = None
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
        """List resources by tags (key/value pairs)"""
        self.tags = []
        self.required = []

class listPortForwardingRulesResponse (baseResponse):
    def __init__(self):
        """the ID of the port forwarding rule"""
        self.id = None
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        """the public ip address for the port forwarding rule"""
        self.ipaddress = None
        """the public ip address id for the port forwarding rule"""
        self.ipaddressid = None
        """the ending port of port forwarding rule's private port range"""
        self.privateendport = None
        """the starting port of port forwarding rule's private port range"""
        self.privateport = None
        """the protocol of the port forwarding rule"""
        self.protocol = None
        """the ending port of port forwarding rule's private port range"""
        self.publicendport = None
        """the starting port of port forwarding rule's public port range"""
        self.publicport = None
        """the state of the rule"""
        self.state = None
        """the VM display name for the port forwarding rule"""
        self.virtualmachinedisplayname = None
        """the VM ID for the port forwarding rule"""
        self.virtualmachineid = None
        """the VM name for the port forwarding rule"""
        self.virtualmachinename = None
        """the list of resource tags associated with the rule"""
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



"""Creates an ip forwarding rule"""
from baseCmd import *
from baseResponse import *
class createIpForwardingRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the public IP address id of the forwarding rule, already associated via associateIp"""
        """Required"""
        self.ipaddressid = None
        """the protocol for the rule. Valid values are TCP or UDP."""
        """Required"""
        self.protocol = None
        """the start port for the rule"""
        """Required"""
        self.startport = None
        """the cidr list to forward traffic from"""
        self.cidrlist = []
        """the end port for the rule"""
        self.endport = None
        """if true, firewall rule for source/end pubic port is automatically created; if false - firewall rule has to be created explicitely. Has value true by default"""
        self.openfirewall = None
        self.required = ["ipaddressid","protocol","startport",]

class createIpForwardingRuleResponse (baseResponse):
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



"""Authorizes a particular egress rule for this security group"""
from baseCmd import *
from baseResponse import *
class authorizeSecurityGroupEgressCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """an optional account for the security group. Must be used with domainId."""
        self.account = None
        """the cidr list associated"""
        self.cidrlist = []
        """an optional domainId for the security group. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        """end port for this egress rule"""
        self.endport = None
        """error code for this icmp message"""
        self.icmpcode = None
        """type of the icmp message being sent"""
        self.icmptype = None
        """an optional project of the security group"""
        self.projectid = None
        """TCP is default. UDP is the other supported protocol"""
        self.protocol = None
        """The ID of the security group. Mutually exclusive with securityGroupName parameter"""
        self.securitygroupid = None
        """The name of the security group. Mutually exclusive with securityGroupName parameter"""
        self.securitygroupname = None
        """start port for this egress rule"""
        self.startport = None
        """user to security group mapping"""
        self.usersecuritygrouplist = []
        self.required = []

class authorizeSecurityGroupEgressResponse (baseResponse):
    def __init__(self):
        """account owning the security group rule"""
        self.account = None
        """the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """the ending IP of the security group rule"""
        self.endport = None
        """the code for the ICMP message response"""
        self.icmpcode = None
        """the type of the ICMP message response"""
        self.icmptype = None
        """the protocol of the security group rule"""
        self.protocol = None
        """the id of the security group rule"""
        self.ruleid = None
        """security group name"""
        self.securitygroupname = None
        """the starting IP of the security group rule"""
        self.startport = None


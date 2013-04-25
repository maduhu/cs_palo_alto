
"""List routers."""
from baseCmd import *
from baseResponse import *
class listRoutersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """if true is passed for this parameter, list only VPC routers"""
        self.forvpc = None
        """the host ID of the router"""
        self.hostid = None
        """the ID of the disk router"""
        self.id = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """the name of the router"""
        self.name = None
        """list by network id"""
        self.networkid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the Pod ID of the router"""
        self.podid = None
        """list objects by project"""
        self.projectid = None
        """the state of the router"""
        self.state = None
        """List networks by VPC"""
        self.vpcid = None
        """the Zone ID of the router"""
        self.zoneid = None
        self.required = []

class listRoutersResponse (baseResponse):
    def __init__(self):
        """the id of the router"""
        self.id = None
        """the account associated with the router"""
        self.account = None
        """the date and time the router was created"""
        self.created = None
        """the first DNS for the router"""
        self.dns1 = None
        """the second DNS for the router"""
        self.dns2 = None
        """the domain associated with the router"""
        self.domain = None
        """the domain ID associated with the router"""
        self.domainid = None
        """the gateway for the router"""
        self.gateway = None
        """the guest IP address for the router"""
        self.guestipaddress = None
        """the guest MAC address for the router"""
        self.guestmacaddress = None
        """the guest netmask for the router"""
        self.guestnetmask = None
        """the ID of the corresponding guest network"""
        self.guestnetworkid = None
        """the host ID for the router"""
        self.hostid = None
        """the hostname for the router"""
        self.hostname = None
        """if this router is an redundant virtual router"""
        self.isredundantrouter = None
        """the link local IP address for the router"""
        self.linklocalip = None
        """the link local MAC address for the router"""
        self.linklocalmacaddress = None
        """the link local netmask for the router"""
        self.linklocalnetmask = None
        """the ID of the corresponding link local network"""
        self.linklocalnetworkid = None
        """the name of the router"""
        self.name = None
        """the network domain for the router"""
        self.networkdomain = None
        """the Pod ID for the router"""
        self.podid = None
        """the project name of the address"""
        self.project = None
        """the project id of the ipaddress"""
        self.projectid = None
        """the public IP address for the router"""
        self.publicip = None
        """the public MAC address for the router"""
        self.publicmacaddress = None
        """the public netmask for the router"""
        self.publicnetmask = None
        """the ID of the corresponding public network"""
        self.publicnetworkid = None
        """the state of redundant virtual router"""
        self.redundantstate = None
        """the version of scripts"""
        self.scriptsversion = None
        """the ID of the service offering of the virtual machine"""
        self.serviceofferingid = None
        """the name of the service offering of the virtual machine"""
        self.serviceofferingname = None
        """the state of the router"""
        self.state = None
        """the template ID for the router"""
        self.templateid = None
        """the version of template"""
        self.templateversion = None
        """VPC the network belongs to"""
        self.vpcid = None
        """the Zone ID for the router"""
        self.zoneid = None
        """the Zone name for the router"""
        self.zonename = None
        """the list of nics associated with the router"""
        self.nic = []

class nic:
    def __init__(self):
        """"the ID of the nic"""
        self.id = None
        """"the broadcast uri of the nic"""
        self.broadcasturi = None
        """"the gateway of the nic"""
        self.gateway = None
        """"the ip address of the nic"""
        self.ipaddress = None
        """"true if nic is default, false otherwise"""
        self.isdefault = None
        """"the isolation uri of the nic"""
        self.isolationuri = None
        """"true if nic is default, false otherwise"""
        self.macaddress = None
        """"the netmask of the nic"""
        self.netmask = None
        """"the ID of the corresponding network"""
        self.networkid = None
        """"the name of the corresponding network"""
        self.networkname = None
        """"the traffic type of the nic"""
        self.traffictype = None
        """"the type of the nic"""
        self.type = None


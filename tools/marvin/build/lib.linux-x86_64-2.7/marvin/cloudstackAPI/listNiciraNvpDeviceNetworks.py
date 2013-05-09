
"""lists network that are using a nicira nvp device"""
from baseCmd import *
from baseResponse import *
class listNiciraNvpDeviceNetworksCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """nicira nvp device ID"""
        """Required"""
        self.nvpdeviceid = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = ["nvpdeviceid",]

class listNiciraNvpDeviceNetworksResponse (baseResponse):
    def __init__(self):
        """the id of the network"""
        self.id = None
        """the owner of the network"""
        self.account = None
        """acl type - access type to the network"""
        self.acltype = None
        """Broadcast domain type of the network"""
        self.broadcastdomaintype = None
        """broadcast uri of the network. This parameter is visible to ROOT admins only"""
        self.broadcasturi = None
        """list networks available for vm deployment"""
        self.canusefordeploy = None
        """the cidr the network"""
        self.cidr = None
        """the displaytext of the network"""
        self.displaytext = None
        """the first DNS for the network"""
        self.dns1 = None
        """the second DNS for the network"""
        self.dns2 = None
        """the domain name of the network owner"""
        self.domain = None
        """the domain id of the network owner"""
        self.domainid = None
        """the network's gateway"""
        self.gateway = None
        """true if network is default, false otherwise"""
        self.isdefault = None
        """true if network is system, false otherwise"""
        self.issystem = None
        """the name of the network"""
        self.name = None
        """the network's netmask"""
        self.netmask = None
        """the network domain"""
        self.networkdomain = None
        """availability of the network offering the network is created from"""
        self.networkofferingavailability = None
        """display text of the network offering the network is created from"""
        self.networkofferingdisplaytext = None
        """network offering id the network is created from"""
        self.networkofferingid = None
        """name of the network offering the network is created from"""
        self.networkofferingname = None
        """the physical network id"""
        self.physicalnetworkid = None
        """the project name of the address"""
        self.project = None
        """the project id of the ipaddress"""
        self.projectid = None
        """related to what other network configuration"""
        self.related = None
        """true network requires restart"""
        self.restartrequired = None
        """true if network supports specifying ip ranges, false otherwise"""
        self.specifyipranges = None
        """state of the network"""
        self.state = None
        """true if users from subdomains can access the domain level network"""
        self.subdomainaccess = None
        """the traffic type of the network"""
        self.traffictype = None
        """the type of the network"""
        self.type = None
        """The vlan of the network. This parameter is visible to ROOT admins only"""
        self.vlan = None
        """VPC the network belongs to"""
        self.vpcid = None
        """zone id of the network"""
        self.zoneid = None
        """the name of the zone the network belongs to"""
        self.zonename = None
        """the list of services"""
        self.service = []
        """the list of resource tags associated with network"""
        self.tags = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class service:
    def __init__(self):
        """"the service name"""
        self.name = None
        """"the service provider name"""
        self.provider = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

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

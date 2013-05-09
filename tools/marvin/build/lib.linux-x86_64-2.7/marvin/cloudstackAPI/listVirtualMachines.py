
"""List the virtual machines owned by the account."""
from baseCmd import *
from baseResponse import *
class listVirtualMachinesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """comma separated list of host details requested, value can be a list of [all, group, nics, stats, secgrp, tmpl, servoff, iso, volume, min]. If no parameter is passed in, the details will be defaulted to all"""
        self.details = []
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """list by network type; true if need to list vms using Virtual Network, false otherwise"""
        self.forvirtualnetwork = None
        """the group ID"""
        self.groupid = None
        """the host ID"""
        self.hostid = None
        """the target hypervisor for the template"""
        self.hypervisor = None
        """the ID of the virtual machine"""
        self.id = None
        """list vms by iso"""
        self.isoid = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """name of the virtual machine"""
        self.name = None
        """list by network id"""
        self.networkid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the pod ID"""
        self.podid = None
        """list objects by project"""
        self.projectid = None
        """state of the virtual machine"""
        self.state = None
        """the storage ID where vm's volumes belong to"""
        self.storageid = None
        """List resources by tags (key/value pairs)"""
        self.tags = []
        """list vms by template"""
        self.templateid = None
        """list vms by vpc"""
        self.vpcid = None
        """the availability zone ID"""
        self.zoneid = None
        self.required = []

class listVirtualMachinesResponse (baseResponse):
    def __init__(self):
        """the ID of the virtual machine"""
        self.id = None
        """the account associated with the virtual machine"""
        self.account = None
        """the number of cpu this virtual machine is running with"""
        self.cpunumber = None
        """the speed of each cpu"""
        self.cpuspeed = None
        """the amount of the vm's CPU currently used"""
        self.cpuused = None
        """the date when this virtual machine was created"""
        self.created = None
        """user generated name. The name of the virtual machine is returned if no displayname exists."""
        self.displayname = None
        """the name of the domain in which the virtual machine exists"""
        self.domain = None
        """the ID of the domain in which the virtual machine exists"""
        self.domainid = None
        """the virtual network for the service offering"""
        self.forvirtualnetwork = None
        """the group name of the virtual machine"""
        self.group = None
        """the group ID of the virtual machine"""
        self.groupid = None
        """Os type ID of the virtual machine"""
        self.guestosid = None
        """true if high-availability is enabled, false otherwise"""
        self.haenable = None
        """the ID of the host for the virtual machine"""
        self.hostid = None
        """the name of the host for the virtual machine"""
        self.hostname = None
        """the hypervisor on which the template runs"""
        self.hypervisor = None
        """instance name of the user vm; this parameter is returned to the ROOT admin only"""
        self.instancename = None
        """an alternate display text of the ISO attached to the virtual machine"""
        self.isodisplaytext = None
        """the ID of the ISO attached to the virtual machine"""
        self.isoid = None
        """the name of the ISO attached to the virtual machine"""
        self.isoname = None
        """ssh key-pair"""
        self.keypair = None
        """the memory allocated for the virtual machine"""
        self.memory = None
        """the name of the virtual machine"""
        self.name = None
        """the incoming network traffic on the vm"""
        self.networkkbsread = None
        """the outgoing network traffic on the host"""
        self.networkkbswrite = None
        """the password (if exists) of the virtual machine"""
        self.password = None
        """true if the password rest feature is enabled, false otherwise"""
        self.passwordenabled = None
        """the project name of the vm"""
        self.project = None
        """the project id of the vm"""
        self.projectid = None
        """public IP address id associated with vm via Static nat rule"""
        self.publicip = None
        """public IP address id associated with vm via Static nat rule"""
        self.publicipid = None
        """device ID of the root volume"""
        self.rootdeviceid = None
        """device type of the root volume"""
        self.rootdevicetype = None
        """the ID of the service offering of the virtual machine"""
        self.serviceofferingid = None
        """the name of the service offering of the virtual machine"""
        self.serviceofferingname = None
        """the state of the virtual machine"""
        self.state = None
        """an alternate display text of the template for the virtual machine"""
        self.templatedisplaytext = None
        """the ID of the template for the virtual machine. A -1 is returned if the virtual machine was created from an ISO file."""
        self.templateid = None
        """the name of the template for the virtual machine"""
        self.templatename = None
        """the ID of the availablility zone for the virtual machine"""
        self.zoneid = None
        """the name of the availability zone for the virtual machine"""
        self.zonename = None
        """the list of nics associated with vm"""
        self.nic = []
        """list of security groups associated with the virtual machine"""
        self.securitygroup = []
        """the list of resource tags associated with vm"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None

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

class egressrule:
    def __init__(self):
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None

class ingressrule:
    def __init__(self):
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None

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

class securitygroup:
    def __init__(self):
        """"the ID of the security group"""
        self.id = None
        """"the account owning the security group"""
        self.account = None
        """"the description of the security group"""
        self.description = None
        """"the domain name of the security group"""
        self.domain = None
        """"the domain ID of the security group"""
        self.domainid = None
        """"the name of the security group"""
        self.name = None
        """"the project name of the group"""
        self.project = None
        """"the project id of the group"""
        self.projectid = None
        """"the list of egress rules associated with the security group"""
        self.egressrule = []
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of ingress rules associated with the security group"""
        self.ingressrule = []
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
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
        """"the ID of the latest async job acting on this object"""
        self.jobid = None
        """"the current status of the latest async job acting on this object"""
        self.jobstatus = None

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

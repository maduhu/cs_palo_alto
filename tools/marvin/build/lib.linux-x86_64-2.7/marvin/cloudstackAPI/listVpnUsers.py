
"""Lists vpn users"""
from baseCmd import *
from baseResponse import *
class listVpnUsersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """The uuid of the Vpn user"""
        self.id = None
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
        """the username of the vpn user."""
        self.username = None
        self.required = []

class listVpnUsersResponse (baseResponse):
    def __init__(self):
        """the vpn userID"""
        self.id = None
        """the account of the remote access vpn"""
        self.account = None
        """the domain name of the account of the remote access vpn"""
        self.domain = None
        """the domain id of the account of the remote access vpn"""
        self.domainid = None
        """the project name of the vpn"""
        self.project = None
        """the project id of the vpn"""
        self.projectid = None
        """the username of the vpn user"""
        self.username = None


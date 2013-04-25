
"""Lists user accounts"""
from baseCmd import *
from baseResponse import *
class listUsersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """List users by account type. Valid types include admin, domain-admin, read-only-admin, or user."""
        self.accounttype = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """List user by ID."""
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
        """List users by state of the user account."""
        self.state = None
        """List user by the username"""
        self.username = None
        self.required = []

class listUsersResponse (baseResponse):
    def __init__(self):
        """the user ID"""
        self.id = None
        """the account name of the user"""
        self.account = None
        """the account ID of the user"""
        self.accountid = None
        """the account type of the user"""
        self.accounttype = None
        """the api key of the user"""
        self.apikey = None
        """the date and time the user account was created"""
        self.created = None
        """the domain name of the user"""
        self.domain = None
        """the domain ID of the user"""
        self.domainid = None
        """the user email address"""
        self.email = None
        """the user firstname"""
        self.firstname = None
        """the boolean value representing if the updating target is in caller's child domain"""
        self.iscallerchilddomain = None
        """the user lastname"""
        self.lastname = None
        """the secret key of the user"""
        self.secretkey = None
        """the user state"""
        self.state = None
        """the timezone user was created in"""
        self.timezone = None
        """the user name"""
        self.username = None


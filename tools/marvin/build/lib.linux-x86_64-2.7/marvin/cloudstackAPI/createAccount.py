
"""Creates an account"""
from baseCmd import *
from baseResponse import *
class createAccountCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Type of the account.  Specify 0 for user, 1 for root admin, and 2 for domain admin"""
        """Required"""
        self.accounttype = None
        """email"""
        """Required"""
        self.email = None
        """firstname"""
        """Required"""
        self.firstname = None
        """lastname"""
        """Required"""
        self.lastname = None
        """Hashed password (Default is MD5). If you wish to use any other hashing algorithm, you would need to write a custom authentication adapter See Docs section."""
        """Required"""
        self.password = None
        """Unique username."""
        """Required"""
        self.username = None
        """Creates the user under the specified account. If no account is specified, the username will be used as the account name."""
        self.account = None
        """details for account used to store specific parameters"""
        self.accountdetails = []
        """Creates the user under the specified domain."""
        self.domainid = None
        """Network domain for the account's networks"""
        self.networkdomain = None
        """Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."""
        self.timezone = None
        self.required = ["accounttype","email","firstname","lastname","password","username",]

class createAccountResponse (baseResponse):
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


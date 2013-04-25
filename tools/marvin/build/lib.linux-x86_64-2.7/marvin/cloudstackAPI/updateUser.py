
"""Updates a user account"""
from baseCmd import *
from baseResponse import *
class updateUserCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """User uuid"""
        """Required"""
        self.id = None
        """email"""
        self.email = None
        """first name"""
        self.firstname = None
        """last name"""
        self.lastname = None
        """Hashed password (default is MD5). If you wish to use any other hasing algorithm, you would need to write a custom authentication adapter"""
        self.password = None
        """Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."""
        self.timezone = None
        """The API key for the user. Must be specified with userSecretKey"""
        self.userapikey = None
        """Unique username"""
        self.username = None
        """The secret key for the user. Must be specified with userApiKey"""
        self.usersecretkey = None
        self.required = ["id",]

class updateUserResponse (baseResponse):
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


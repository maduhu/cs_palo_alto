
"""Logs a user into the CloudStack. A successful login attempt will generate a JSESSIONID cookie value that can be passed in subsequent Query command calls until the "logout" command has been issued or the session has expired."""
from baseCmd import *
from baseResponse import *
class loginCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Username"""
        """Required"""
        self.username = None
        """Hashed password (Default is MD5). If you wish to use any other hashing algorithm, you would need to write a custom authentication adapter See Docs section."""
        """Required"""
        self.password = None
        """path of the domain that the user belongs to. Example: domain=/com/cloud/internal.  If no domain is passed in, the ROOT domain is assumed."""
        self.domain = None
        """id of the domain that the user belongs to. If both domain and domainId are passed in, "domainId" parameter takes precendence"""
        self.domainId = None
        self.required = ["username","password",]

class loginResponse (baseResponse):
    def __init__(self):
        """Username"""
        self.username = None
        """User id"""
        self.userid = None
        """Password"""
        self.password = None
        """domain ID that the user belongs to"""
        self.domainid = None
        """the time period before the session has expired"""
        self.timeout = None
        """the account name the user belongs to"""
        self.account = None
        """first name of the user"""
        self.firstname = None
        """last name of the user"""
        self.lastname = None
        """the account type (admin, domain-admin, read-only-admin, user)"""
        self.type = None
        """user time zone"""
        self.timezone = None
        """user time zone offset from UTC 00:00"""
        self.timezoneoffset = None
        """Session key that can be passed in subsequent Query command calls"""
        self.sessionkey = None


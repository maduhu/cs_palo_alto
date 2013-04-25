
"""Remove the LDAP context for this site."""
from baseCmd import *
from baseResponse import *
class ldapRemoveCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class ldapRemoveResponse (baseResponse):
    def __init__(self):
        """Specify the distinguished name of a user with the search permission on the directory"""
        self.binddn = None
        """DN password"""
        self.bindpass = None
        """Hostname or ip address of the ldap server eg: my.ldap.com"""
        self.hostname = None
        """Specify the LDAP port if required, default is 389"""
        self.port = None
        """Check Use SSL if the external LDAP server is configured for LDAP over SSL"""
        self.port = None
        """You specify a query filter here, which narrows down the users, who can be part of this domain"""
        self.queryfilter = None
        """The search base defines the starting point for the search in the directory tree Example:  dc=cloud,dc=com"""
        self.searchbase = None


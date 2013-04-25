
"""Reset api count"""
from baseCmd import *
from baseResponse import *
class resetApiLimitCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the acount whose limit to be reset"""
        self.account = None
        self.required = []

class resetApiLimitResponse (baseResponse):
    def __init__(self):
        """the account name of the api remaining count"""
        self.account = None
        """the account uuid of the api remaining count"""
        self.accountid = None
        """currently allowed number of apis"""
        self.apiAllowed = None
        """number of api already issued"""
        self.apiIssued = None
        """seconds left to reset counters"""
        self.expireAfter = None


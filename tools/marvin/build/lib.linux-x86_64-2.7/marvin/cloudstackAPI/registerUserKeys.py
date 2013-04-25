
"""This command allows a user to register for the developer API, returning a secret key and an API key. This request is made through the integration API port, so it is a privileged command and must be made on behalf of a user. It is up to the implementer just how the username and password are entered, and then how that translates to an integration API request. Both secret key and API key should be returned to the user"""
from baseCmd import *
from baseResponse import *
class registerUserKeysCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """User id"""
        """Required"""
        self.id = None
        self.required = ["id",]

class registerUserKeysResponse (baseResponse):
    def __init__(self):
        """the api key of the registered user"""
        self.apikey = None
        """the secret key of the registered user"""
        self.secretkey = None



"""Returns an encrypted password for the VM"""
from baseCmd import *
from baseResponse import *
class getVMPasswordCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """The ID of the virtual machine"""
        """Required"""
        self.id = None
        self.required = ["id",]

class getVMPasswordResponse (baseResponse):
    def __init__(self):
        """The encrypted password of the VM"""
        self.encryptedpassword = None


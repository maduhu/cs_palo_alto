
"""Update password of a host/pool on management server."""
from baseCmd import *
from baseResponse import *
class updateHostPasswordCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the new password for the host/cluster"""
        """Required"""
        self.password = None
        """the username for the host/cluster"""
        """Required"""
        self.username = None
        """the cluster ID"""
        self.clusterid = None
        """the host ID"""
        self.hostid = None
        self.required = ["password","username",]

class updateHostPasswordResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None


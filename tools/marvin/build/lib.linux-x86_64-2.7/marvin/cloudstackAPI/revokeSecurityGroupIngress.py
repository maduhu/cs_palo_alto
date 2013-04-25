
"""Deletes a particular ingress rule from this security group"""
from baseCmd import *
from baseResponse import *
class revokeSecurityGroupIngressCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """The ID of the ingress rule"""
        """Required"""
        self.id = None
        self.required = ["id",]

class revokeSecurityGroupIngressResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None


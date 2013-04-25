
"""Accepts or declines project invitation"""
from baseCmd import *
from baseResponse import *
class deleteProjectInvitationCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of the invitation"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteProjectInvitationResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None



"""Accepts or declines project invitation"""
from baseCmd import *
from baseResponse import *
class updateProjectInvitationCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of the project to join"""
        """Required"""
        self.projectid = None
        """if true, accept the invitation, decline if false. True by default"""
        self.accept = None
        """account that is joining the project"""
        self.account = None
        """list invitations for specified account; this parameter has to be specified with domainId"""
        self.token = None
        self.required = ["projectid",]

class updateProjectInvitationResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None


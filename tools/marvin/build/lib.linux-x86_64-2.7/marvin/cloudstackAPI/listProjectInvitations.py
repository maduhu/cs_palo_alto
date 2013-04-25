
"""Lists projects and provides detailed information for listed projects"""
from baseCmd import *
from baseResponse import *
class listProjectInvitationsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """if true, list only active invitations - having Pending state and ones that are not timed out yet"""
        self.activeonly = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """list invitations by id"""
        self.id = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list by project id"""
        self.projectid = None
        """list invitations by state"""
        self.state = None
        self.required = []

class listProjectInvitationsResponse (baseResponse):
    def __init__(self):
        """the id of the invitation"""
        self.id = None
        """the account name of the project's owner"""
        self.account = None
        """the domain name where the project belongs to"""
        self.domain = None
        """the domain id the project belongs to"""
        self.domainid = None
        """the email the invitation was sent to"""
        self.email = None
        """the name of the project"""
        self.project = None
        """the id of the project"""
        self.projectid = None
        """the invitation state"""
        self.state = None



"""Updates iso permissions"""
from baseCmd import *
from baseResponse import *
class updateIsoPermissionsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the template ID"""
        """Required"""
        self.id = None
        """a comma delimited list of accounts. If specified, "op" parameter has to be passed in."""
        self.accounts = []
        """true if the template/iso is extractable, false other wise. Can be set only by root admin"""
        self.isextractable = None
        """true for featured template/iso, false otherwise"""
        self.isfeatured = None
        """true for public template/iso, false for private templates/isos"""
        self.ispublic = None
        """permission operator (add, remove, reset)"""
        self.op = None
        """a comma delimited list of projects. If specified, "op" parameter has to be passed in."""
        self.projectids = []
        self.required = ["id",]

class updateIsoPermissionsResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None


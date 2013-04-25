
"""Lists snapshot policies."""
from baseCmd import *
from baseResponse import *
class listSnapshotPoliciesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the disk volume"""
        """Required"""
        self.volumeid = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = ["volumeid",]

class listSnapshotPoliciesResponse (baseResponse):
    def __init__(self):
        """the ID of the snapshot policy"""
        self.id = None
        """the interval type of the snapshot policy"""
        self.intervaltype = None
        """maximum number of snapshots retained"""
        self.maxsnaps = None
        """time the snapshot is scheduled to be taken."""
        self.schedule = None
        """the time zone of the snapshot policy"""
        self.timezone = None
        """the ID of the disk volume"""
        self.volumeid = None


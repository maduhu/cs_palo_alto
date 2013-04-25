
"""Lists all available snapshots for the account."""
from baseCmd import *
from baseResponse import *
class listSnapshotsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """lists snapshot by snapshot ID"""
        self.id = None
        """valid values are HOURLY, DAILY, WEEKLY, and MONTHLY."""
        self.intervaltype = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """lists snapshot by snapshot name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list objects by project"""
        self.projectid = None
        """valid values are MANUAL or RECURRING."""
        self.snapshottype = None
        """List resources by tags (key/value pairs)"""
        self.tags = []
        """the ID of the disk volume"""
        self.volumeid = None
        self.required = []

class listSnapshotsResponse (baseResponse):
    def __init__(self):
        """ID of the snapshot"""
        self.id = None
        """the account associated with the snapshot"""
        self.account = None
        """the date the snapshot was created"""
        self.created = None
        """the domain name of the snapshot's account"""
        self.domain = None
        """the domain ID of the snapshot's account"""
        self.domainid = None
        """valid types are hourly, daily, weekly, monthy, template, and none."""
        self.intervaltype = None
        """name of the snapshot"""
        self.name = None
        """the project name of the snapshot"""
        self.project = None
        """the project id of the snapshot"""
        self.projectid = None
        """the type of the snapshot"""
        self.snapshottype = None
        """the state of the snapshot. BackedUp means that snapshot is ready to be used; Creating - the snapshot is being allocated on the primary storage; BackingUp - the snapshot is being backed up on secondary storage"""
        self.state = None
        """ID of the disk volume"""
        self.volumeid = None
        """name of the disk volume"""
        self.volumename = None
        """type of the disk volume"""
        self.volumetype = None
        """the list of resource tags associated with snapshot"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None


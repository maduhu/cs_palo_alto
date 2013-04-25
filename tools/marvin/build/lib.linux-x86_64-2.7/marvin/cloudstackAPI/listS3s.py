
"""Lists S3s"""
from baseCmd import *
from baseResponse import *
class listS3sCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listS3sResponse (baseResponse):
    def __init__(self):
        """The ID of the S3 configuration"""
        self.id = None
        """The S3 access key"""
        self.accesskey = None
        """The name of the template storage bucket"""
        self.bucket = None
        """The connection timeout (milliseconds)"""
        self.connectiontimeout = None
        """The S3 end point"""
        self.endpoint = None
        """The maximum number of time to retry a connection on error."""
        self.maxerrorretry = None
        """The S3 secret key"""
        self.secretkey = None
        """The connection socket (milliseconds)"""
        self.sockettimeout = None
        """Connect to S3 using HTTPS?"""
        self.usehttps = None


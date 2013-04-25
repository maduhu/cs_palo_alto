
"""Adds S3"""
from baseCmd import *
from baseResponse import *
class addS3Cmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """S3 access key"""
        """Required"""
        self.accesskey = None
        """name of the template storage bucket"""
        """Required"""
        self.bucket = None
        """S3 secret key"""
        """Required"""
        self.secretkey = None
        """connection timeout (milliseconds)"""
        self.connectiontimeout = None
        """S3 host name"""
        self.endpoint = None
        """maximum number of times to retry on error"""
        self.maxerrorretry = None
        """socket timeout (milliseconds)"""
        self.sockettimeout = None
        """connect to the S3 endpoint via HTTPS?"""
        self.usehttps = None
        self.required = ["accesskey","bucket","secretkey",]

class addS3Response (baseResponse):
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


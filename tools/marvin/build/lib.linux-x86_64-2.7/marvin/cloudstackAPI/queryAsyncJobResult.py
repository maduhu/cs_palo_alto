
"""Retrieves the current status of asynchronous job."""
from baseCmd import *
from baseResponse import *
class queryAsyncJobResultCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the asychronous job"""
        """Required"""
        self.jobid = None
        self.required = ["jobid",]

class queryAsyncJobResultResponse (baseResponse):
    def __init__(self):
        """the account that executed the async command"""
        self.accountid = None
        """the async command executed"""
        self.cmd = None
        """the created date of the job"""
        self.created = None
        """the unique ID of the instance/entity object related to the job"""
        self.jobinstanceid = None
        """the instance/entity object related to the job"""
        self.jobinstancetype = None
        """the progress information of the PENDING job"""
        self.jobprocstatus = None
        """the result reason"""
        self.jobresult = None
        """the result code for the job"""
        self.jobresultcode = None
        """the result type"""
        self.jobresulttype = None
        """the current job status-should be 0 for PENDING"""
        self.jobstatus = None
        """the user that executed the async command"""
        self.userid = None
        """the ID of the async job"""
        self.jobid = None


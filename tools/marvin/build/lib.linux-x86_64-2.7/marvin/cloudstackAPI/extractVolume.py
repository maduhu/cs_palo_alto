
"""Extracts volume"""
from baseCmd import *
from baseResponse import *
class extractVolumeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the volume"""
        """Required"""
        self.id = None
        """the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD"""
        """Required"""
        self.mode = None
        """the ID of the zone where the volume is located"""
        """Required"""
        self.zoneid = None
        """the url to which the volume would be extracted"""
        self.url = None
        self.required = ["id","mode","zoneid",]

class extractVolumeResponse (baseResponse):
    def __init__(self):
        """the id of extracted object"""
        self.id = None
        """the account id to which the extracted object belongs"""
        self.accountid = None
        """the time and date the object was created"""
        self.created = None
        """the upload id of extracted object"""
        self.extractId = None
        """the mode of extraction - upload or download"""
        self.extractMode = None
        """the name of the extracted object"""
        self.name = None
        """the state of the extracted object"""
        self.state = None
        """the status of the extraction"""
        self.status = None
        """type of the storage"""
        self.storagetype = None
        """the percentage of the entity uploaded to the specified location"""
        self.uploadpercentage = None
        """if mode = upload then url of the uploaded entity. if mode = download the url from which the entity can be downloaded"""
        self.url = None
        """zone ID the object was extracted from"""
        self.zoneid = None
        """zone name the object was extracted from"""
        self.zonename = None


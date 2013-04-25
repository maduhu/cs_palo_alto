
"""Logs out the user"""
from baseCmd import *
from baseResponse import *
class logoutCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class logoutResponse (baseResponse):
    def __init__(self):
        """success if the logout action succeeded"""
        self.description = None


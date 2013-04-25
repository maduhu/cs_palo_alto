
"""Uploads a custom certificate for the console proxy VMs to use for SSL. Can be used to upload a single certificate signed by a known CA. Can also be used, through multiple calls, to upload a chain of certificates from CA to the custom certificate itself."""
from baseCmd import *
from baseResponse import *
class uploadCustomCertificateCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """The certificate to be uploaded."""
        """Required"""
        self.certificate = None
        """DNS domain suffix that the certificate is granted for."""
        """Required"""
        self.domainsuffix = None
        """An integer providing the location in a chain that the certificate will hold. Usually, this can be left empty. When creating a chain, the top level certificate should have an ID of 1, with each step in the chain incrementing by one. Example, CA with id = 1, Intermediate CA with id = 2, Site certificate with ID = 3"""
        self.id = None
        """A name / alias for the certificate."""
        self.name = None
        """The private key for the attached certificate."""
        self.privatekey = None
        self.required = ["certificate","domainsuffix",]

class uploadCustomCertificateResponse (baseResponse):
    def __init__(self):
        """message of the certificate upload operation"""
        self.message = None


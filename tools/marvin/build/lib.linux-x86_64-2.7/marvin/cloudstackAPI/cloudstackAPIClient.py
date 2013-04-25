"""Test Client for CloudStack API"""
import copy
from createAccount import createAccountResponse
from deleteAccount import deleteAccountResponse
from updateAccount import updateAccountResponse
from disableAccount import disableAccountResponse
from enableAccount import enableAccountResponse
from lockAccount import lockAccountResponse
from listAccounts import listAccountsResponse
from markDefaultZoneForAccount import markDefaultZoneForAccountResponse
from createUser import createUserResponse
from deleteUser import deleteUserResponse
from updateUser import updateUserResponse
from listUsers import listUsersResponse
from lockUser import lockUserResponse
from disableUser import disableUserResponse
from enableUser import enableUserResponse
from getUser import getUserResponse
from createDomain import createDomainResponse
from updateDomain import updateDomainResponse
from deleteDomain import deleteDomainResponse
from listDomains import listDomainsResponse
from listDomainChildren import listDomainChildrenResponse
from getCloudIdentifier import getCloudIdentifierResponse
from updateResourceLimit import updateResourceLimitResponse
from updateResourceCount import updateResourceCountResponse
from listResourceLimits import listResourceLimitsResponse
from deployVirtualMachine import deployVirtualMachineResponse
from destroyVirtualMachine import destroyVirtualMachineResponse
from rebootVirtualMachine import rebootVirtualMachineResponse
from startVirtualMachine import startVirtualMachineResponse
from stopVirtualMachine import stopVirtualMachineResponse
from resetPasswordForVirtualMachine import resetPasswordForVirtualMachineResponse
from updateVirtualMachine import updateVirtualMachineResponse
from listVirtualMachines import listVirtualMachinesResponse
from getVMPassword import getVMPasswordResponse
from restoreVirtualMachine import restoreVirtualMachineResponse
from changeServiceForVirtualMachine import changeServiceForVirtualMachineResponse
from assignVirtualMachine import assignVirtualMachineResponse
from migrateVirtualMachine import migrateVirtualMachineResponse
from recoverVirtualMachine import recoverVirtualMachineResponse
from createSnapshot import createSnapshotResponse
from listSnapshots import listSnapshotsResponse
from deleteSnapshot import deleteSnapshotResponse
from createSnapshotPolicy import createSnapshotPolicyResponse
from deleteSnapshotPolicies import deleteSnapshotPoliciesResponse
from listSnapshotPolicies import listSnapshotPoliciesResponse
from createTemplate import createTemplateResponse
from registerTemplate import registerTemplateResponse
from updateTemplate import updateTemplateResponse
from copyTemplate import copyTemplateResponse
from deleteTemplate import deleteTemplateResponse
from listTemplates import listTemplatesResponse
from updateTemplatePermissions import updateTemplatePermissionsResponse
from listTemplatePermissions import listTemplatePermissionsResponse
from extractTemplate import extractTemplateResponse
from prepareTemplate import prepareTemplateResponse
from attachIso import attachIsoResponse
from detachIso import detachIsoResponse
from listIsos import listIsosResponse
from registerIso import registerIsoResponse
from updateIso import updateIsoResponse
from deleteIso import deleteIsoResponse
from copyIso import copyIsoResponse
from updateIsoPermissions import updateIsoPermissionsResponse
from listIsoPermissions import listIsoPermissionsResponse
from extractIso import extractIsoResponse
from listOsTypes import listOsTypesResponse
from listOsCategories import listOsCategoriesResponse
from createServiceOffering import createServiceOfferingResponse
from deleteServiceOffering import deleteServiceOfferingResponse
from updateServiceOffering import updateServiceOfferingResponse
from listServiceOfferings import listServiceOfferingsResponse
from createDiskOffering import createDiskOfferingResponse
from updateDiskOffering import updateDiskOfferingResponse
from deleteDiskOffering import deleteDiskOfferingResponse
from listDiskOfferings import listDiskOfferingsResponse
from createVlanIpRange import createVlanIpRangeResponse
from deleteVlanIpRange import deleteVlanIpRangeResponse
from listVlanIpRanges import listVlanIpRangesResponse
from associateIpAddress import associateIpAddressResponse
from disassociateIpAddress import disassociateIpAddressResponse
from listPublicIpAddresses import listPublicIpAddressesResponse
from listPortForwardingRules import listPortForwardingRulesResponse
from createPortForwardingRule import createPortForwardingRuleResponse
from deletePortForwardingRule import deletePortForwardingRuleResponse
from updatePortForwardingRule import updatePortForwardingRuleResponse
from enableStaticNat import enableStaticNatResponse
from createIpForwardingRule import createIpForwardingRuleResponse
from deleteIpForwardingRule import deleteIpForwardingRuleResponse
from listIpForwardingRules import listIpForwardingRulesResponse
from disableStaticNat import disableStaticNatResponse
from createLoadBalancerRule import createLoadBalancerRuleResponse
from deleteLoadBalancerRule import deleteLoadBalancerRuleResponse
from removeFromLoadBalancerRule import removeFromLoadBalancerRuleResponse
from assignToLoadBalancerRule import assignToLoadBalancerRuleResponse
from createLBStickinessPolicy import createLBStickinessPolicyResponse
from deleteLBStickinessPolicy import deleteLBStickinessPolicyResponse
from listLoadBalancerRules import listLoadBalancerRulesResponse
from listLBStickinessPolicies import listLBStickinessPoliciesResponse
from listLoadBalancerRuleInstances import listLoadBalancerRuleInstancesResponse
from updateLoadBalancerRule import updateLoadBalancerRuleResponse
from createCounter import createCounterResponse
from createCondition import createConditionResponse
from createAutoScalePolicy import createAutoScalePolicyResponse
from createAutoScaleVmProfile import createAutoScaleVmProfileResponse
from createAutoScaleVmGroup import createAutoScaleVmGroupResponse
from deleteCounter import deleteCounterResponse
from deleteCondition import deleteConditionResponse
from deleteAutoScalePolicy import deleteAutoScalePolicyResponse
from deleteAutoScaleVmProfile import deleteAutoScaleVmProfileResponse
from deleteAutoScaleVmGroup import deleteAutoScaleVmGroupResponse
from listCounters import listCountersResponse
from listConditions import listConditionsResponse
from listAutoScalePolicies import listAutoScalePoliciesResponse
from listAutoScaleVmProfiles import listAutoScaleVmProfilesResponse
from listAutoScaleVmGroups import listAutoScaleVmGroupsResponse
from enableAutoScaleVmGroup import enableAutoScaleVmGroupResponse
from disableAutoScaleVmGroup import disableAutoScaleVmGroupResponse
from updateAutoScalePolicy import updateAutoScalePolicyResponse
from updateAutoScaleVmProfile import updateAutoScaleVmProfileResponse
from updateAutoScaleVmGroup import updateAutoScaleVmGroupResponse
from startRouter import startRouterResponse
from rebootRouter import rebootRouterResponse
from stopRouter import stopRouterResponse
from destroyRouter import destroyRouterResponse
from changeServiceForRouter import changeServiceForRouterResponse
from listRouters import listRoutersResponse
from listVirtualRouterElements import listVirtualRouterElementsResponse
from configureVirtualRouterElement import configureVirtualRouterElementResponse
from createVirtualRouterElement import createVirtualRouterElementResponse
from startSystemVm import startSystemVmResponse
from rebootSystemVm import rebootSystemVmResponse
from stopSystemVm import stopSystemVmResponse
from destroySystemVm import destroySystemVmResponse
from listSystemVms import listSystemVmsResponse
from migrateSystemVm import migrateSystemVmResponse
from changeServiceForSystemVm import changeServiceForSystemVmResponse
from updateConfiguration import updateConfigurationResponse
from listConfigurations import listConfigurationsResponse
from ldapConfig import ldapConfigResponse
from ldapRemove import ldapRemoveResponse
from listCapabilities import listCapabilitiesResponse
from createPod import createPodResponse
from updatePod import updatePodResponse
from deletePod import deletePodResponse
from listPods import listPodsResponse
from createZone import createZoneResponse
from updateZone import updateZoneResponse
from deleteZone import deleteZoneResponse
from listZones import listZonesResponse
from listEvents import listEventsResponse
from listEventTypes import listEventTypesResponse
from listAlerts import listAlertsResponse
from listCapacity import listCapacityResponse
from addSwift import addSwiftResponse
from listSwifts import listSwiftsResponse
from addS3 import addS3Response
from listS3s import listS3sResponse
from addHost import addHostResponse
from addCluster import addClusterResponse
from deleteCluster import deleteClusterResponse
from updateCluster import updateClusterResponse
from reconnectHost import reconnectHostResponse
from updateHost import updateHostResponse
from deleteHost import deleteHostResponse
from prepareHostForMaintenance import prepareHostForMaintenanceResponse
from cancelHostMaintenance import cancelHostMaintenanceResponse
from listHosts import listHostsResponse
from addSecondaryStorage import addSecondaryStorageResponse
from updateHostPassword import updateHostPasswordResponse
from attachVolume import attachVolumeResponse
from uploadVolume import uploadVolumeResponse
from detachVolume import detachVolumeResponse
from createVolume import createVolumeResponse
from deleteVolume import deleteVolumeResponse
from listVolumes import listVolumesResponse
from extractVolume import extractVolumeResponse
from migrateVolume import migrateVolumeResponse
from resizeVolume import resizeVolumeResponse
from registerUserKeys import registerUserKeysResponse
from queryAsyncJobResult import queryAsyncJobResultResponse
from listAsyncJobs import listAsyncJobsResponse
from listStoragePools import listStoragePoolsResponse
from createStoragePool import createStoragePoolResponse
from updateStoragePool import updateStoragePoolResponse
from deleteStoragePool import deleteStoragePoolResponse
from listClusters import listClustersResponse
from enableStorageMaintenance import enableStorageMaintenanceResponse
from cancelStorageMaintenance import cancelStorageMaintenanceResponse
from createSecurityGroup import createSecurityGroupResponse
from deleteSecurityGroup import deleteSecurityGroupResponse
from authorizeSecurityGroupIngress import authorizeSecurityGroupIngressResponse
from revokeSecurityGroupIngress import revokeSecurityGroupIngressResponse
from authorizeSecurityGroupEgress import authorizeSecurityGroupEgressResponse
from revokeSecurityGroupEgress import revokeSecurityGroupEgressResponse
from listSecurityGroups import listSecurityGroupsResponse
from createInstanceGroup import createInstanceGroupResponse
from deleteInstanceGroup import deleteInstanceGroupResponse
from updateInstanceGroup import updateInstanceGroupResponse
from listInstanceGroups import listInstanceGroupsResponse
from uploadCustomCertificate import uploadCustomCertificateResponse
from listHypervisors import listHypervisorsResponse
from createRemoteAccessVpn import createRemoteAccessVpnResponse
from deleteRemoteAccessVpn import deleteRemoteAccessVpnResponse
from listRemoteAccessVpns import listRemoteAccessVpnsResponse
from addVpnUser import addVpnUserResponse
from removeVpnUser import removeVpnUserResponse
from listVpnUsers import listVpnUsersResponse
from createNetworkOffering import createNetworkOfferingResponse
from updateNetworkOffering import updateNetworkOfferingResponse
from deleteNetworkOffering import deleteNetworkOfferingResponse
from listNetworkOfferings import listNetworkOfferingsResponse
from createNetwork import createNetworkResponse
from deleteNetwork import deleteNetworkResponse
from listNetworks import listNetworksResponse
from restartNetwork import restartNetworkResponse
from updateNetwork import updateNetworkResponse
from registerSSHKeyPair import registerSSHKeyPairResponse
from createSSHKeyPair import createSSHKeyPairResponse
from deleteSSHKeyPair import deleteSSHKeyPairResponse
from listSSHKeyPairs import listSSHKeyPairsResponse
from createProject import createProjectResponse
from deleteProject import deleteProjectResponse
from updateProject import updateProjectResponse
from activateProject import activateProjectResponse
from suspendProject import suspendProjectResponse
from listProjects import listProjectsResponse
from addAccountToProject import addAccountToProjectResponse
from deleteAccountFromProject import deleteAccountFromProjectResponse
from listProjectAccounts import listProjectAccountsResponse
from listProjectInvitations import listProjectInvitationsResponse
from updateProjectInvitation import updateProjectInvitationResponse
from deleteProjectInvitation import deleteProjectInvitationResponse
from createFirewallRule import createFirewallRuleResponse
from deleteFirewallRule import deleteFirewallRuleResponse
from listFirewallRules import listFirewallRulesResponse
from updateHypervisorCapabilities import updateHypervisorCapabilitiesResponse
from listHypervisorCapabilities import listHypervisorCapabilitiesResponse
from createPhysicalNetwork import createPhysicalNetworkResponse
from deletePhysicalNetwork import deletePhysicalNetworkResponse
from listPhysicalNetworks import listPhysicalNetworksResponse
from updatePhysicalNetwork import updatePhysicalNetworkResponse
from listSupportedNetworkServices import listSupportedNetworkServicesResponse
from addNetworkServiceProvider import addNetworkServiceProviderResponse
from deleteNetworkServiceProvider import deleteNetworkServiceProviderResponse
from listNetworkServiceProviders import listNetworkServiceProvidersResponse
from updateNetworkServiceProvider import updateNetworkServiceProviderResponse
from addTrafficType import addTrafficTypeResponse
from deleteTrafficType import deleteTrafficTypeResponse
from listTrafficTypes import listTrafficTypesResponse
from updateTrafficType import updateTrafficTypeResponse
from listTrafficTypeImplementors import listTrafficTypeImplementorsResponse
from createStorageNetworkIpRange import createStorageNetworkIpRangeResponse
from deleteStorageNetworkIpRange import deleteStorageNetworkIpRangeResponse
from listStorageNetworkIpRange import listStorageNetworkIpRangeResponse
from updateStorageNetworkIpRange import updateStorageNetworkIpRangeResponse
from addNetworkDevice import addNetworkDeviceResponse
from listNetworkDevice import listNetworkDeviceResponse
from deleteNetworkDevice import deleteNetworkDeviceResponse
from createVPC import createVPCResponse
from listVPCs import listVPCsResponse
from deleteVPC import deleteVPCResponse
from updateVPC import updateVPCResponse
from restartVPC import restartVPCResponse
from createVPCOffering import createVPCOfferingResponse
from updateVPCOffering import updateVPCOfferingResponse
from deleteVPCOffering import deleteVPCOfferingResponse
from listVPCOfferings import listVPCOfferingsResponse
from createPrivateGateway import createPrivateGatewayResponse
from listPrivateGateways import listPrivateGatewaysResponse
from deletePrivateGateway import deletePrivateGatewayResponse
from createNetworkACL import createNetworkACLResponse
from deleteNetworkACL import deleteNetworkACLResponse
from listNetworkACLs import listNetworkACLsResponse
from createStaticRoute import createStaticRouteResponse
from deleteStaticRoute import deleteStaticRouteResponse
from listStaticRoutes import listStaticRoutesResponse
from createTags import createTagsResponse
from deleteTags import deleteTagsResponse
from listTags import listTagsResponse
from createVpnCustomerGateway import createVpnCustomerGatewayResponse
from createVpnGateway import createVpnGatewayResponse
from createVpnConnection import createVpnConnectionResponse
from deleteVpnCustomerGateway import deleteVpnCustomerGatewayResponse
from deleteVpnGateway import deleteVpnGatewayResponse
from deleteVpnConnection import deleteVpnConnectionResponse
from updateVpnCustomerGateway import updateVpnCustomerGatewayResponse
from resetVpnConnection import resetVpnConnectionResponse
from listVpnCustomerGateways import listVpnCustomerGatewaysResponse
from listVpnGateways import listVpnGatewaysResponse
from listVpnConnections import listVpnConnectionsResponse
from generateUsageRecords import generateUsageRecordsResponse
from listUsageRecords import listUsageRecordsResponse
from listUsageTypes import listUsageTypesResponse
from addTrafficMonitor import addTrafficMonitorResponse
from deleteTrafficMonitor import deleteTrafficMonitorResponse
from listTrafficMonitors import listTrafficMonitorsResponse
from addNiciraNvpDevice import addNiciraNvpDeviceResponse
from deleteNiciraNvpDevice import deleteNiciraNvpDeviceResponse
from listNiciraNvpDevices import listNiciraNvpDevicesResponse
from listNiciraNvpDeviceNetworks import listNiciraNvpDeviceNetworksResponse
from listApis import listApisResponse
from getApiLimit import getApiLimitResponse
from resetApiLimit import resetApiLimitResponse
from login import loginResponse
from logout import logoutResponse
class CloudStackAPIClient:
    def __init__(self, connection):
        self.connection = connection

    def __copy__(self):
        return CloudStackAPIClient(copy.copy(self.connection))

    def createAccount(self,command):
        response = createAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteAccount(self,command):
        response = deleteAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateAccount(self,command):
        response = updateAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def disableAccount(self,command):
        response = disableAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def enableAccount(self,command):
        response = enableAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def lockAccount(self,command):
        response = lockAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def listAccounts(self,command):
        response = listAccountsResponse()
        response = self.connection.make_request(command, response)
        return response

    def markDefaultZoneForAccount(self,command):
        response = markDefaultZoneForAccountResponse()
        response = self.connection.make_request(command, response)
        return response

    def createUser(self,command):
        response = createUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteUser(self,command):
        response = deleteUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateUser(self,command):
        response = updateUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def listUsers(self,command):
        response = listUsersResponse()
        response = self.connection.make_request(command, response)
        return response

    def lockUser(self,command):
        response = lockUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def disableUser(self,command):
        response = disableUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def enableUser(self,command):
        response = enableUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def getUser(self,command):
        response = getUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def createDomain(self,command):
        response = createDomainResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateDomain(self,command):
        response = updateDomainResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteDomain(self,command):
        response = deleteDomainResponse()
        response = self.connection.make_request(command, response)
        return response

    def listDomains(self,command):
        response = listDomainsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listDomainChildren(self,command):
        response = listDomainChildrenResponse()
        response = self.connection.make_request(command, response)
        return response

    def getCloudIdentifier(self,command):
        response = getCloudIdentifierResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateResourceLimit(self,command):
        response = updateResourceLimitResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateResourceCount(self,command):
        response = updateResourceCountResponse()
        response = self.connection.make_request(command, response)
        return response

    def listResourceLimits(self,command):
        response = listResourceLimitsResponse()
        response = self.connection.make_request(command, response)
        return response

    def deployVirtualMachine(self,command):
        response = deployVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def destroyVirtualMachine(self,command):
        response = destroyVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def rebootVirtualMachine(self,command):
        response = rebootVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def startVirtualMachine(self,command):
        response = startVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def stopVirtualMachine(self,command):
        response = stopVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def resetPasswordForVirtualMachine(self,command):
        response = resetPasswordForVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateVirtualMachine(self,command):
        response = updateVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVirtualMachines(self,command):
        response = listVirtualMachinesResponse()
        response = self.connection.make_request(command, response)
        return response

    def getVMPassword(self,command):
        response = getVMPasswordResponse()
        response = self.connection.make_request(command, response)
        return response

    def restoreVirtualMachine(self,command):
        response = restoreVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def changeServiceForVirtualMachine(self,command):
        response = changeServiceForVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def assignVirtualMachine(self,command):
        response = assignVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def migrateVirtualMachine(self,command):
        response = migrateVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def recoverVirtualMachine(self,command):
        response = recoverVirtualMachineResponse()
        response = self.connection.make_request(command, response)
        return response

    def createSnapshot(self,command):
        response = createSnapshotResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSnapshots(self,command):
        response = listSnapshotsResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteSnapshot(self,command):
        response = deleteSnapshotResponse()
        response = self.connection.make_request(command, response)
        return response

    def createSnapshotPolicy(self,command):
        response = createSnapshotPolicyResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteSnapshotPolicies(self,command):
        response = deleteSnapshotPoliciesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSnapshotPolicies(self,command):
        response = listSnapshotPoliciesResponse()
        response = self.connection.make_request(command, response)
        return response

    def createTemplate(self,command):
        response = createTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def registerTemplate(self,command):
        response = registerTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateTemplate(self,command):
        response = updateTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def copyTemplate(self,command):
        response = copyTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteTemplate(self,command):
        response = deleteTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def listTemplates(self,command):
        response = listTemplatesResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateTemplatePermissions(self,command):
        response = updateTemplatePermissionsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listTemplatePermissions(self,command):
        response = listTemplatePermissionsResponse()
        response = self.connection.make_request(command, response)
        return response

    def extractTemplate(self,command):
        response = extractTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def prepareTemplate(self,command):
        response = prepareTemplateResponse()
        response = self.connection.make_request(command, response)
        return response

    def attachIso(self,command):
        response = attachIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def detachIso(self,command):
        response = detachIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def listIsos(self,command):
        response = listIsosResponse()
        response = self.connection.make_request(command, response)
        return response

    def registerIso(self,command):
        response = registerIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateIso(self,command):
        response = updateIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteIso(self,command):
        response = deleteIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def copyIso(self,command):
        response = copyIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateIsoPermissions(self,command):
        response = updateIsoPermissionsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listIsoPermissions(self,command):
        response = listIsoPermissionsResponse()
        response = self.connection.make_request(command, response)
        return response

    def extractIso(self,command):
        response = extractIsoResponse()
        response = self.connection.make_request(command, response)
        return response

    def listOsTypes(self,command):
        response = listOsTypesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listOsCategories(self,command):
        response = listOsCategoriesResponse()
        response = self.connection.make_request(command, response)
        return response

    def createServiceOffering(self,command):
        response = createServiceOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteServiceOffering(self,command):
        response = deleteServiceOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateServiceOffering(self,command):
        response = updateServiceOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def listServiceOfferings(self,command):
        response = listServiceOfferingsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createDiskOffering(self,command):
        response = createDiskOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateDiskOffering(self,command):
        response = updateDiskOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteDiskOffering(self,command):
        response = deleteDiskOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def listDiskOfferings(self,command):
        response = listDiskOfferingsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVlanIpRange(self,command):
        response = createVlanIpRangeResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVlanIpRange(self,command):
        response = deleteVlanIpRangeResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVlanIpRanges(self,command):
        response = listVlanIpRangesResponse()
        response = self.connection.make_request(command, response)
        return response

    def associateIpAddress(self,command):
        response = associateIpAddressResponse()
        response = self.connection.make_request(command, response)
        return response

    def disassociateIpAddress(self,command):
        response = disassociateIpAddressResponse()
        response = self.connection.make_request(command, response)
        return response

    def listPublicIpAddresses(self,command):
        response = listPublicIpAddressesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listPortForwardingRules(self,command):
        response = listPortForwardingRulesResponse()
        response = self.connection.make_request(command, response)
        return response

    def createPortForwardingRule(self,command):
        response = createPortForwardingRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def deletePortForwardingRule(self,command):
        response = deletePortForwardingRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def updatePortForwardingRule(self,command):
        response = updatePortForwardingRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def enableStaticNat(self,command):
        response = enableStaticNatResponse()
        response = self.connection.make_request(command, response)
        return response

    def createIpForwardingRule(self,command):
        response = createIpForwardingRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteIpForwardingRule(self,command):
        response = deleteIpForwardingRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def listIpForwardingRules(self,command):
        response = listIpForwardingRulesResponse()
        response = self.connection.make_request(command, response)
        return response

    def disableStaticNat(self,command):
        response = disableStaticNatResponse()
        response = self.connection.make_request(command, response)
        return response

    def createLoadBalancerRule(self,command):
        response = createLoadBalancerRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteLoadBalancerRule(self,command):
        response = deleteLoadBalancerRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def removeFromLoadBalancerRule(self,command):
        response = removeFromLoadBalancerRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def assignToLoadBalancerRule(self,command):
        response = assignToLoadBalancerRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def createLBStickinessPolicy(self,command):
        response = createLBStickinessPolicyResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteLBStickinessPolicy(self,command):
        response = deleteLBStickinessPolicyResponse()
        response = self.connection.make_request(command, response)
        return response

    def listLoadBalancerRules(self,command):
        response = listLoadBalancerRulesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listLBStickinessPolicies(self,command):
        response = listLBStickinessPoliciesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listLoadBalancerRuleInstances(self,command):
        response = listLoadBalancerRuleInstancesResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateLoadBalancerRule(self,command):
        response = updateLoadBalancerRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def createCounter(self,command):
        response = createCounterResponse()
        response = self.connection.make_request(command, response)
        return response

    def createCondition(self,command):
        response = createConditionResponse()
        response = self.connection.make_request(command, response)
        return response

    def createAutoScalePolicy(self,command):
        response = createAutoScalePolicyResponse()
        response = self.connection.make_request(command, response)
        return response

    def createAutoScaleVmProfile(self,command):
        response = createAutoScaleVmProfileResponse()
        response = self.connection.make_request(command, response)
        return response

    def createAutoScaleVmGroup(self,command):
        response = createAutoScaleVmGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteCounter(self,command):
        response = deleteCounterResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteCondition(self,command):
        response = deleteConditionResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteAutoScalePolicy(self,command):
        response = deleteAutoScalePolicyResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteAutoScaleVmProfile(self,command):
        response = deleteAutoScaleVmProfileResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteAutoScaleVmGroup(self,command):
        response = deleteAutoScaleVmGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def listCounters(self,command):
        response = listCountersResponse()
        response = self.connection.make_request(command, response)
        return response

    def listConditions(self,command):
        response = listConditionsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listAutoScalePolicies(self,command):
        response = listAutoScalePoliciesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listAutoScaleVmProfiles(self,command):
        response = listAutoScaleVmProfilesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listAutoScaleVmGroups(self,command):
        response = listAutoScaleVmGroupsResponse()
        response = self.connection.make_request(command, response)
        return response

    def enableAutoScaleVmGroup(self,command):
        response = enableAutoScaleVmGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def disableAutoScaleVmGroup(self,command):
        response = disableAutoScaleVmGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateAutoScalePolicy(self,command):
        response = updateAutoScalePolicyResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateAutoScaleVmProfile(self,command):
        response = updateAutoScaleVmProfileResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateAutoScaleVmGroup(self,command):
        response = updateAutoScaleVmGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def startRouter(self,command):
        response = startRouterResponse()
        response = self.connection.make_request(command, response)
        return response

    def rebootRouter(self,command):
        response = rebootRouterResponse()
        response = self.connection.make_request(command, response)
        return response

    def stopRouter(self,command):
        response = stopRouterResponse()
        response = self.connection.make_request(command, response)
        return response

    def destroyRouter(self,command):
        response = destroyRouterResponse()
        response = self.connection.make_request(command, response)
        return response

    def changeServiceForRouter(self,command):
        response = changeServiceForRouterResponse()
        response = self.connection.make_request(command, response)
        return response

    def listRouters(self,command):
        response = listRoutersResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVirtualRouterElements(self,command):
        response = listVirtualRouterElementsResponse()
        response = self.connection.make_request(command, response)
        return response

    def configureVirtualRouterElement(self,command):
        response = configureVirtualRouterElementResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVirtualRouterElement(self,command):
        response = createVirtualRouterElementResponse()
        response = self.connection.make_request(command, response)
        return response

    def startSystemVm(self,command):
        response = startSystemVmResponse()
        response = self.connection.make_request(command, response)
        return response

    def rebootSystemVm(self,command):
        response = rebootSystemVmResponse()
        response = self.connection.make_request(command, response)
        return response

    def stopSystemVm(self,command):
        response = stopSystemVmResponse()
        response = self.connection.make_request(command, response)
        return response

    def destroySystemVm(self,command):
        response = destroySystemVmResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSystemVms(self,command):
        response = listSystemVmsResponse()
        response = self.connection.make_request(command, response)
        return response

    def migrateSystemVm(self,command):
        response = migrateSystemVmResponse()
        response = self.connection.make_request(command, response)
        return response

    def changeServiceForSystemVm(self,command):
        response = changeServiceForSystemVmResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateConfiguration(self,command):
        response = updateConfigurationResponse()
        response = self.connection.make_request(command, response)
        return response

    def listConfigurations(self,command):
        response = listConfigurationsResponse()
        response = self.connection.make_request(command, response)
        return response

    def ldapConfig(self,command):
        response = ldapConfigResponse()
        response = self.connection.make_request(command, response)
        return response

    def ldapRemove(self,command):
        response = ldapRemoveResponse()
        response = self.connection.make_request(command, response)
        return response

    def listCapabilities(self,command):
        response = listCapabilitiesResponse()
        response = self.connection.make_request(command, response)
        return response

    def createPod(self,command):
        response = createPodResponse()
        response = self.connection.make_request(command, response)
        return response

    def updatePod(self,command):
        response = updatePodResponse()
        response = self.connection.make_request(command, response)
        return response

    def deletePod(self,command):
        response = deletePodResponse()
        response = self.connection.make_request(command, response)
        return response

    def listPods(self,command):
        response = listPodsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createZone(self,command):
        response = createZoneResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateZone(self,command):
        response = updateZoneResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteZone(self,command):
        response = deleteZoneResponse()
        response = self.connection.make_request(command, response)
        return response

    def listZones(self,command):
        response = listZonesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listEvents(self,command):
        response = listEventsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listEventTypes(self,command):
        response = listEventTypesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listAlerts(self,command):
        response = listAlertsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listCapacity(self,command):
        response = listCapacityResponse()
        response = self.connection.make_request(command, response)
        return response

    def addSwift(self,command):
        response = addSwiftResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSwifts(self,command):
        response = listSwiftsResponse()
        response = self.connection.make_request(command, response)
        return response

    def addS3(self,command):
        response = addS3Response()
        response = self.connection.make_request(command, response)
        return response

    def listS3s(self,command):
        response = listS3sResponse()
        response = self.connection.make_request(command, response)
        return response

    def addHost(self,command):
        response = addHostResponse()
        response = self.connection.make_request(command, response)
        return response

    def addCluster(self,command):
        response = addClusterResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteCluster(self,command):
        response = deleteClusterResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateCluster(self,command):
        response = updateClusterResponse()
        response = self.connection.make_request(command, response)
        return response

    def reconnectHost(self,command):
        response = reconnectHostResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateHost(self,command):
        response = updateHostResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteHost(self,command):
        response = deleteHostResponse()
        response = self.connection.make_request(command, response)
        return response

    def prepareHostForMaintenance(self,command):
        response = prepareHostForMaintenanceResponse()
        response = self.connection.make_request(command, response)
        return response

    def cancelHostMaintenance(self,command):
        response = cancelHostMaintenanceResponse()
        response = self.connection.make_request(command, response)
        return response

    def listHosts(self,command):
        response = listHostsResponse()
        response = self.connection.make_request(command, response)
        return response

    def addSecondaryStorage(self,command):
        response = addSecondaryStorageResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateHostPassword(self,command):
        response = updateHostPasswordResponse()
        response = self.connection.make_request(command, response)
        return response

    def attachVolume(self,command):
        response = attachVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def uploadVolume(self,command):
        response = uploadVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def detachVolume(self,command):
        response = detachVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVolume(self,command):
        response = createVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVolume(self,command):
        response = deleteVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVolumes(self,command):
        response = listVolumesResponse()
        response = self.connection.make_request(command, response)
        return response

    def extractVolume(self,command):
        response = extractVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def migrateVolume(self,command):
        response = migrateVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def resizeVolume(self,command):
        response = resizeVolumeResponse()
        response = self.connection.make_request(command, response)
        return response

    def registerUserKeys(self,command):
        response = registerUserKeysResponse()
        response = self.connection.make_request(command, response)
        return response

    def queryAsyncJobResult(self,command):
        response = queryAsyncJobResultResponse()
        response = self.connection.make_request(command, response)
        return response

    def listAsyncJobs(self,command):
        response = listAsyncJobsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listStoragePools(self,command):
        response = listStoragePoolsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createStoragePool(self,command):
        response = createStoragePoolResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateStoragePool(self,command):
        response = updateStoragePoolResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteStoragePool(self,command):
        response = deleteStoragePoolResponse()
        response = self.connection.make_request(command, response)
        return response

    def listClusters(self,command):
        response = listClustersResponse()
        response = self.connection.make_request(command, response)
        return response

    def enableStorageMaintenance(self,command):
        response = enableStorageMaintenanceResponse()
        response = self.connection.make_request(command, response)
        return response

    def cancelStorageMaintenance(self,command):
        response = cancelStorageMaintenanceResponse()
        response = self.connection.make_request(command, response)
        return response

    def createSecurityGroup(self,command):
        response = createSecurityGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteSecurityGroup(self,command):
        response = deleteSecurityGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def authorizeSecurityGroupIngress(self,command):
        response = authorizeSecurityGroupIngressResponse()
        response = self.connection.make_request(command, response)
        return response

    def revokeSecurityGroupIngress(self,command):
        response = revokeSecurityGroupIngressResponse()
        response = self.connection.make_request(command, response)
        return response

    def authorizeSecurityGroupEgress(self,command):
        response = authorizeSecurityGroupEgressResponse()
        response = self.connection.make_request(command, response)
        return response

    def revokeSecurityGroupEgress(self,command):
        response = revokeSecurityGroupEgressResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSecurityGroups(self,command):
        response = listSecurityGroupsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createInstanceGroup(self,command):
        response = createInstanceGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteInstanceGroup(self,command):
        response = deleteInstanceGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateInstanceGroup(self,command):
        response = updateInstanceGroupResponse()
        response = self.connection.make_request(command, response)
        return response

    def listInstanceGroups(self,command):
        response = listInstanceGroupsResponse()
        response = self.connection.make_request(command, response)
        return response

    def uploadCustomCertificate(self,command):
        response = uploadCustomCertificateResponse()
        response = self.connection.make_request(command, response)
        return response

    def listHypervisors(self,command):
        response = listHypervisorsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createRemoteAccessVpn(self,command):
        response = createRemoteAccessVpnResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteRemoteAccessVpn(self,command):
        response = deleteRemoteAccessVpnResponse()
        response = self.connection.make_request(command, response)
        return response

    def listRemoteAccessVpns(self,command):
        response = listRemoteAccessVpnsResponse()
        response = self.connection.make_request(command, response)
        return response

    def addVpnUser(self,command):
        response = addVpnUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def removeVpnUser(self,command):
        response = removeVpnUserResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVpnUsers(self,command):
        response = listVpnUsersResponse()
        response = self.connection.make_request(command, response)
        return response

    def createNetworkOffering(self,command):
        response = createNetworkOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateNetworkOffering(self,command):
        response = updateNetworkOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteNetworkOffering(self,command):
        response = deleteNetworkOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNetworkOfferings(self,command):
        response = listNetworkOfferingsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createNetwork(self,command):
        response = createNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteNetwork(self,command):
        response = deleteNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNetworks(self,command):
        response = listNetworksResponse()
        response = self.connection.make_request(command, response)
        return response

    def restartNetwork(self,command):
        response = restartNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateNetwork(self,command):
        response = updateNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def registerSSHKeyPair(self,command):
        response = registerSSHKeyPairResponse()
        response = self.connection.make_request(command, response)
        return response

    def createSSHKeyPair(self,command):
        response = createSSHKeyPairResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteSSHKeyPair(self,command):
        response = deleteSSHKeyPairResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSSHKeyPairs(self,command):
        response = listSSHKeyPairsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createProject(self,command):
        response = createProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteProject(self,command):
        response = deleteProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateProject(self,command):
        response = updateProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def activateProject(self,command):
        response = activateProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def suspendProject(self,command):
        response = suspendProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def listProjects(self,command):
        response = listProjectsResponse()
        response = self.connection.make_request(command, response)
        return response

    def addAccountToProject(self,command):
        response = addAccountToProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteAccountFromProject(self,command):
        response = deleteAccountFromProjectResponse()
        response = self.connection.make_request(command, response)
        return response

    def listProjectAccounts(self,command):
        response = listProjectAccountsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listProjectInvitations(self,command):
        response = listProjectInvitationsResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateProjectInvitation(self,command):
        response = updateProjectInvitationResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteProjectInvitation(self,command):
        response = deleteProjectInvitationResponse()
        response = self.connection.make_request(command, response)
        return response

    def createFirewallRule(self,command):
        response = createFirewallRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteFirewallRule(self,command):
        response = deleteFirewallRuleResponse()
        response = self.connection.make_request(command, response)
        return response

    def listFirewallRules(self,command):
        response = listFirewallRulesResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateHypervisorCapabilities(self,command):
        response = updateHypervisorCapabilitiesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listHypervisorCapabilities(self,command):
        response = listHypervisorCapabilitiesResponse()
        response = self.connection.make_request(command, response)
        return response

    def createPhysicalNetwork(self,command):
        response = createPhysicalNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def deletePhysicalNetwork(self,command):
        response = deletePhysicalNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def listPhysicalNetworks(self,command):
        response = listPhysicalNetworksResponse()
        response = self.connection.make_request(command, response)
        return response

    def updatePhysicalNetwork(self,command):
        response = updatePhysicalNetworkResponse()
        response = self.connection.make_request(command, response)
        return response

    def listSupportedNetworkServices(self,command):
        response = listSupportedNetworkServicesResponse()
        response = self.connection.make_request(command, response)
        return response

    def addNetworkServiceProvider(self,command):
        response = addNetworkServiceProviderResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteNetworkServiceProvider(self,command):
        response = deleteNetworkServiceProviderResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNetworkServiceProviders(self,command):
        response = listNetworkServiceProvidersResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateNetworkServiceProvider(self,command):
        response = updateNetworkServiceProviderResponse()
        response = self.connection.make_request(command, response)
        return response

    def addTrafficType(self,command):
        response = addTrafficTypeResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteTrafficType(self,command):
        response = deleteTrafficTypeResponse()
        response = self.connection.make_request(command, response)
        return response

    def listTrafficTypes(self,command):
        response = listTrafficTypesResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateTrafficType(self,command):
        response = updateTrafficTypeResponse()
        response = self.connection.make_request(command, response)
        return response

    def listTrafficTypeImplementors(self,command):
        response = listTrafficTypeImplementorsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createStorageNetworkIpRange(self,command):
        response = createStorageNetworkIpRangeResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteStorageNetworkIpRange(self,command):
        response = deleteStorageNetworkIpRangeResponse()
        response = self.connection.make_request(command, response)
        return response

    def listStorageNetworkIpRange(self,command):
        response = listStorageNetworkIpRangeResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateStorageNetworkIpRange(self,command):
        response = updateStorageNetworkIpRangeResponse()
        response = self.connection.make_request(command, response)
        return response

    def addNetworkDevice(self,command):
        response = addNetworkDeviceResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNetworkDevice(self,command):
        response = listNetworkDeviceResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteNetworkDevice(self,command):
        response = deleteNetworkDeviceResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVPC(self,command):
        response = createVPCResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVPCs(self,command):
        response = listVPCsResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVPC(self,command):
        response = deleteVPCResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateVPC(self,command):
        response = updateVPCResponse()
        response = self.connection.make_request(command, response)
        return response

    def restartVPC(self,command):
        response = restartVPCResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVPCOffering(self,command):
        response = createVPCOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateVPCOffering(self,command):
        response = updateVPCOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVPCOffering(self,command):
        response = deleteVPCOfferingResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVPCOfferings(self,command):
        response = listVPCOfferingsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createPrivateGateway(self,command):
        response = createPrivateGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def listPrivateGateways(self,command):
        response = listPrivateGatewaysResponse()
        response = self.connection.make_request(command, response)
        return response

    def deletePrivateGateway(self,command):
        response = deletePrivateGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def createNetworkACL(self,command):
        response = createNetworkACLResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteNetworkACL(self,command):
        response = deleteNetworkACLResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNetworkACLs(self,command):
        response = listNetworkACLsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createStaticRoute(self,command):
        response = createStaticRouteResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteStaticRoute(self,command):
        response = deleteStaticRouteResponse()
        response = self.connection.make_request(command, response)
        return response

    def listStaticRoutes(self,command):
        response = listStaticRoutesResponse()
        response = self.connection.make_request(command, response)
        return response

    def createTags(self,command):
        response = createTagsResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteTags(self,command):
        response = deleteTagsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listTags(self,command):
        response = listTagsResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVpnCustomerGateway(self,command):
        response = createVpnCustomerGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVpnGateway(self,command):
        response = createVpnGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def createVpnConnection(self,command):
        response = createVpnConnectionResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVpnCustomerGateway(self,command):
        response = deleteVpnCustomerGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVpnGateway(self,command):
        response = deleteVpnGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteVpnConnection(self,command):
        response = deleteVpnConnectionResponse()
        response = self.connection.make_request(command, response)
        return response

    def updateVpnCustomerGateway(self,command):
        response = updateVpnCustomerGatewayResponse()
        response = self.connection.make_request(command, response)
        return response

    def resetVpnConnection(self,command):
        response = resetVpnConnectionResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVpnCustomerGateways(self,command):
        response = listVpnCustomerGatewaysResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVpnGateways(self,command):
        response = listVpnGatewaysResponse()
        response = self.connection.make_request(command, response)
        return response

    def listVpnConnections(self,command):
        response = listVpnConnectionsResponse()
        response = self.connection.make_request(command, response)
        return response

    def generateUsageRecords(self,command):
        response = generateUsageRecordsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listUsageRecords(self,command):
        response = listUsageRecordsResponse()
        response = self.connection.make_request(command, response)
        return response

    def listUsageTypes(self,command):
        response = listUsageTypesResponse()
        response = self.connection.make_request(command, response)
        return response

    def addTrafficMonitor(self,command):
        response = addTrafficMonitorResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteTrafficMonitor(self,command):
        response = deleteTrafficMonitorResponse()
        response = self.connection.make_request(command, response)
        return response

    def listTrafficMonitors(self,command):
        response = listTrafficMonitorsResponse()
        response = self.connection.make_request(command, response)
        return response

    def addNiciraNvpDevice(self,command):
        response = addNiciraNvpDeviceResponse()
        response = self.connection.make_request(command, response)
        return response

    def deleteNiciraNvpDevice(self,command):
        response = deleteNiciraNvpDeviceResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNiciraNvpDevices(self,command):
        response = listNiciraNvpDevicesResponse()
        response = self.connection.make_request(command, response)
        return response

    def listNiciraNvpDeviceNetworks(self,command):
        response = listNiciraNvpDeviceNetworksResponse()
        response = self.connection.make_request(command, response)
        return response

    def listApis(self,command):
        response = listApisResponse()
        response = self.connection.make_request(command, response)
        return response

    def getApiLimit(self,command):
        response = getApiLimitResponse()
        response = self.connection.make_request(command, response)
        return response

    def resetApiLimit(self,command):
        response = resetApiLimitResponse()
        response = self.connection.make_request(command, response)
        return response

    def login(self,command):
        response = loginResponse()
        response = self.connection.make_request(command, response)
        return response

    def logout(self,command):
        response = logoutResponse()
        response = self.connection.make_request(command, response)
        return response


#!/usr/bin/env python2 
"""
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""
import os
import sys 

subscription_id = str(sys.argv[1])
client_ids = str(sys.argv[2])
key = str(sys.argv[3])
tenant_id = str(sys.argv[4])

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

resourcegroup = 'MC_VisperaResourceGroupTest_aks-vispera-test-anw_centralindia'
vmss_name = 'aks-general-14908190-vmss'
instance_id = '0'
credentials = ServicePrincipalCredentials(client_id=client_ids, secret=key, tenant=tenant_id)
client = ComputeManagementClient(credentials, subscription_id)
vmss = client.virtual_machine_scale_set_vms.start(resourcegroup,vmss_name,instance_id,custom_headers=None)




#!/usr/bin/env python
from snmp_helper import snmp_get_oid, snmp_extract

OID_list = ['1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.5.0']
IP = "184.105.247.70"
COMMUNITY_STRING = "galileo"
SNMP_PORT = 161

a_device = (IP,COMMUNITY_STRING,SNMP_PORT)
for oid in OID_list:
    snmp_data = snmp_get_oid(a_device, oid)
    print snmp_extract(snmp_data)

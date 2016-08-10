#!/usr/bin/env python
from snmp_helper import snmp_get_oid, snmp_extract

OID_list = ['1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.5.0']
OID_name = ['sysDscr', 'sysName']
IP_list = ["184.105.247.70", "184.105.247.71"]
COMMUNITY_STRING = "galileo"
SNMP_PORT = 161

for ip in IP_list:
    print "<<<<<<<<<",ip,">>>>>>>>>"
    a_device = (ip,COMMUNITY_STRING,SNMP_PORT)
    for i in range(len(OID_list)):
       print "==",OID_name[i],"=="
       snmp_data = snmp_get_oid(a_device, OID_list[i])
       print snmp_extract(snmp_data)

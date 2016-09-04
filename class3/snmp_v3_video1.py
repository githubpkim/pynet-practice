#!/usr/bin/env python

import snmp_helper

IP = '184.105.247.70'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (IP,161)
pynet_rtr2 = (IP,161)

snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1,snmp_user)
output = snmp_helper.snmp_extract(snmp_data)

print output

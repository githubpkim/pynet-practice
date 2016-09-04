#!/usr/bin/env python

import snmp_helper
import email_helper
import pickle

IP1 = '184.105.247.71'
IP2 = '184.105.247.71'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (IP1,161)
pynet_rtr2 = (IP2,161)

snmp_data1 = snmp_helper.snmp_get_oid_v3(pynet_rtr1,snmp_user,oid='1.3.6.1.4.1.9.9.43.1.1.1.0')
snmp_data2 = snmp_helper.snmp_get_oid_v3(pynet_rtr2,snmp_user,oid='1.3.6.1.4.1.9.9.43.1.1.1.0')
#snmp_data3 = snmp_helper.snmp_get_oid_v3(pynet_rtr2,snmp_user,oid='1.3.6.1.4.1.9.9.43.1.1.3.0')
#snmp_data4 = snmp_helper.snmp_get_oid_v3(pynet_rtr2,snmp_user,oid='1.3.6.1.2.1.1.3.0')
output1 = snmp_helper.snmp_extract(snmp_data1)
output2 = snmp_helper.snmp_extract(snmp_data2)
#output3 = snmp_helper.snmp_extract(snmp_data3)
#output4 = snmp_helper.snmp_extract(snmp_data4)

fp = open("./config_change.txt","wb")
pickle.dump(output1,fp)
pickle.dump(output2,fp)
fp.close()

# how to issue the snmp command regularly?
# how to compare the before and after? using pickle?


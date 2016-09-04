#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
import re
'''
Find all of the crypto map entries that are using PFS group2
'''

cisco_conf = CiscoConfParse("/home/pkim/ciscoconfparse/cisco.txt") #read cisco.txt file in CiscoConfParse format and set the filepoint named "cisco_conf"

crypto_no_aes = cisco_conf.find_objects_wo_child(parentspec = r"^crypto map CRYPTO", childspec = "AES") #return a list of parent lines in IOSCfgLine format 

for parent_line in crypto_no_aes:
    print parent_line.text
    for child in parent_line.children:  # make sure that tpye(parent_line.children) is a list !!
        print child.text
        if 'transform-set' in child.text:
            transform = re.findall('transform-set (.+)',child.text)
print "\n##Transform name:",transform

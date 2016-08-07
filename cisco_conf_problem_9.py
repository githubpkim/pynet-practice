from ciscoconfparse import CiscoConfParse
'''
Find all of the crypto map entries that are using PFS group2
'''

cisco_conf = CiscoConfParse("/home/pkim/ciscoconfparse/cisco.txt") #read cisco.txt file in CiscoConfParse format and set the filepoint named "cisco_conf"

crypto_group2 = cisco_conf.find_objects_w_child(parentspec = r"^crypto map CRYPTO", childspec = "group2") #return a list of parent lines in IOSCfgLine format 

for parent_line in crypto_group2:
    print parent_line.text
    for child in parent_line.children:  # make sure that tpye(parent_line.children) is a list !!
        print child.text

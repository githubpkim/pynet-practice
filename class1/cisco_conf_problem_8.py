from ciscoconfparse import CiscoConfParse
'''
The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
'''

cisco_conf = CiscoConfParse("./cisco.txt") #read cisco.txt file in CiscoConfParse format and set the filepoint named "cisco_conf"

crypto_maps = cisco_conf.find_objects(r"^crypto map CRYPTO") # find 'crypto map CRYPTO' and add them into a list with IOSCfgLine format

for crypto_map in crypto_maps: #list(crypto_maps) is used as iterative and crypto_map(list's element) in IOSCfgLine format
    print crypto_map.text  # print normal format converted from IOSCfgLine format with using "text" attribute
    for crypto_line in crypto_map.children: #list(crypto_maps.children) is used as iterative,the list's element in IOSCfgLine format
        print crypto_line.text # print normal format converted from IOSCfgLine format with using "text" attribute


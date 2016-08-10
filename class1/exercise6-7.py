import yaml
import json
from pprint import pprint as pp

my_list = range(10)
my_list.append("whatever")
my_list.append("python123")
my_list.append({})
my_list[-1]['ip_address'] = '172.16.100.1'
my_list[-1]['hostname'] = 'cr1.sjc2.turn.com'
my_list[-1]['attr'] = range(8)

print my_list

with open("my_file.yml",'w') as fp:
    fp.write(yaml.dump(my_list,default_flow_style = True))

with open('my_file.yml','r') as fp:
    new_list = yaml.load(fp)
print "=====pprint yaml file====="
pp(new_list)

with open("my_file.json", 'w') as fp:
    json.dump(my_list,fp)

with open("my_file.json") as fp:
    new_json_list = json.load(fp)

print "=====pprint json file====="
pp(new_json_list)

import json

f=open("cty.json",'r')
for line in f.readlines():
	json_data=json.loads(line)
#	print (json_data)
print (json_data['8J1RL'])
sub_data=json.dumps(json_data['8J1RL'])
sub_data_parsed=json.loads(sub_data)
print (sub_data_parsed['continent'])



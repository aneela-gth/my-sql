import json
ip=['apple','banana','grapes']
with open('data1.json','w')as f:
    # f.write(json.dumps(ip))
    json.dump(ip,f)

with open('data1.json','r')as f:
    data1=f.read()
    print(data1[2])
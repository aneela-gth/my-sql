import json
data={'name':'john','age':23,'gender':'femail'}
op=json.dumps(data) #use to convert as a json object
op=(str(data))
print(type(op))
# print(data['name'])

data1=['hello','hie','welcome']
op1=json.dumps(data1)#conver to json object
print(type(op1))
op2=json.loads(op1)
# print(data1[2])
# print(op1[2])
# op2=json.loads(op1)#cnvert to ist origineal form
print(type(op2))

# print(data1[2])
# print(op1[2])
# print(data['name'])
# with open('./product.json','w') as f:
#      json.dump()   
list=['aneela','naresh','akhila','alekhya','sunny','naveen']
with open('product.json','w')as f:
    data_json=json.dumps(list)
    f.write(data_json)

with open('product.json','r')as f:
    res=f.read()
    # print(res)
    cnvrt_data=json.loads(res)
    print(cnvrt_data[1])


#1. add few names into the existing list in the file
# remove any name
# names=['aneela','akhila','sunny']
# with open("product.json",'w')as f:
#     json.dump(names,f,indent=4)
# with open("product.json", "r") as f:
#     existing_names = json.load(f)
# print("Before update:", existing_names)
# new_names = ['naresh', 'naveen']
# existing_names.extend(new_names)
# if 'akhila' in existing_names:
#     existing_names.remove('akhila')
# with open("product.json", "w") as f:
#     json.dump(existing_names, f, indent=4)
# print("After update:", existing_names)



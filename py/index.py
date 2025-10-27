# adding operation only frof authorised persons
import json
ip=['apple','banana','grapes']
# with open('data.json','w')as f:
    # f.write( json.dumps(ip))
    # json.dump(ip,f)



# with open('data.json','r')as f:
    # data=f.read()
    # print(data[2])
    # convrt_data=json.loads(data)
    # print(convrt_data[2])
    # data=json.load(f)
    # print(data[1])
    

    
# 1.add element:

# ip1='pineapple'
# with open ('data.json')as f:
#     data=json.load(f) #data will change from json to list
#     data["fruits"].append(ip1) #new element will append into the list
# with open('data.json','w')as f:
#     json.dump(data,f)
#     print('data upadte sucessfully')


# 2.
# ip1='pineapple'
# with open ('data.json')as f:
#     data=json.load(f) #data will change from json to list
#     if ip1 not in data:
#         data['fruits'].append(ip1) #new element will append into the list
#     else:
#         print(f'{ip1} already exists')
# with open('data.json','w')as f:
#     json.dump(data,f)
#     print('data upadte sucessfully')



# 2.remove the pertuclurele element
# remove_element='graphes'
# file_name='data.json'
# with open(file_name,'r')as h:
#         data=json.load(h)
#         if remove_element not in data["fruits"]:
#             print(f"{remove_element}is not available")
#         else:
#             data["fruits"].remove(remove_element)
#             print(f"{remove_element} is removed sucessfully")
# with open(file_name,'w')as f:
#     json.dump(data,f) 

#2.
# remove_element='grapes'
# file_name='data.json'
# user="aneela"
# with open(file_name,'r')as h:
#     data=json.load(h)
#     if user in data["users"]:
#         if remove_element not in data["fruits"]:
#                 print(f"{remove_element}is not available")
#         else:
#             data["fruits"].remove(remove_element)
#             print(f"{remove_element} is removed sucessfully")
#     else:
#          print("u r not authorised to perfrom remove operaction")
# with open(file_name,'w')as f:
#     json.dump(data,f) 


# remove operaction only for authorised persons

# remove_element=input("entear fruites names")
# file_name='data.json'
# user=input("enter user name")
# with open(file_name,'r')as h:
#     data=json.load(h)
#     if user in data["users"]:
#         if remove_element not in data["fruits"]:
#                 print(f"{remove_element}is not available")
#         else:
#             data["fruits"].remove(remove_element)
#             print(f"{remove_element} is removed sucessfully")
#     else:
#          print("u r not authorised to perfrom remove operaction")
# with open(file_name,'w')as f:
#     json.dump(data,f) 



# 3. adding operaction
user=input("enter user name")
file_name='data.json'
adding_element=input("enter fruit name to be add:")
with open(file_name,'r')as h:
    data=json.load(h)
    if user in data["users"]:
        if adding_element not in data["fruits"]:
                print(f"{adding_element}is already exists")
        else:
            data["fruits"].remove(adding_element)
            print(f"{adding_element} is added sucessfully")
    else:
         print("u r not authorised to perfrom adding operaction")
with open(file_name,'w')as f:
    json.dump(data,f) 


    
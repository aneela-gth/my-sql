#sholow
import copy
info={'name':'aneela','city':'hyd','age':23}
x=copy.copy(info)
x1=copy.copy(info)
x['name']='anee'
print(x)
print(x1)

import copy 
score_board={'score':{'runs':135,'wikkets':4,'overs':4.4}}
shanu=copy.copy(score_board)
aneela=copy.copy(score_board)
aneela['score']['runs']+=6
print(score_board)
print(shanu)
print(aneela)

import copy
x=[[1,2,3],[4,5],6]
shallow=copy.copy(x)


#deeppcopy
import copy
info={'detils':{'name':'tharun','city':'hyd','age':23}}
x=copy.deepcopy(info)
y=copy.deepcopy(info)
info['detils']['name']='naveen'
print(info)
print(x)
print(y)

import copy
pubg={'score':{'kill':0,'health':100}}
aneela=copy.deepcopy(pubg)
suppu=copy.deepcopy(pubg)
sharanya=copy.deepcopy(pubg)
sreevani=copy.deepcopy(pubg)
aneela['score']['kill']+=4
sreevani['score']['health']-=25
print(pubg)
print(suppu)
print(aneela)
print(sreevani)
print(sharanya)

import copy
x=[[1,2,3],[4,5],6]
shallow=copy.deepcopy(x)

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

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")

def sum_nested_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):  
            total += sum_nested_list(item)
        else:  
            total += item
    return total


nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = sum_nested_list(nested_list)
print("Sum of all numbers:", result)

def sum_nested_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):  
            total += sum_nested_list(item)
        else:  
            total += item
    return total


x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]

result = sum_nested_list(x)
print("Sum of all numbers:", result)

# list=[1,2,1,3,1,4]
# x=[]
# for i in list:
#     if i not in x:
#         x.append(i)
# print(x)
numbers = [1, 2, 1, 3, 1, 4]
unique = []

for i in range(len(numbers)):
    is_duplicate = False
    
    for j in range(i):
        if numbers[i] == numbers[j]:
            is_duplicate = True
            break
    
    if not is_duplicate:
        unique.append(numbers[i])

print(unique)



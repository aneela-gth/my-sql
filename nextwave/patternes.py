# for i in range(5):
#     for j in range(i):
#         print('*' ,end='')
#     print('*')

# for i in range(5):
#     for j in range(i):
#         print(1 ,end='')
#     print(1)

# for i in range(6):
#     for j in range(6-i):
#         print('*',end='')
#     print('*')

# for i in range(5):
#     for k in range(5-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*' ,end='')
#     print(end='\n')

#peramiead
for i in range(1,5):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for k in range(i,1,-1):  
        print("*",end=" ")
    print(" ")




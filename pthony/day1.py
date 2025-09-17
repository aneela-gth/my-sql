# for i in range(5):
#     for j in range(i):
#         print('*',end="")
#     print()

# for i in range(5):
#     for k in range(i):
#         print(' ',end=" ")
#         for j in range(1):
#             print(' *',end='')
#     print()
# row=5
# for i in range(1,row + 1):
#     print(" "  *(row - i) + '*' * (2 * i - 1))

def process(fun,x):
    result=[]
    for i in x:
        op=fun(i)
        result.append(op)
        print(result)
process(lambda x:'helow'+x,['aneela','suppu','sharnya','sreevani'])

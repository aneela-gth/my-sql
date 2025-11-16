# # 1
# x=[1,2,3]
# x.append([4,5])
# print(len(x))  #output:4

# # 2.
# a=[x+y for x in "ab" for y in "12"]
# print(a) #output:['a1', 'a2', 'b1', 'b2']

# # 3.
# t=(1,2,(3,4))
# print(t[2][1]) #output:4

# # 4
# x=[1,2,3]
# y=x
# del x
# print(y)  #output:[1, 2, 3]

# q="xyz"
# for i in q:
#     print(chr(ord(i)-32))

# n="az"
# for i in n:
#     print(ord(i)) 

# for i in range(len("xxxxxxxxx")):
#     print(i+True)



# start=ord("a")-ord("`")
# end=ord("j")-ord("`")
# for i in range(start,end+True):
#     print(i)


# start=ord("a")%ord(" ")
# end=ord("z")-1%ord(" ")
# for i in range(start,end+1):
#     print(i)

# print(ord('a'))
# print(ord('b'))
# print(ord("z89"))

# print(ord('d')

# for i in range(ord('B')-ord('A'),ord('d')+1):
#     print(i)

# x=[1,2,3,4,5]
# sum=""
# assinding=[]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             temp=x[i]
#             x[i]=x[j]
#             x[j]=temp
#             sum+=j
# print(sum)

# sum=0
# for i in range(ord("B")-ord("A"),ord("c")+1):
#     sum+=i
# print(sum)


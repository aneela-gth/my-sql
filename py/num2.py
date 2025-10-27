import numpy as np
# mat=np.array([[1,2,3,4],[5,6,7,8]])
# print(np.ndim(mat))

# reshape:
# dim1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(np.reshape(dim1,(3,4)))
# print(np.reshape(np.arrangrd)).

# flaten():
# convert to multideminctional to 1 dimaction
# arr=[1,2,3,[4,5,6,[7,8,[9,10,11,12]]]]
# print(len(arr))
# print(np.array(arr).flatten())
# arr=[[1,2,3,4,5,6,],[7,8,9,10,11,12],[13,14,15,16,17,18]]
# print(len(arr))


# concatenate
# a=np.array([1,2],[5,6])
# b=np.array([3,4],[7,8])
# print(np.concatenate((a,b)))
# arr=[1,2,3,4,500,70,80]
# np_arr=np.array(arr)
# print(np_arr)
# print(np.where(np_arr>50))
# print(np.where(np_arr%2==0))
# print([1,2,3]*2)-->scalar cal
# print(np.array([1,2,3])*2)-->vector cal
# print(np.unique([1,2,3,1,2,3,5]))

# vector
# dimension and magnitude

# matrix multiplaction
# no of row in 1st matrix=no of cols  in 2nd mateix
# print(np.dot([1,2]),[[3],[4],[5]])    

# transpose:swap the columns and rows
# rows converst columns,columns convert to rows
# print(np.transpose([[1,2],
#                     [3,4]]))

# from np.linaping.
# import random
# print(np,random.randint(6,10,5))

# import numpy as np

# array = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))
# np.rray(print([1,2,3]))


# arr1=np.array((1,2,3,4,5))
# print(arr1)

# import time
# start=time .time()
# for i in range(10000):
#     i*2
#     print("time taken",time.time()-start)
#     start=time.time()
#     num2=arr=np.arange(100000)*2
#     print("num time",time.time()-start)

# arr2=np.arange(500)
# print(arr2)
# print(np.array([1,2,3],"1d"))
# print(np.array([[1,2],[3,4]]),"2d")

# zeros:
# print(np.zeros(3))
# print(np.zeros(10))
# print(np.zeros(5,dtype=int))
# print(np.zeros([3,5],dtype=int))

# ones:
# print(np.ones(4))
# print(np.ones(4,dtype=int))
# print(np.ones([1,10],dtype=int))
# print(np.ones([1,10],dtype=bool))


# linspace:
# print(np.linspace(2,101,2))

# math&start:
# print(np.sum([1,2,3,4,5,6,7,8,9,10]))

# mean():
# list=[1,2,3,4,5]
# sum=0
# for i in list:
#     sum+=i
#     print(sum/len(list))
# print(np.mean([1,2,3,4,5,6,7,8,9,10]))

# median():
# list=[1,2,3,4,5]
# mid=len(list)/2
# print(mid)
# print(np.median([1,2,3,4,5]))


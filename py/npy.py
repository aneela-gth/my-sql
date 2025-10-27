# 📊 Array Creation Methods
# 1. np.array()
import numpy as np
# print(np.array([1,2,3]))
# np.array1([[1,2],[3,8]])
# np.array((2,4,7))


# 2. np.zeros(shape)
# arr=np.zeros(3)
# print(arr)
# np.zeros(2,2)
# np.zeros(3,1)

# 3. np.ones(shape)
# arr=np.ones(4)
# print(arr)
# arr1=np.ones((2,3))
# print(arr1)
# arr2=np.ones((1,5))
# print(arr2)

# np.arange(start, stop, step)
# arr=np.arange(5)
# print(arr)
# arr=np.arange(1,10,2)
# print(arr)
# arr=np.arange(10,0,-2)
# print(arr)

# 5. np.linspace(start, stop, num)
# arr=np.linspace(0, 1, 5)
# print(arr)
# arr1=np.linspace(1, 10, 4)
# print(arr1)
# arr2=np.linspace(5, 6, 3)
# print(arr2)

# 📈 Math & Stats Methods
# 6. np.sum()
# arr=np.sum([1,2,3])
# print(arr)
# arr1=np.sum([[1,2],[3,4]])
# print(arr1)
# arr2=np.sum([[1,2],[3,4]])
# print(arr2)

# 7. np.mean()
# op=np.mean([10, 20, 30])
# print(op)
# op1=np.mean([[1, 2], [3, 4]])
# print(op1)
# op2=np.mean(np.array([[1, 2], [3, 4]]), axis=1)
# print(op2)

# 8. np.median()
# np.median([10, 20, 30])
# np.median([10, 20, 30, 40])
# np.median([[5, 10], [15, 20]])

# 🔄 Array Operation Methods
# 9. np.reshape(shape)
# arr=np.reshape([1, 2, 3, 4], (2, 2))
# print(arr)
# arr1=np.reshape(np.arange(6), (3, 2))
# print(arr1)
# arr2=np.reshape(np.arange(12), (2, 2, 3))
# print(arr2)

# 10. np.flatten()
# arr=np.array([[1,2],[3,4]]).flatten()
# print(arr)
# arr1=np.array([[10,20],[30,40]])
# print(arr1)
# arr=np.array([[5],[6]]).flatten()
# print(arr)

# 11. np.concatenate((a, b), axis)
# a=np.array([1,2])
# b=np.array([3,4])
# op=np.concatenate((a,b))
# print(op)
# x=np.array([[1,2]])
# y=np.array([[3,4]])
# op1=np.concatenate((x,y), axis=0)
# print(op1)
# p = np.array([[1], [2]])
# q = np.array([[3], [4]])
# arr=np.concatenate((p, q), axis=1)
# print(arr)


# 🔢 Indexing and Logical Methods
# 12. np.where(condition)
# a = np.array([10, 20, 30])
# ar=np.where(a > 15)
# print(ar)
# arr=np.where(a == 20)
# print(arr)
# op=np.where(a % 10 == 0)
# print(op)




# 1.Create a 1D NumPy array with values from 1 to 10.
import numpy as np
# arr=np.arange(1,11)
# print(arr)

# # 2.Create a 2D (3x3) array with numbers from 1 to 9.
# arr=np.arange(1,10).reshape(3,3)
# print(arr)

# # 3.Access a specific element — print the value in the 2nd row and 3rd column.
# arr=np.arange(1,10).reshape(3,3)
# print(arr[1,2])

# # 4.Slice the array — get the first two rows from the 2D array.
# arr = np.arange(1, 10).reshape(3,3)
# print(arr[:2,:])

# # 5.Find the total sum of all elements in the array.
# arr=np.arange(1,10).reshape(3,3)
# print(arr.sum())

# # 6.Find basic statistics — mean, median, and standard deviation of an array.
# arr=np.arange(1,10).reshape(3,3)
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))

# # 7.Perform element-wise multiplication — multiply all elements by 2.
# arr=np.arange(1,10).reshape(3,3)
# print(arr*2)

# # 8.Filter even numbers from a 1D array.
# arr=np.arange(1,10).reshape(3,3)
# even=arr[arr%2==0]
# print(even)

# #9. Create special arrays — a matrix of zeros and a matrix of ones.
# zeros_matrix = np.zeros((3, 3))
# print("Matrix of Zeros:\n", zeros_matrix)
# ones_matrix = np.ones((3, 3))
# print("Matrix of Ones:\n", ones_matrix)

# 10.Generate random integers — create an array of 5 random numbers between 10 and 50.
random_array = np.random.randint(10, 51, 5)
print(random_array)
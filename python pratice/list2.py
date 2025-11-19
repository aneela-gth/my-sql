# 📋 Python List Practice Questions
# ✅ Easy (40 Questions)
# Create a list of 5 integers.
# list=[1,2,3,4,5]
# print(list)

# Access the 3rd element of a list.
# list=[1,2,3,4,5]
# c=list[3]
# print(c)

# Change the value at index 2.
# list=[1,2,3,4,5,6]
# list[2]=10
# print(list)

# Append an element to the list.
# list=[1,2,3,4,5]
# list.append(6)
# print(list)

# Insert an element at index 1.

# list=[1,2,3,4,5]
# list.insert(1,20)
# print(list)

# Remove an element by value.
# list=[1,2,3,4,5]
# list.remove(3)
# print(list)

# Remove an element by index.
# list=[1,2,3,4,5]
# list.pop(3)
# print(list)

# Find the length of a list.
# list=[1,2,3,4,5]
# print(len(list))

# Check if an element exists in a list.
# list=[1,2,3,4,5,6]
# if 1 in list:
#     print("element exists")
# else:
#     print("element not found")

# Loop through a list and print each item.
# list=[1,2,3,4,5]
# for i in list:
#     print(i)

# Sort a list in ascending order.
# list=[2,6,3,5,4,1]
# # list.sort()
# # print(list)
# ascending=sorted(list)
# print(ascending)

# Sort a list in descending order.
# list=[1,2,3,4,5,6]
# descending=sorted(list,reverse=True)
# print(descending)

# Reverse a list using reverse().
# list=[1,2,3,4,5]
# list.reverse()
# print(list)

# Reverse a list using slicing.
# list=[1,2,3,4,5]
# reversed=list[::-1]
# print(reversed)

# Copy a list using slicing.

# list=[1,2,3,4,5]
# copy_list=list[:]
# print(copy_list)

# Copy a list using the copy() method.

# list=[1,2,3,4,5]
# copy=list.copy()
# print(copy)

# Clear all elements in a list.

# list=[1,2,3,4,5]
# list.clear()
# print(list)

# Count occurrences of a number.
# list=[1,2,3,4,1,1]
# c=list.count(1)
# print(c)

# # Find the index of a number.
# import random
# list=[1,2,3,4,5,6,7,8]
# rade=random.choice(list)
# print(rade)

# Concatenate two lists.
# list1=[1,2,3]
# list2=[4,5]
# merged=list1+list2
# print(merged)


# Repeat a list 3 times.
# list=[1,2,3]
# rep=[]
# for i in range(3):
#     for j in list:
#         rep.append(j)
# print(rep)

# Print every second element.
# Print elements from index 2 to 5.
# Check if all elements are positive.
# Convert list to a string with commas.
# Find the max element.
# Find the min element.
# Sum all numbers in a list.
# Square every number in a list.
# Filter even numbers from a list.
# Filter odd numbers from a list.

# # Find duplicates in a list.
# list = [1, 2, 2, 3, 4, 3, 5, 2]
# duple=[]
# for i in list:
#     if list.count(i)>1 and i not in duple:
#         duple.append(i)
# print(duple)

# Remove duplicates from a list.
# list = [1, 2, 2, 3, 4, 3, 5]
# new_list=[]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# Get unique elements using set().
# list = [1, 2, 2, 3, 4, 3, 5]
# uni_set=set(list)
# print(uni_set)

# Check if a list is empty.
# my_list = []

# if not my_list:
#     print("The list is empty")
# else:
#     print("The list is not empty")

# Initialize a list of n zeros.

# n = 5
# zeros_list = [0] * n
# print(zeros_list)

# Swap two elements in a list.
a=[1,2,3]
b=[4,5,6]
a,b=b,a
print(a)
print(b)




# Get last element of a list.
# Convert a string to a list of chars.
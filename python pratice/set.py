# Set and Dictionary Interview Questions – Problem Statements and Explanations
# ________________________________________
# Set-Based Questions
# 1. Add Element to a Set
# Problem: Add an item to a given set.
# Explanation: Use add() method.
# Input: {1, 2, 3}, add 4
# Output: {1, 2, 3, 4}

# set={1, 2, 3}
# set.add(4)
# print(set)


# my_set={1, 2, 3}
# temp=list(my_set) #convert to list
# temp.append(4)
# my_set=set(temp)  #convert back to set
# print(my_set)

# _____________________________________________________________________________________________________________________________
# 2. Remove Element from Set
# Problem: Remove a specific element from a set.
# Explanation: Use remove() or discard() to avoid KeyError.
# Input: {1, 2, 3}, remove 2
# Output: {1, 3}

# set={1, 2, 3}
# set.remove(2)
# print(set)

# my_set={1, 2, 3}
# temp=list(my_set)
# temp.remove(2)
# my_set=set(temp)
# print(my_set)


# ______________________________________________________________________________________________________________________________
# 3. Union of Two Sets
# Problem: Find union of two sets.
# Explanation: Use | operator or union() method.
# Input: {1, 2}, {2, 3}
# Output: {1, 2, 3}

# seta={1, 2}
# setb={2, 3}
# union_set=set()
# for i in seta:
#     union_set.add(i)
#     for j in setb:
#         union_set.add(j)
# print(union_set)

# _______________________________________________________________________________________________________________________________
# 4. Intersection of Sets
# Problem: Find common elements in two sets.
# Explanation: Use & operator or intersection().
# Input: {1, 2}, {2, 3}
# Output: {2}

# set1={1, 2}
# set2={2, 3}
# intersection_set=set()
# for i in set1:
#   if i in set2:
#     intersection_set.add(i)
# print( intersection_set)

# _______________________________________________________________________________________________________________________________
# 5. Difference of Sets
# Problem: Elements present in first set but not in second.
# Explanation: Use - or difference() method.
# Input: {1, 2, 3}, {2, 3}
# Output: {1}

# set1={1, 2, 3}
# set2={2, 3}
# difference=set()
# for i in set1:
#     if i not in set2:
#         difference.add(i)
# print(difference)


# __________________________________________________________________________________________________________________________________
# 6. Check Subset
# Problem: Check if one set is a subset of another.
# Explanation: Use issubset() method.
# Input: {1, 2}, {1, 2, 3}
# Output: True

# set1={1, 2}
# set2={1, 2, 3}
# subset=True
# for i in set1:
#     if i  not in set2:
#         subset=False
# print(subset)


# ___________________________________________________________________________________________________________________________________
# 7. Set Length
# Problem: Find number of elements in set.
# Explanation: Use len().
# Input: {1, 2, 3}
# Output: 3

# set={1, 2, 3}
# count=0
# for i in set:
#     count+=1
# print(count)

# ________________________________________
# 8. Clear a Set
# Problem: Remove all elements from a set.
# Explanation: Use clear().
# Input: {1, 2, 3}
# Output: set()

# set={1, 2, 3}
# set.clear()
# print(set)


# set={1, 2, 3}
# for i in list(set):
#     set.remove(i)
# print(set)


# ________________________________________
# 9. Symmetric Difference
# Problem: Find elements in either set but not in both.
# Explanation: Use ^ or symmetric_difference()
# Input: {1, 2, 3}, {2, 3, 4}
# Output: {1, 4}

# set1={1, 2, 3}
# set2={2, 3, 4}
# difference=set1^set2
# print(difference)


# set1={1, 2, 3}
# set2={2, 3, 4}
# difference=set()
# for i in set1:
#     if i not in set2:
#         difference.add(i)
# for i in set2:
#     if i  not in set1:
#         difference.add(i)
# print(difference) b 


# ________________________________________
# 10. Convert List to Set
# Problem: Remove duplicates using set.
# Explanation: Use set() constructor.
# Input: [1, 2, 2, 3]
# Output: {1, 2, 3}

# list= [1, 2, 2, 3]
# set=set(list)
# print(set)

# list= [1, 2, 2, 3]
# unique=[]
# for i in list:
#     if i not in unique:
#      unique.append(i)
#      result={*unique}
# print(result)

# ________________________________________
# Dictionary-Based Questions
# 11. Create a Dictionary from Two Lists
# Problem: Combine two lists into a dictionary.
# Explanation: Use zip() function.
# Input: ["a", "b"], [1, 2]
# Output: {"a": 1, "b": 2}

# list1=["a", "b"]
# list2=[1, 2]
# dict={}
# for i in range(len(list1)):
#     dict[list1[i]]=list2[i]
# print(dict)



# ________________________________________
# 12. Update Dictionary Value
# Problem: Change value for a specific key.
# Explanation: Use assignment dict[key] = value.
# Input: {"a": 1}, update a to 2
# Output: {"a": 2}

# dict={"a": 1}
# dict["a"]=2
# print(dict)


# ________________________________________
# 13. Remove Key from Dictionary
# Problem: Delete a key-value pair.
# Explanation: Use del or pop() method.
# Input: {"a": 1, "b": 2}, remove b
# Output: {"a": 1}

# d={"a": 1, "b": 2}
# del d["b"]
# print(d)

# ________________________________________
# 14. Check Key Existence
# Problem: Verify if a key exists.
# Explanation: Use in operator.
# Input: {"x": 1}, key = "x"
# Output: True

# d1={"x": 1}
# if 'x' in d1: 
#    print(True)

# d1={"x":1}
# if d1.get("x")is not None:
#     print(True)

# ________________________________________
# 15. Iterate Over Dictionary
# Problem: Print all keys and values.
# Explanation: Use .items() in loop.
# Input: {"a": 10, "b": 20}
# Output: a 10, b 20

# s={"a": 10, "b": 20}
# for key,value in s.items():
#  print(key,value)

# ________________________________________
# 16. Dictionary Length
# Problem: Count total key-value pairs.
# Explanation: Use len() function.
# Input: {"x": 1, "y": 2}
# Output: 2

# d={"x": 1, "y": 2}
# print(len(d))

# ________________________________________
# 17. Merge Two Dictionaries
# Problem: Combine two dictionaries.
# Explanation: Use unpacking or update().
# Input: {"a": 1}, {"b": 2}
# Output: {"a": 1, "b": 2}

# d1={"a": 1}
# d2={"b": 2}
# s={}
# s=d1.copy()
# s.update(d2)
# print(s)

# d1={"a": 1}
# d2={"b": 2}
# s={**d1,**d2}
# print(s)

# ________________________________________
# 18. Get Value with Default
# Problem: Get value or default if key not found.
# Explanation: Use get() method.
# Input: {"a": 1}, get "b" with default 0
# Output: 0


# ________________________________________
# 19. Count Frequency of Elements
# Problem: Count frequency using dictionary.
# Input: [1, 2, 2, 3]
# Output: {1: 1, 2: 2, 3: 1}
# ________________________________________
# 20. Invert a Dictionary
# Problem: Flip keys and values.
# Input: {"a": 1, "b": 2}
# Output: {1: "a", 2: "b"}
# ________________________________________
# 21. Find Key with Maximum Value
# Problem: Identify the key with the highest value.
# Input: {"a": 10, "b": 20, "c": 15}
# Output: "b"
# ________________________________________
# 22. Sort Dictionary by Values
# Problem: Sort a dictionary based on its values.
# Input: {"a": 3, "b": 1, "c": 2}
# Output: [('b', 1), ('c', 2), ('a', 3)]
# ________________________________________
# 23. Create Dictionary of Squares
# Problem: Create dictionary where keys are numbers and values are their squares.
# Input: range(1, 4)
# Output: {1: 1, 2: 4, 3: 9}
# ________________________________________
# 24. Filter Dictionary by Value Condition
# Problem: Retain only items with value greater than a threshold.
# Input: {"a": 10, "b": 5, "c": 15}, condition: > 10
# Output: {"c": 15}
# ________________________________________
# 25. Combine Values of Duplicate Keys
# Problem: Given two dictionaries, add values of common keys.
# Input: {"a": 1, "b": 2}, {"a": 3, "c": 4}
# Output: {"a": 4, "b": 2, "c": 4}
# ________________________________________
# 26. Count Word Frequency in Sentence
# Problem: Count occurrences of each word in a string.
# Input: "apple banana apple"
# Output: {"apple": 2, "banana": 1}
# ________________________________________
# 27. Remove Duplicate Values from Dictionary
# Problem: Remove duplicate values keeping first key only.
# Input: {"a": 1, "b": 2, "c": 1}
# Output: {"a": 1, "b": 2}


# d={"a": 1, "b": 2, "c": 1}
# seen_values=[]
# result={}
# for key ,value in d.items():
#     if value not in seen_values:
#         result[key]=value
#         seen_values.append(value)
# print(result)

# ________________________________________
# 28. Find Common Keys in Two Dictionaries
# Problem: Return keys common to both dictionaries.
# Input: {"a": 1, "b": 2}, {"b": 3, "c": 4}
# Output: ["b"]

# d1={"a": 1, "b": 2}
# d2={"b": 3, "c": 4}
# common_key=list(d1.keys()&d2.keys())
# print(common_key)

# ________________________________________
# 29. Swap Keys and Values Safely
# Problem: Flip keys and values ensuring all values are unique.
# Input: {"x": 1, "y": 2}
# Output: {1: "x", 2: "y"}

# d={"x": 1, "y": 2}
# swapped={value:key for key,value in d.items()}
# print(swapped)

# ____________________________________________________
# 30. Delete Items by Value
# Problem: Remove key-value pairs with specific value.
# Input: {"a": 1, "b": 2, "c": 1}, value: 1
# Output: {"b": 2}

# d={"a": 1, "b": 2, "c": 1}
# value_to_remove=1
# filtered_dict={k:v for k,v in d.items() if v!=value_to_remove}
# print(filtered_dict)

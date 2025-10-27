# Easy (40 Questions)
# 1.Create a list of 5 integers.
# list=[1,2,3,4,5]
# print(list)

# 2.Access the 3rd element of a list.
# list=["aneela","akhila",'naveen',"naresh"]
# print(list[2])

# 3.Change the value at index 2.
# list=["aneela","akhila",'naveen',"naresh"]
# list[1]="akhi"
# print(list)

# 4.Append an element to the list.
# ist=["aneela","akhila",'naveen',"naresh"] 
# list.append("ram")
# print(list)

# 5.Insert an element at index 1.
# list=["aneela","akhila",'naveen',"naresh"]
# list.insert(1,20)
# print(list)

# 6. Remove an element by value.
# list=["aneela","akhila",'naveen',"naresh"]
# list.pop(1)
# print(list)

# 7. Remove an element by index.
# list=["aneela","akhila",'naveen',"naresh"]
# list.pop(1)
# print(list)

# 8.Find the length of a list.
# list=["aneela","akhila",'naveen',"naresh"]
# print(len(list))

# 9.Check if an element exists in a list.
# fruites=["apple","banana","pineaple","oreange"]
# if "pineaple" in fruites:
#     print("pineaple in the fruites")
# else:
#     print("pineaple is not in the fruites")

# # 10.Loop through a list and print each item.
# list=[1,2,3,4,5,6,7,8,9]
# for list in  list:
#     print(list)

# # 11.Sort a list in ascending order.
# list=[2,5,7,3,9,7,6,1,4,8]
# list.sort()
# print(list)

# 12.Sort a list in descending order.
# list=[1,2,3,4,5,6,7,8,9]
# list.sort(reverse=True)
# print(list)

# 13.Reverse a list using reverse().
# list=[1,2,3,4,5,6,7,8,9]
# list.reverse()
# print(list)
# list=["aneela","akhila","naveen","naresh"]
# list.reverse()
# print(list)

# 14.Reverse a list using slicing.
# list=["aneela","akhila","naveen","naresh"]
# reversed_list=list[::-1]
# print(reversed_list)

# 15. Copy a list using slicing.
# list=["aneela","akhila","naveen","naresh"]
# copied_list = list[:]
# print("Original list:", list)
# print("Copied list:", copied_list)

# 16.Copy a list using the copy() method.
# list=["aneela","akhila","naresh","naveen"]
# copy_inst=list[:]
# print("copy_list:",list)

# 17.Clear all elements in a list.
# list=["aneela","naresh","naveen","akhila"]
# list.clear()
# print(list)

# 18.Count occurrences of a number.
# list=[1,5,3,4,5,6,7,8,5]
# print(list.count(5))

# 19.Find the index of a number.
# list=[1,5,3,4,5,6,7,8,5]
# print(list.index(5))

# 20.Concatenate two lists.
# list1=[1,2,3,4]
# list2=[5,6,7]
# concatenate=list1+list2
# print(concatenate)

# 21. Repeat a list 3 times.
# list=[1,2,3]
# new_list=list*3
# print(new_list)
# list=[1,2,3,4]
# op=list*4
# print(op)

# 22. Print every second element.
# list=[1,2,3,4,5,6,7,8,9,10]
# print(list[1::2])

# 23. Print elements from index 2 to 5.
# list=[1,2,3,8,4,5,6,7,]
# print(list[2:5])

# 24. Check if all elements are positive.
# numbers=[1,2,3,4,5,6,7,8]
# all_positive=all(num>0 for num in numbers)
# print("all_positive")

# 25.Convert list to a string with commas.
# list=[1,2,3,4,5]
# op=",".join(map(str,list))
# print(op)
# list=["apple","banana","pineaple"]
# op=",".join(list)
# print(op)

# 26.Find the max element.
# list=[1,2,4,3,1,2,4,5,2,4]
# op=max(list)
# print(op)

# 27. Find the min element.
# list=[1,2,3,4,1,3,1,34,2,2,2]
# op=min(list)
# print(op)

# 28. Sum all numbers in a list.
# list=[1,2,3,4,5]
# toteal=sum(list)
# print(toteal)

# 29.Square every number in a list.
# list=[1,2,3,4,5]
# sqr=[num**2 for num in list]
# print(sqr)

# 30.Filter even numbers from a list.
# list=[1,2,3,4,5]
# even=[num for num in list if num%2==0]
# print(even)

# 31.Filter odd numbers from a list.
# list=[1,2,3,4,5]
# odd=[num for num in list if num%2!=0]
# print(odd)

# 32.Find duplicates in a list.
# list=[1,2,1,4,1,6,1,8,1,10]
# duplicates=[num for num in set(list) if list.count(num)>1]
# print(duplicates)

# 33.Remove duplicates from a list.
# num=[1,2,1,6,4,5,1,6,1]
# remove_duplicates=list(set(num))
# print("list without duplicates:",remove_duplicates)

# 34.Get unique elements using set().
# num=[1,2,3,2,4,1,5]
# unique_elements=set(num)
# print("uniqe_element",unique_elements)

# 35.Check if a list is empty.
# list=[]
# if not list:
#     print("the list is empty")
# else:
#     print("the list is not empty")

# 36.Initialize a list of n zeros.
# n=5
# zero_list=[0]*n
# print("list of zero:",zero_list)

# 37.Swap two elements in a list.
# list=[12,13,14,15]
# list[1],list[3]=list[3],list[1]
# print("list after swap:",list)

# 38.Get last element of a list.
# numbers = [5, 10, 15, 20]
# last_element = numbers[-1]
# print("Last element:", last_element)

# 39.Convert a string to a list of chars.
# text = "Hello"
# chars = list(text)
# print("List of characters:", chars)


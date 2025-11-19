# List-Based Interview Questions – Logic & Practice
# ________________________________________
# 1. Add an Element to a List
# Problem: Write a function to add an element to a list. Explanation: Use append() to add the element to the end. Input: [1, 2, 3], add 4 Output: [1, 2, 3, 4]
# num=[1,2,3]
# num.append(4)
# print(num)

# lt=[1,2,3,4]
# new_element=5
# lt=lt+[new_element]
# print(lt)

# lst=[1,2,3]
# val=4
# new_lst=[]
# for i in lst:
#     new_lst+=[i]
# new_lst+=[val]
# print(new_lst)


# --------------------------------------------------------------------------------------
# 2. Remove an Element from a List
# Problem: Write a function to remove a specific element from a list. Explanation: Use remove() or pop() if index is known. Input: [1, 2, 3, 4], remove 3 Output: [1, 2, 4]
# lt=[1,2,3,4,5]
# remove_element=5
# lt.remove(remove_element)
# print(lt)

# lst=[1,2,3,4]
# val=3
# new_list=[]
# for i in lst:
#     if i!=val:
#         new_list+=[i]
# print(new_list)





# ------------------------------------------------------------------------------------------------
# 3. Find Maximum in List
# Problem: Find the maximum value in a list. Explanation: Use max() or iterate manually. Input: [4, 7, 1, 9] Output: 9
# s=[4, 7, 1, 9]
# p=max(s)
# print(p)
# s=[4, 7, 1, 9]
# max=s[0]
# for i in s:
#     if i >max:
#         max=i
# print(max)

# lst=[5,3,4,7]
# max_val=lst[0]
# for i in lst:
#     if i>max_val:
#         max_val=i
# print(max_val)





# 4. Find Minimum in List
# Problem: Find the minimum value in a list. Explanation: Use min() or iterate manually. Input: [4, 7, 1, 9] Output: 1
# t=[4, 7, 1, 9]
# m=min(t)
# print(m)

# s=[4, 7, 1, 9]
# min=s[0]
# for i in s:
#     if i<min:
#         min=i
# print(min)



# s= [4, 7, 1, 9]
# min_val=s[0]
# for i in s:
#     if i<min_val:
#         min_val=i
# print(min_val)


# 5. Sum of All Elements in List
# Problem: Write a function to find the sum of all list elements. Explanation: Use sum() or loop to add all items. Input: [1, 2, 3] Output: 6
# c=[1, 2, 3]
# sum=0
# for i in c:
#         sum+=i
# print(sum)

# 6. Count Occurrence of an Element
# Problem: Count how many times a value appears in a list. Explanation: Use count() method. Input: [1, 2, 2, 3, 2], value 2 Output: 3
# a=[1, 2, 2, 3, 2]
# value=2
# count=0
# for i in a:
#     if i==value:
#       count+=1
# print(count)


# 7. Reverse a List
# Problem: Write a function to reverse the order of list elements. Explanation: Use slicing or reverse() method. Input: [1, 2, 3] Output: [3, 2, 1]
# a=[1, 2, 3]
# rev=[]
# for i in a:
#     rev=[i]+rev
# print(rev)


# a=[1, 2, 3]
# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev+=[a[i]]
# print(rev)


# 8. Sort a List
# Problem: Write a function to sort a list in ascending order. Explanation: Use sort() or sorted(). Input: [4, 1, 3, 2] Output: [1, 2, 3, 4]
# v=[4, 1, 3, 2]
# ascending=[]
# for i in range(len(v)):
#     for j in range(i+1,len(v)):
#         if v[i]>v[j]:
#             temp=v[i]
#             v[i]=v[j]
#             v[j]=temp
# print(v)







# 9. Remove Duplicates from a List
# Problem: Eliminate duplicate values. Explanation: Use set() or manual loop. Input: [1, 2, 2, 3] Output: [1, 2, 3]
# c=[1, 2, 2, 3]
# dupli=[]
# for i in range(len(c)):
#     present=False
# for j in range(len(dupli)):
#     if c[i]==dupli[j]:
#         present=True
#         break
#     if not present:
#         dupli+=[c[i]]
# print(dupli)

# 10. Merge Two Lists
# Problem: Merge two lists into one. Explanation: Use + operator or extend(). Input: [1, 2], [3, 4] Output: [1, 2, 3, 4]
# c=[1,2]
# d=[3,4]
# e=c+d
# print(e)

# c=[1,2]
# d=[3,4]
# merged=[]
# for i in range(len(c)):
#     merged+=[c[i]]
# for j in range(len(d)):
#     merged+=[d[j]]
# print(merged)

# c=[1,2]
# d=[3,4]
# merged=[]
# for i in c:
#     merged+=[i]
# for i in d:
#     merged+=[i]
# print(merged)




# 11. Find Common Elements in Two Lists
# Problem: Return common elements between two lists. Explanation: Use set() and & or loops. Input: [1, 2, 3], [2, 3, 4] Output: [2, 3]

# x=([1, 2, 3],[2, 3, 4])
# a=x[0]
# b=x[1]
# coman=[]
# for i in a:
#     if i in b:
#         coman+=[i]
# print(coman)


# 12. Print Even Numbers in a List
# Problem: Print only even numbers from a list. Explanation: Use modulo condition in a loop. Input: [1, 2, 3, 4] Output: [2, 4]

# x=[1, 2, 3, 4]
# even=[]
# for i in x:
#     if i%2==0:
#         even+=[i]
# print(even)

    
# 13. Print Odd Numbers in a List
# Problem: Print only odd numbers from a list. Input: [1, 2, 3, 4] Output: [1, 3]

# c=[1, 2, 3, 4]
# odd=[]
# for i in c:
#     if i%2!=0:
#         odd+=[i]
# print(odd)

# 14. Check if List is Palindrome
# Problem: Check if the list reads the same forwards and backwards. Input: [1, 2, 1] Output: True

# lst=[1,2,1]
# rev_list=[]
# for i in range(len(lst)-1,-1,-1):
#     rev_list+=[lst[i]]
# if rev_list==lst:
#     print("palindrom")
# else:
#     print("not a palindrom")


# 15. Count Positive, Negative, Zero
# Problem: Count the number of positive, negative and zero values in a list. Input: [0, -1, 2, -3, 4] Output: Positive: 2, Negative: 2, Zero: 1

# list=[0, -1, 2, -3, 4]
# positive=0
# negative=0
# zero=0
# for i in list:
#     if i<0:
#         negative+=1
#     elif i>0:
#         positive+=1
#     else:
#         zero+=1
# print(positive)
# print(negative)
# print(zero)

# 16. Find Second Largest Number in List
# Problem: Find the second highest value. Input: [1, 3, 4, 5, 0] Output: 4

# list=[1, 3, 4, 5, 0]
# largest=float("-inf")
# sec_large=float("-inf")
# for i in list:
#     if i>sec_large:
#         sec_large=largest
#         largest=i
#     elif i>sec_large and i!=largest:
#         sec_large=i
# print(sec_large)


# 17. Find Second Smallest Number in List
# Problem: Find the second lowest value. Input: [5, 1, 4, 2, 3] Output: 2


# list=[1, 3, 4, 5, 0]
# smallest=float("inf")
# sec_smallest=float("inf")
# for i in list:
#     if i<smallest:
#         sec_smallest=smallest
#         smallest=i
#     elif i<sec_smallest and i!=smallest:
#         sec_smallest=i
# print(sec_smallest)


# 18. Copy List to Another List
# Problem: Copy the contents of one list to another. Explanation: Use slicing or copy(). Input: [1, 2, 3] Output: [1, 2, 3]

# list=[1, 2, 3]
# copy_list=[]
# for i in list:
#     copy_list.append(i)
# print(copy_list)


# list1=[1, 2, 3]
# copy_list=list1.copy()
# print(copy_list)


# 19. Print All Prime Numbers in List
# Problem: Print all prime numbers from a list. Input: [1, 2, 3, 4, 5] Output: [2, 3, 5]

# x=[1, 2, 3, 4, 5] 
# prime=[]
# if x>1:
#  for i in x:
#     if x%i==0:
#         print("not prime")
#     else:
#         print("it is prime")
# else:
#     print("invalid input")
    

# 20. Replace All Zeroes with a Given Number
# Problem: Replace every zero with a specific value (e.g., -1). Input: [0, 2, 0, 4], replace with -1 Output: [-1, 2, -1, 4]


# 21. Check if All Elements Are Same
# Problem: Check whether all elements in the list are identical. Input: [5, 5, 5, 5] Output: True


# 22. Find Frequency of All Elements
# Problem: Return a dictionary with the frequency of each element. Input: [1, 2, 2, 3, 1] Output: {1: 2, 2: 2, 3: 1}

# lst=[1, 2, 2, 3, 1]
# dict_count={}
# for i in lst:
#     if i not in dict_count:
#         dict_count[i]=i
#     else:
#         dict_count[i]+=i
# print(dict_count)


# 23. Flatten a Nested List
# Problem: Convert a nested list into a single list. Input: [[1, 2], [3, 4]] Output: [1, 2, 3, 4]

# lst= [[1, 2], [3, 4]]
# new_lst=[]
# for i in lst:
#     for j in i:
#         new_lst+=[j]
# print(new_lst)



# 24. Split a List into Even and Odd Lists
# Problem: Separate even and odd numbers into different lists. Input: [1, 2, 3, 4, 5] Output: Even: [2, 4], Odd: [1, 3, 5]
# list=[1, 2, 3, 4, 5]
# even=[]
# odd=[]
# for i in list:
#     if i%2==0:
#         even+=[i]
#     else:
#         odd+=[i]
# print(even)
# print(odd)

# 25. Find Pair of Elements with Given Sum
# Problem: Find all pairs in the list whose sum equals a given value. Input: [1, 2, 3, 4], sum = 5 Output: [(1, 4), (2, 3)]



# 26. Remove All Odd Numbers
# Problem: Remove all odd numbers from the list. Input: [1, 2, 3, 4, 5] Output: [2, 4]
# list=[1, 2, 3, 4, 5]
# even_list=[]
# for i in list:
#     if i%2==0:
#       even_list+=[i]
# print(even_list)


# 27. Remove All Even Numbers
# Problem: Remove all even numbers from the list. Input: [1, 2, 3, 4, 5] Output: [1, 3, 5]
# list=[1, 2, 3, 4, 5]
# odd_list=[]
# for i in list:
#     if i%2!=0:
#         odd_list+=[i]
# print(odd_list)


# 28. Multiply All Elements by a Number
# Problem: Multiply every element in the list by a fixed number. Input: [1, 2, 3], multiply by 2 Output: [2, 4, 6]

# list=[1, 2, 3]
# multiple_list=[]
# num=2
# for i in list:
#     if list*i:
#         multiple_list+=[i*num]
# print(multiple_list)


# 29. Find Difference Between Max and Min
# Problem: Return the difference between the largest and smallest element. Input: [4, 2, 7, 1] Output: 6


# 30. Check if a List is Empty
# Problem: Write a function that returns True if the list is empty, else False. Input: [] Output: True

# list=[]
# if not list:
#     print(True)
# else:
#     print(False)


# 31. Insert Element at Specific Index
# Problem: Insert a value at a specific position. Input: [1, 2, 4], insert 3 at index 2 Output: [1, 2, 3, 4]

# list= [1, 2, 4]
# list.insert(2,3)
# print(list)

# with out using bultin method
# list= [1, 2, 4]
# index=2
# value=3
# new_list=[]
# for i in range(len(list)):
#     if i==index:
#         new_list+=[value]
#     new_list+=[list[i]]
# print(new_list)



# 32. Remove All Instances of a Value
# Problem: Remove all occurrences of a specific value. Input: [1, 2, 2, 3], remove 2 Output: [1, 3]

# list=[1, 2, 2, 3]
# duple=[]
# for i in list:
#     if i!=2:
#         duple.append(i)
# print(duple)

# 33. Get Index of an Element
# Problem: Return the index of a given value. Input: [10, 20, 30], find index of 20 Output: 1

# list=[10, 20, 30]
# value=20
# for i in range(len(list)):
#     if list[i]==value:
#         print(i)


# 34. Square All Elements in a List
# Problem: Return a list with each element squared. Input: [1, 2, 3] Output: [1, 4, 9]\

# list=[1, 2, 3]
# sqr=[]
# for i in list:
#      sqr.append(i**2)
# print(sqr)

# 35. Filter Out Negative Numbers
# Problem: Remove all negative values from the list. Input: [-1, 2, -3, 4] Output: [2, 4]
# list= [-1, 2, -3, 4] 
# positive=[]
# for i in list:
#     if i>0:
#       positive.append(i)
# print(positive)


# 36. Get Elements Greater Than a Value
# Problem: Return elements greater than a specified number. Input: [1, 5, 8, 3], greater than 4 Output: [5, 8]

# list=[1, 5, 8, 3]
# greater=[]
# for i in range(len(list)):
#     if list[i]>4:
#         greater+=[list[i]]
# print(greater)


# 37. Find Duplicates in List
# Problem: Return a list of duplicated values. Input: [1, 2, 2, 3, 3, 4] Output: [2, 3]

# list=[1, 2, 2, 3, 3, 4]
# duple=[]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]==list[j]:
#             if list[i] not in duple:
#                 duple+=[list[i]]
# print(duple)


# 38. Rotate List Elements Right
# Problem: Rotate list by k positions to the right. Input: [1, 2, 3, 4], k = 2 Output: [3, 4, 1, 2]





# 39. Check If List Contains a Value
# Problem: Return True if list contains a specific value. Input: [1, 2, 3], check 2 Output: True

# list=[1, 2, 3]
# value=2
# if value in list:
#     print(True)
# else:
#     print(False)


# 40. Chunk List into Smaller Lists
# Problem: Break a list into chunks of given size. Input: [1, 2, 3, 4, 5, 6], chunk size 2 Output: [[1, 2], [3, 4], [5, 6]]

# list1=[1,2,3,4,5]
# list2=[6,7,8]
# merged=[]
# merged=list1+list2
# print(merged)
# import random
# list=[1,2,3,4,5,6,2,3,2,3,2]
# li=random.randint(1,10)
# print(list[4])
# list=[1,2,3,4]
# print(list[0],list[3])
# list.append(5)
# print(list)
# list.insert(1,20)
# print(list)
# list.remove(2)
# list.pop(1)
# list.reverse()

# print(4 in list)
# print(len(list))
# list.count(2)
# list.index(3)
# print(list)



# a="1.2.3.4"
# b=""
# for i in a:
#   if i==".":
#     b+="*"
#   else:
#     b+=i
# print(b)
  


list=[1,2,3,4,5]
max_value=[]
for i in list:
    max_value+=
   
      
# # Interview Questions – Logic-Based Programs

# # 🔢 Prime and Armstrong Logic Questions
# # 1. Print All Prime Numbers from m to n
# # Problem: Given a range from m to n, print all prime numbers in that range.
# # Input: m = 10, n = 30
# # Output: 11 13 17 19 23 29
# # Explanation: A prime number has only two factors: 1 and itself.
# m=10
# n=30
# count=0
# for i in range(10,30):
#     if i>1:
#         for j in range(2,int(i**0.5)):
#           if i%j==0:
#              count+=1
#              break
#           else:
#              print(i)

# m=1
# n=20
# count=0
# for i in range(m,n+1):
#     is_prime=True
#     if i<2:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
           
#             break  
#         if is_prime==True:
#             count+=1
#             print(count)


# 2. Count of All Prime Numbers from m to n
# Problem: Count how many prime numbers are there between m and n.
# Input: m = 1, n = 10
# Output: 4
# Explanation: Prime numbers are: 2, 3, 5, 7
# n=10
# m=1
# n=10
# count=0
# for i in range(1,10):
#     if i>1:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 break
#             else:
#                 count+=1
# print(count)


# 3. Print All Armstrong Numbers in a Range
# Problem: Print all Armstrong numbers between m and n.
# Input: m = 1, n = 500
# Output: 1 153 370 371 407
# Explanation: Armstrong number = sum of each digit raised to the power of number of digits.

# m=1
# n=500
# for i in range(1,n+1):
#  digits=str(i)
#  power=len(digits)
#  sum_of_powers=sum(int(digits)**power for digits in digits)
#  if i==sum_of_powers:
#   print(i,end=" ")


# m=1
# n=500
# for i in range(m,n+1):
#     temp=i
#     count=0
#     while temp!=0:
#         count+=1
#         temp//=10
#     dummy=i
#     sum=0
#     count1=0
#     while dummy!=0:
#         rem=dummy%10
#         sum+=rem**count
#         dummy//=10
#     if sum==i:
#         print(i)



# 4. First Prime Number from m to n
# Problem: Find the first prime number in the given range.
# Input: m = 10, n = 25
# Output: 11
# m=10
# n=25
# first_prime=None
# for num in range(m,n+1):
#     if num>1:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 break
#             else:
#                 first_prime=num
#                 break
# if first_prime:
#     print("first_prime:",first_prime)
# else:
#     print("no first number")
# 4. First Prime Number from m to n
# Problem: Find the first prime number in the given range.
# Input: m = 10, n = 25
# Output: 11

# m = 10
# n = 25
# first_prime = None

# for num in range(m, n + 1):
#     if num > 1:
#         for i in range(2,int(num ** 0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             first_prime = num
#             break  # Stop after finding the first prime

# if first_prime:
#     print("First prime:", first_prime)
# else:
#     print("No prime number found in the range")




# 5. Last Prime Number from m to n
# Problem: Find the last prime number in the given range.
# Input: m = 10, n = 25
# Output: 23
# m=10
# n=25
# last_prim=None
# for num in range(m,n):
#     if num>1:
#         for i in range(2,int(num**0.5)+1):
#           if num%i==0:
#              break
#           else:
#              last_prim=num
# if last_prim:
#    print("last prime number:",last_prim)
# else:
#    print("no prime number found in the range")



# 6. First Vowel in a Name
# Problem: Given a string, find the first vowel in the string.
# Input: name = "Krishna"
# Output: i
# Explanation: First vowel from left is ‘i’

# name="krishna"
# vowles="aeiou"
# for i in name:
#     if i in vowles:
#         print(i)
#         break

# 7. Last Vowel in a Name
# Problem: Given a string, find the last vowel in the string.
# Input: name = "Ramakrishna"
# Output: a
# Explanation: Last vowel is ‘a’
# name="rmkrishna"
# vowles="aeiou"
# for i in name:
#     if i in vowles:
#         last_vowles=i
# if last_vowles:
#         print("last_vowles:",last_vowles)
# else:
#      print("no vowles found")
        
        

# 8. Print All Even Numbers Using Continue
# Problem: Use continue statement to skip odd numbers and print only even numbers between 1 and n.
# Input: n = 10
# Output: 2 4 6 8 10
# n=10
# for i in range(1,11):
#     if i%2!=0:
#         continue
#     print(i)


# 9. Print All Odd Numbers Using Continue
# Problem: Use continue statement to skip even numbers and print only odd numbers.
# Input: n = 10
# Output: 1 3 5 7 9
# n=10
# for i in range(1,10):
#     if i%2==0:
#         continue
#     print(i)

# 10. Count of Prime and Composite Numbers from m to n
# Problem: Count how many are prime and how many are composite numbers in range m to n.
# Input: m = 1, n = 10
# Output: Prime: 4, Composite: 4
# Explanation: Prime: 2,3,5,7 | Composite: 4,6,8,9
# m=1
# n=10
# p_count=0
# c_count=0
# for num in range(m,n+1):
#     if num>1:
#         for j in range(2,int(num**0.5)+1):
#             if (num%j==0):
#                 c_count+=1
#                 break
#             else:
#                 p_count+=1
# print("prime:",p_count,"composite:",c_count)



n=1
m=10
c_count=0
p_count=0
for i in range(n,m+1):
        count=0
    # if i>1:
        for j in range(1,i+1):
            if i%j==0:
              count+=1
        if count==2:
              print("prime:",i)
        elif count>2:
              print("composite :",i)
              
   























# amstronge number:
# m=1
# n=500
# for i in range(m,n+1):
#     temp=i
#     count=0
#     while temp!=0:
#         count+=1
#         temp//=10
#     dummy=i
#     sum=0
#     count1=0
#     while dummy!=0:
#         rem=dummy%10
#         sum+=rem**count
#         dummy//=10
#     if sum==i:
#         print(i)

# m=1
# n=20
# first_prime=None
# for i in range(m,n+1):
#     is_prime=True
#     if i<2:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break  
#         if is_prime==True:
#             first_prime=i
#             break
# print(first_prime)


# m=1
# n=20
# last_prime=None
# for i in range(m,n+1):
#     is_prime=True
#     if i<2:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break  
#         if is_prime==True:
#             last_prime=i
# print(last_prime)



# name="aneela"
# vowles="aeiou"
# fist_vowles=" "
# for i in name:
#     for name in vowles:
#        if i in vowles:
#         fist_vowles=name
#         break
#     else:
#         break
#     print(fist_vowles)
    


# name="aneela"
# vowles="aeiouAEIOU"
# first_oveal=" "
# for i in name:
#     is_v=True
#     if i<name:
#         continue
#     for j in name:
#         if i in j:
#             vowles=False
#             break  
#         if vowles==True:
#             first_oveal=i
# print(first_oveal)

# name="aneela"
# vowles="aeiou"
# first_vowle=""
# for i in name:
#     if i in vowles:
#         break
#     else:
#         break
#     print(first_vowle)

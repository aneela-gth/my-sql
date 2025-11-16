# 1. Check Even or Odd
# # Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number
# x=int(input("entear a number"))
# if(x%2==0):
#     print("it is even")
# else:
#     print("it is odd")

# 2.Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy
# y=int(input("entear a numbear"))
# if(y%5==0 and y%10!=0):
#    print("the number is divisible by 5 but not divisibel by10")
# else:
#    print("the number is not divisible by 5 but divisible by 10")

# 3.Biggest Among Two Numbers
# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# if(a>b):
#     print("a is biggest number")
# else:
#     print("b is biggest number")

# 4.Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# if(a<b):
#     print("a is smallest number")
# else:
#     print("b is smallest number")

# 5.Divisible by 2, 3, and 6
# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy
# a=int(input("enter a number :"))
# if(a%2==0 and a%3==0 and a%6==0):
#     print("the number divisible by both 2,3 also 6")
# else:
#     print("the number not divisible by both 2,3 also 6")

# 6.Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote
# age=int(input("entear age:"))
# if(age>=18):
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# 7.Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail
# m=int(input("enter markes"))
# p=int(input("enter markes"))
# c=int(input("enter markes"))
# if(m>=35 and p>=35 and c>=35):
#     print("pass subjects")
# else:
#     print("faile subjects")

# 8.Student Pass if Passed Any One Subject (>= 35)
# Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass
# m=int(input("enter markes"))
# p=int(input("enter markes"))
# c=int(input("enter markes"))
# if(m>=35 or p>=35 or c>=35 ):
#     print("pass all subjects")
# else:
#     print("fail all subjects")

# 9.Student Pass if Passed Any Two Subjects
# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass
# m=int(input("enter markes"))
# p=int(input("enter markes"))
# c=int(input("enter markes"))
# if(m>=35 or p>=35 or c>=35):
#     print("pass subjects")
# else:
#     print("fail subjects")

# 10.Biggest Among Three Numbers
# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if(a > b and a > c):
#     print("a is biggest number")
# elif(b > c):
#     print("b is biggest number")
# else:
#     print("c is biggest number")

# 11.Smallest Among Three Numbers
# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if(a < b and a < c):
#     print("a is smallest number")
# elif(b < c):
#     print("b is smallest number")
# else:
#     print("c is smallest number")

# 12. Perfect Square or Not
# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square
# number=int(input("enter a number"))
# sqrt=int(number**0.5)
# if(sqrt*sqrt==number):
#     print("a number is a perfect square")
# else:
#     print("a number is not a perfect square")

# 13.Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4
# members=17
# members_per_car=5
# cars_required=members//members_per_car
# if members%members_per_car!=0:                                        
#     cars_required+=1
#         #     print(cars_required)

# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18
# a=int(input("entear a number :"))
# b=int(input("enter a number :"))
# c=int(input("enter a number :"))
# if (a>b and a<c) or (a>c and a<b):
#     print(f"the second biggest number is {a}")
# elif(b>a and b<c) or (b<a and b>c):
#     print(f"the secong biggest number is {b}")
# else:
#     print(f"the second biggest number is {c}") 

# 15.Leap Year or Not
# Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
# year=int(input("entera year"))
# if(year%4==0 and year%100 !=0) or (year%400==0):
#     print("it is leep year")
# else:
#     print("not leep year")

# # second method:    
# year=2028
# leap=False
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             leap=True
#         else:
#             leap=False
#     else:
#         leap=True
# else:
#     leap=False
# if leap:
#     print("leap year")
# else:
#     print("not leap year")

# num=123
# sum=0
# while num>0:
#     rem=num%10
#     sum+=rem
#     num=num//10
# print(sum)

# members=17
# car_members=5
# # car_req=members//car_members
# # if members%car_req!=0:
# #     car_req+=1
# #     print(car_req)

# n=4
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     for m in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     for m in range(i):
#         print("*",end=" ")
#     print()


# perimied       
# n=4
# for i in range(1,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# n=4
# for i in range(n,0,-1):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     s=" "
#     for j in range(1,n+1):
#         s+=str(j)+" "
#     print(s)
    

# n=5
# for i in range(1,n+1):
#     s=" "
#     for j in range(1,n+1):
#         s+=str(i)+""
#     print(s)

# r=5
# for i in range(1,r+1):
#     str=" "
#     for j in range(r,r+1):
#         if i==1 or i==r or j==1 or j==r:
#             str+="*"+" "
#         else:
#             str+=" "+" "
#         print(str)


# r=5
# for i in range(r):
#     str=" "
#     for j in range(r):
#         if j==0 or j==r-1 or i==j or j==r-1 or i==j:
#             str+="*"+" "
#         else:
#             str+=" "+" "
#         print(str)

num=123
len=0
while num>0:
    rem=num%10
    len+=rem
    num=num//num
print(len)


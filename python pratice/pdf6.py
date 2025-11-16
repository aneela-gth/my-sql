# # 1. Add Two Numbers Using Function
# # Problem: Write a function that takes two numbers as arguments and returns their sum.
# # Explanation: The function should accept two inputs and return the result of their addition.

# def add(a,b):
#     print(a+b)
# add(10,20)

# # 2. Check Even or Odd Using Function
# # Problem: Write a function that determines whether a number is even or odd.
# # Explanation: Even numbers are divisible by 2. The function should return “Even” or “Odd”.
# def even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input("entear a number"))
# print("the number is:",even(n))

# 3. Check Leap Year Using Function
# # Problem: Write a function that checks if a given year is a leap year.
# # Explanation: A leap year is divisible by 4 but not by 100 unless also divisible by 400.

# def leap_year(num):
#     if num%400==0 or  num%4==0 and num%100!=0:
#         return "leap_year"
#     else:
#         return "not_leap"
# num=int(input("entear a year"))
# print(num,"is leap")

# 4. Check Prime Number Using Function
# Problem: Write a function that checks whether a given number is prime.
# Explanation: A prime number has only two factors: 1 and itself.

def prime(num):
    if num>0:
        for i in range(2,(num**0.5)+1):
            if num%i==0:
                return "not peime"
        return "prime"
n=int(input("entear anumber"))
print(n ,prime(n))
#Function-Based Interview Questions – Logic & Practice:
#  1. Add Two Numbers Using Function:

# def add(a,b):
#     return a+b
# num1=int(input("entear a number:"))
# num2=int(input("entear a number:"))
# sum=add(num1,num2)
# print("sum=",sum)
# -------------------------------------------------------------------
# # 2. Check Even or Odd Using Function:

# def check_even_odd(num):
#     if num%2==0:
#         return "eveen"
#     else:
#         return "odd"
# n=int(input("entear anumber:"))
# result=check_even_odd(n)
# print(f'{n}is {result}')
# -----------------------------------------------------------------------
# 3. Check Leap Year Using Function:

# def check_leapyear(year):
#     if year%400==0 or year!=100 or year%4==0:
#         return "leap year"
#     else:
#         return "not leap year"
# n=int(input("entera a year:"))
# result=check_leapyear(n)
# print(f"{n} is {result}")
# -------------------------------------------------------------------------
# 4. Check Prime Number Using Function:

# def check_prime(num):
#     if num<2:
#         return "not a prime number"
#     for i in range(2,num):
#         if num%i==0:
#             return "not a prime number"
#     return "prime number"
# n=int(input("entear a number"))
# result=check_prime(n)
# print(f"{n} is {result}")

# --------------------------------------------------------------------------
# 5. Print Armstrong Numbers from m to n Using Function:
# def chech_armstrong(num):
#    digits=str(num)
#    power=len(digits)
#    total=sum(int(d)**power for d in digits)
#    return num==total
# def print_armstrong(m,n):
#    print(f"armstrong number between {m} and {n}: ",end=" ")
#    for i in range(m,n+1):
#       if is_armstrong(i):
#          print(i,end=" ")
# m=int(input("enter a number:"))
# n=int(input(input("entear a number:")))
# print_armstrong(m,n)


# ---------------------------------------------------------------------------

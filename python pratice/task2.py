# # 1. Check if a number is positive, negative, or zero
# num=3
# if num>0:
#     print("positive")
# elif num<0:
#     print("negitive")
# else:
#     print("zero")

# # 2. Check if a number is even or odd
# num=7
# if num%2==0:
#     print("eveen")
# else:
#     print("odd")

# # 3. Find the greatest of two numbers
# b=12
# a=15
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("both numbers are eaual")

# # 4. Find the greatest of three numbers
# a=12
# b=16
# c=17
# if a>=b and a>=c:
#     print("a is greaterthan")
# elif b>=a and b>=c:
#     print("b is graterthan")
# else:
#     print("c is graterthan")

# # 5. Check if a year is a leap year
# year=int(input("entear a year:"))
# if (year%400==0 or year%4==0 and year%100!=0):
#     print("leep year")
# else:
#     print("not leep year")

# # 6. Check if a character is a vowel or consonant
# str="aneela"
# vowel='aeiouAEIOU'
# v_count=0
# for i in str:
#     if i in vowel:  
#       v_count+=1
# print(v_count)

# 7. Check if one number is a multiple of another
a=int(input("enter the first number(a):"))
b = int(input("Enter the second number (b): "))
if b == 0:
    print("Division by zero is not allowed.")
elif a % b == 0:
    print(f"{a} is a multiple of {b}")
else:
    print(f"{a} is not a multiple of {b}")



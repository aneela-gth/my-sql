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
# #     if i in vowel:  
# #       v_count+=1
# # print(v_count)

# # 7. Check if one number is a multiple of another
# a=int(input("enter the first number(a):"))
# b = int(input("Enter the second number (b): "))
# if b == 0:
#     print("Division by zero is not allowed.")
# elif a % b == 0:
#     print(f"{a} is a multiple of {b}")
# else:
#     print(f"{a} is not a multiple of {b}")

# # 8. Create a simple calculator using if-else
# num1=float(input("entear a number"))
# operator=input("entear an operator(+,-,*,/):")
# num2=float(input("enter the second number:"))
# if operator=='+':
#     result=num1-num2
#     print(f"{num1}+{num2}=result")
# elif operator=='-':
#     result=num1-num2
#     print(f'{num1}-{num2}={result}')
# elif operator=='*':
#     result=num1*num2
#     print(f'{num1}*{num2}={result}')
# else:
#     print("invalid operator please use +,-,*or/")

# # 9. Check if a number is within a given range
# num = float(input("Enter a number: "))
# lower = float(input("Enter the lower bound of the range: "))
# upper = float(input("Enter the upper bound of the range: "))

# # Check if the number is within the range
# if lower <= num <= upper:
#     print(f"{num} is within the range {lower} to {upper}.")
# else:
#     print(f"{num} is not within the range {lower} to {upper}.")


# # 10. Check if a person qualifies for a discount
# age=int(input("entear a number"))
# is_member=input("age you a number (yes/no):").lower()
# if age<12:
#     print("you qualify for a child discount")
# elif age>=60:
#     print("you qualify for a senior citizen discount")
# elif is_member=="yes":
#     print("you qualify for a member discount")
# else:
#     print("you do not qualify for a discount")


# # 11. Check if a character is uppercase, lowercase, digit, or special character
# char = input("Enter a single character: ")
# if len(char)!=1:
#     print("please enter exactly one character")
# else:
#     if char.isupper():
#         print("the character is an uppercase letter")
#     elif char.islower():
#       print("The character is a lowercase letter.")
#     elif char.isdigit():
#         print("The character is a digit.")
#     else:
#         print("The character is a special character.")

# 12. Check if a person is eligible to vote

# # recursion:
# def fun(n):
#     if n==6: #base condiction
#         return
#     print(n)
#     fun(n+1)
# fun(1)

# reverse:
# def fun(n):
#     if n==0: #base condiction
#         return
#     print(n)
#     fun(n-1)
# fun(5)


# # 6. Factorial Using Recursion

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return fact(n-1)*n
# print(fact(5))

# # 7. Fibonacci Series Using Recursion

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(5):
#   print(fib(i))

 
# # 8. Sum of Digits Using Recursion

# def digit_sum(n):
#     if n==0:
#         return 0
#     else:
#       return n%10+digit_sum(n//10)
# print(digit_sum(123))

# # 9. Reverse a Number Using Recursion

# def reverse(n,rev=0):
#     if n==0:
#         return rev
#     else:
#         rev=rev*10+n%10
#         return reverse(n//10,rev)
# print(reverse(1234))
    

# # 10. Check Palindrome Using Recursion

# def is_palindeome(s):
#     if len(s)<=1:
#         return True
#     elif s[0]!=s[-1]:
#         return False
#     else:
#         return is_palindeome(s[1:-1])
# inp="madam"
# if is_palindeome(inp):
#     print("palindrome")
# else:
#     print("not a palindrome")
    

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#     def show(self):

#         print("Brand:", self.brand)
#         print("Color:", self.color)
# car1=Car("toyota","red")
# car2 = Car("BMW", "Black")
# car1.show()
# car2.show()

# # 1️⃣ Encapsulation (Data Hiding)
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance
    
# account=BankAccount(1000)
# account.deposit(500)
# print("Current Balance:", account.get_balance())


def fun(n):
    if n==6:
        return
    print(n)
    fun(n+1)
fun(1)

# # Python Functions - Practice Question Paper
# # 1. Palindrome Check
# # Write a function `is_palindrome(s)` that returns `True` if `s` is a palindrome, otherwise `False`.
# def palindrome(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     if s==rev:
#         return True
#     else:
#         return False
# z=palindrome("madam")
# print(z)

# def palindrome1(num):
#     temp=num
#     sum=0
#     while num>0:
#         rev=num%10
#         sum=sum*10+rev
#         num=num//10
#     if temp==sum:
#         return True
#     else:
#         return False
# print(palindrome1(121))


# # 2. Factorial Using Function
# # Write a function `factorial(n)` that returns the factorial of a number using recursion.


# def fact(num):
#     fact=1
#     for i in range(2,num+1):
#         fact=fact*i
# if fact==num:
#  True

# # 3. Count Vowels
# # Write a function `count_vowels(s)` that returns the number of vowels in a string.
# def c_vowels(s):
#     vowiles="aeiou"
#     v_count=0
#     for ch in s:
       
#       if ch in vowiles:
#         v_count+=1
#     return v_count
    
# print(c_vowels("aneela"))

# # 4. Prime Number Check
# # Write a function `is_prime(n)` that checks whether a number is prime or not.

# def prime(num):
#     if num<1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     print(num ,"is prime")
#     return True
# print(prime(7))


# # 5. Reverse a String
# # Write a function `reverse_string(s)` that returns the reversed string.
# def r_string(name):
#     rev=""
#     for ch in name:
#         rev=ch+rev
#     return rev
# print(r_string('hello'))
    

# # 6. Fibonacci Series
# # Write a recursive function `fibonacci(n)` that prints the Fibonacci series up to `n` terms.
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         temp=a+b
#         a=b
#         b=temp
#         print(temp)
# fib(8)   


   
# n=5
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n):
#  c=a+b
#  a=b
#  b=c
#  print(c)

# # 7. Armstrong Number Check
# # Write a function `is_armstrong(n)` that checks if a number is an Armstrong number.
# def armstrong(num):
#     temp=num
#     len=0
#     while temp>0:
#         len+=1
#         temp=temp//10

#     sum=0
#     ans=num
#     while ans>0:
#         rem=ans%10
#         sum+=rem**len
#         ans=ans//10
#     if num==sum:
#         return 'armstrong'
#     else:
#         return 'not armstrong'
# print(armstrong(370))



# 8. Strong Number Check
# Write a function `is_strong(n)` that checks whether a number is a strong number.


# 9. Perfect Number
# Write a function `is_perfect(n)` that checks whether a number is a perfect number.


# 10. Calculator Function
# Write a function `calculator(a, b, op)` that performs `+`, `-`, `*`, `/` based on the operator passed.




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

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

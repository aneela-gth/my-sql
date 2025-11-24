# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. Explanation: Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5
# using for loop:

# n=int(input("entear number:"))
# for i in range(1,n+1):
#     print(i)

# using while loop:
# n=int(input("entear number:"))
# i=1
# while i<n+1:
#     print(i)
#     i+=1

# 2.Print Numbers from m to n
# Question: Write a program to print numbers from m to n. Explanation: Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7
# m=int(input("entear a number"))
# n=int(input("entear a number"))
# for i in range(m,n+1):
#     print(i)

# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1
# for i in range(5,0,-1):
#     print(i)

# while loop using:
# i=0
# n=5
# while i<n:
#     print(i)
#     n-=1


# 4.. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6
# n=10
# m=6
# for i in range(10,0,-1):
#     print(i)

# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n natural numbers. Explanation: Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15

# num=10
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)

# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120
# n=5
# fact=1
# for i in range(2,n+1):
#     fact=fact*i
# print(fact)


# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18
# m=3
# n=6
# sum=0
# for i in range(1,7):
#     sum+=i
# print(sum)
# sum=m*n
# print(sum)

# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24
# n=2
# m=4
# product=1
# for i in range(2,5):
#     product*=i
# print(product)

# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6
# num=6
# for i in range(1,num+1):
#   if num%i==0:
#     print(i,end=" ")

# 10. Count of Factors
# Question: Write a program to count how many factors a number has. Explanation: Increment count when divisible. - Input: n = 6 - Output: 4
# num=6
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#      count+=1
# print(count)

# 11. Prime Number Check
# Question: Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime
# num=7
# count=0
# for i in range(1,num+1):
#    if num%i==0:
#     count+=1
# if count==2:
#   print("prime")
# else:
#   print("not prime number")

# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10
# m=3
# n=10
# for i in range(3,11):
#     if i%2==0:
#         print(i,end=" ")

# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9
# m=3
# n=10
# for i in range(2,11):
#     if i%2!=0:
#         print(i,end=" ")

# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3
# m=1
# n=10
# even=0
# odd=0
# for i in range(1,11):
#     if i%2==0 :
#         even+=1
#     else:
#         odd+=1    
# print("even",even)
# print("odd",odd)

# 15. Reverse a String
# Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”
# str="hello"
# rev=" "
# for ch in str:
#     rev=ch+rev
# print(rev)

# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome
# str="madam"
# rev=""
# for ch in str:
#     rev=ch+rev
# if str==rev:
#   print("palindrom")
# else:'''
#    print("not palindrom")

# name="Madam"
# name=name.lower()
# rev=""
# for i in name:
#     rev=i+rev
# if(rev==name):
#     print("palindrom")
# else:
#     print("not palindrom")
# word="level"
# rev="" 
# for i in word:
#     rev=rev+i
# if(rev==word):
#     print("it is palindrom")
# else:
#     print("it is not palindrom")
# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6
# num=123
# sum=0
# for i in range(1,num+1):
#     if i%10==0:
#         sum+=1
# print(sum)


# num=123
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)

# num=126
# sum=0
# while num!=0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)

# num=123
# rev=0
# while num!=0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# 18. Product of Digits
# Question: Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6
# num=123
# sum=1
# while num!=0
#     rem=num%10
#     sum=sum*rem
#     num=num//10
# print(sum)

# num=234
# product=1
# while num!=0:
#     var=num%10
#     product=product*var
#     num=num//10
# print(product)

# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number
# amstrong means:degites based (square  or) and add the value is called an amgstrong
# num=153
# len=0
# temp=0
# while num>0:
#     len+=1
#     num=num//10
# sum=0
# ans=0
# while num>0:
#     rem=num%10
#     sum=sum*10+rem
#     num=num//10
# if(sum==temp):
#     print("amstronge number")
# else:
#     print("not a amstrong")

# num=153
# len=0
# while num!=0:-------->digit lenth find with out using built in functions
#     len+=1
#     num=num//10
# print(len)
# --------------------------------------------------------------------
# num=153
# temp=num
# len=0
# while temp!=0:
#     len+=1
#     temp=temp//10
# sum=0
# ans=num
# while ans!=0:
#     rem=ans%10
#     sum=sum+rem**len
#     ans=ans//10
# if sum==num:
#     print("armstrong number")
# else:
#     print("not an armstrong number")


# 20. Reverse a Number
# Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321

# num=123
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# 21. Palindrome Number Check
# Question: Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome
# num=121
# temp=num
# rev=0
# while num!=0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if(rev==temp):
#     print("palindrom")
# else:
#     print("not palindrom")


# 22. Count Vowels in String
# Question: Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2
# name="apple"
# vowels="aeiouAEIOU"
# # v_count=0
# c_count=0
# for i in name:
#     if i in vowels:
#         v_count+=1
    
# print(v_count)
# name="programming"
# vowels="aeiouAEIOU"
# c_count=0
# for i in name:
#     if i not in vowels:
#         c_count+=1
# print(c_count)
# name="programming"
# vowels="aeiouAEIOU"
# v_count=0
# c_count=0
# for i in name:
#     if i in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)

# 23. Count Consonants in String
# Question: Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 3

# name="apple"
# vowels="aeiou"
# c_count=0
# for i in name:
#     if i not in vowels:
#         c_count+=1
# print(c_count)

# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3
# name="apple"
# vowels="aeiouAEIOU"
# v_count=0
# c_count=0
# for i in name:
#     if i in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)
# 25. Perfect Number Check
# Question: Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number
# num=28
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print("perfect number")
# else:
#     print("not perfect number")
# 26. Neon Number Check
# Question: Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - Input: 9 - Output: Neon number
# num=9
# sum=0
# square=num*num
# for i in str(square):
#     sum+=int(i)
# if (sum==num):
#     print(f"{num} is neonnumber")
# else:
#     print(f"{num}is not a neonnumber")

# num=9
# temp=num
# sqr=temp*temp
# sum=0
# while sqr!=0:
#     rem=sqr%10
#     sum=sum+rem
#     sqr=sqr//10
# if(sum==num):
#     print(f"{num} is neonnumber")
# else:
#     print(f"{num}is not a neonnumber")

# 27. Strong Number Check
# Question: Check if a number is a strong number. Explanation: Sum of factorial of digits equals the number. - Input: 145 - Output: Strong number
# num=145    6                              
# temp=num
# fact_sum=0
# while temp!=0:
#     rem=temp%10
#     fact=1
#     for i in range(2,rem+1):
#         fact *= i
#     fact_sum += fact
#     temp=temp//10
# if fact_sum==num:
#     print("stronge number")
# else:
#     print("not strong number")


# 28. Harshad Number Check
# Question: Check if a number is divisible by the sum of its digits. Explanation: Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number
# num=18
# sum=0
# while num!=0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# if num%sum==0:
#     print("harshad number")
# else:
#     print("not harshad number")

# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3
# n=5
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# 30. Check for Neon Number (Repeated)
# Question: Again, check for a neon number (example). Explanation: Square number and sum digits. - Input: 9 - Output: Neon number
# num=9
# sum=0
# sqare=num*num
# for i in str(sqare):
#         sum+=int(i)
# if(sum==num):
#     print(f"{num} is neon number")
# else:
#       print(f"{num}is not a neon number")

# num=9
# sum=0
# sqare=num*num
# temp=sqare
# while temp > 0:
#     rem=temp%10
#     sum+=rem
#     temp=temp//10
# if sum==num:
#     print("neonnumber")
# else:
#     print("not a neonnumber")



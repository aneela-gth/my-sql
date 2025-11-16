# 1.print revers string
# str="hello"
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)

# name="level"
# rev=""
# for i in name:
#     rev=i+rev
# print(rev)


# 2.check palindrom
# num=121
# rev=0
# temp=num
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if (rev==temp):
#     print("palindrom")
# else:
#     print("not palindrom")


# num=323
# rev=0
# temp=num
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if rev==temp:
#     print("palindrom")
# else:
#     print("not a palindrom")


# Count Vowels in String
# name="pythonfullstck"
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


# name="aneela"
# vowels="aeiouAEIOU"
# for i  in name:
#     if i not in vowels:
#      print(i ,end="  ")

# 25. Perfect Number Check
# num=6
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if (num==sum):
#     print("perfectnumber")
# else:
#     print("not perfectnumber")


# # neon:
# num=9
# square=num*num
# sum=0
# for i in str(square):
#     sum+=int(i)
# if sum==num:
#     print(f"{num}is a neon")
# else:
#     print(f"{num}is not neon")

# --------------------------------------------------------------------------------------------------------------
# 1.
# for num in range(1,101):
#     if (num%7==0):
#         print(num)

# 2.
# for num in range(1,11):
#         print(num**2)

# 3.Find the sum of even numbers between 1 and N.
# n=int(input("entear a number:"))
# sum_even=0
# for num in range(1,n+1):
#     if num%2==0:
#         sum_even+=num
# print(sum_even)

#  4.Find the product of digits in a number.
# num=int(input("entear a number"))
# product=1
# temp=num
# while temp >0:
#     digit=temp%10
#     product*=digit
#     temp//=10
# print(f"product of digits in {num}is {product}")

# 5. Find the smallest digit in a number.
# num=531
# smalest=1
# temp=num
# while temp>0:
#     digit=temp%10
#     if digit <smalest:
#         smallest=digit
#     temp//=10
# print(f"Smallest digit in {num} is {smalest}")

#  7.Count how many digits are even and how many are odd in a number.
# num=int(input("entear a number:"))
# even_count=0
# odd_count=0
# for i in range(1,num+1):
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print(even_count)  
# print(odd_count)   

# num=23456
# even_count=0
# odd_count=0
# while num!=0:
#     ld=num%10
#     if ld%2==0:
#      even_count+=1
#     else:
#         odd_count+=1
#     num=num//10
# print(even_count)
# print(odd_count)            
        


    
# sentance=input("entear a sentance:")
# word=sentance.split()
# print(word)
# words_count=len(word)
# print(words_count)
# v_count=0
# c_count=0
# vowles="aeiouAEIOU"
# for i in vowles:
#     if i in sentance:
#         v_count+=1
    
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)



# num=int(input("enter a number:"))
# fact=1
# i=1
# if num<0:
#     print("factorial does not exist for negative numbers")
# else:
#     while i<=num:
#         fact=fact*i
#         i+=1
#     print("factorial of",num, "is",fact)


# num=5
# a=0
# b=1
# print(a,b, end=" ")
# for i in range(2,num):
#     temp=a+b
#     print(temp ,end=" ")
#     a=b
#     b=temp

#  8. Print all prime numbers between two numbers (input from user).
# num1=int(input("entear a number:"))
# num2=int(input("entear a number"))
# count=0
# for i in range(num1,num2+1):
#     if i>1:
#         for x in range(2,i):
#             if x%i==0:
#                 break
#             else:
#                 print(i)
# num=int(input("entear a numbear"))
# count=0
# if num>1:
#    for i in range(2,num):
#       if num%i==0:
#          print(num,"is not a prime number")
#          break
#       else:
#          print(num,"is a prime number")
# else:
#    print(num,"is not a prime number")

# 1. Check if a number is positive, negative, or zero
# n=int(input("entear a numbear"))
# if(n>0):
#     print("positive")
# elif(n<0):
#     print("negitive")
# else:
#     print("zero")


# num=123
# temp=num
# rev=0
# while num!=0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if rev==temp:
#     print("palindrom")
# else:
#     print("not a palindrom")
# num=121

# num=6932
# while num>0:
#     digit=num%10
#     if digit<min:
#         min=digit
#     if digit>max:
#         max=digit
#     if min==0:
#         min=digit
#     num=num//10
             
# name="naresh"
# vowiles="aeiou"
# v_count=0
# c_count=0
# for i in name:
#     if i in vowiles:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)


# name="naresh"
# vowles="aeiou"
# for i in name:
#     if i not in vowles:
#         print(i)

# m=10
# n=30
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,int(i**0.5)):
#             if i%j==0:
#                 break
#             else:
#                 print(i,end=" ")

# n=10
# for i in range(1,n+1):
#     if i%2!=0:
#         continue
#     print(i,end=" ")

# # swape numbers:
# a=10
# b=20
# temp=a
# a=b
# b=temp
# print("afteraar swapping:a=",a,"b=",b)
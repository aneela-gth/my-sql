# x=20
# y=30
# op=x*y
# print(op)

# a=2
# b=3
# op=a+b
# print(op)

# c=57
# d=98
# op=c-d
# print(op)

# a=2,4
# b=5,4
# print(a)

# x=5,7
# y=3,7
# m=3
# n=7
# for i in range(m,n):
#     print(i)
# n=5
# for i in range(n,0,-1):
#     print(i,end=" ")
# n=10
# m=5
# for i in range(n,m,-1):
#     print(i,end=" ")
# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# m=3
# n=6
# sum=0
# for i in range(m,n+1):
#     sum+=i
# print(sum)

# for i in range(1,11):
#     print(i**2)

# for i in range(1,10):
#     if i%2!=0:
#         print(i)

# m=2
# n=4
# product=1
# for i in range(m,n+1):
#     product*=i
# print(product)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=6
# f_count=0
# for i in range(1,n+1):
#     if n%i==0:
#        f_count+=1
# print(f_count)

# n=7
# count=0
# for i in range(1,n+1):
#      if n%i==0:
#        count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")
    
# m=3
# n=10
# for i in range(m,n+1):
#     if i%2==0:
#         print(i)

    
# m=3
# n=10
# for i in range(m,n+1):
#     if i%2!=0:
#         print(i)

# m=3
# n=7
# e_count=0
# c_count=0
# for i in range(m,n+1):
#     if i%2==0:
#         e_count+=1
#     else:
#         c_count+=1
# print("even count:",e_count)
# print("odd count:",c_count)
# n=10
# for i in range(1,n+1,2):
#     print(i)
# n=10
# for i in range(1,n+1):
#     if i%2==0:
#       print(i)

# name="hello"
# str=""
# for i in name:
#     str=i+str
# print(str)

# name="madam"
# rev=""
# for i in name:
#     rev=i+rev
# if rev==name:
#     print("palindrom")
# else:
#     print("not a palindrom")

# num=121
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if(rev==temp):
#     print("palindrom")
# else:
#     print("not a palindrom")

# num=153
# len=0
# while num!=0:
#     len+=1
#     num=num//10
# print(len)

num=153
len=0
temp=num
while temp!=0:
    len+=1
    temp=temp//10
sum=0
ans=num
while ans!=0:
    rem=ans%10
    sum=sum+rem**len
    ans=ans//10
if sum==num:
    print("armosting")
else:
    print("not amrstong")




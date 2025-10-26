
# Write a program to check input string is palindrome or not using while loop
num=121
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(rev==temp):
    print("palindrom")
else:
    print("not palindrom")
# Write a program to reverse a number without converting into string
num=int(input("entear a number:"))
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)


'''#1.area of square
side=5
area=side*side
print("area of sqare is:",area)

#2.area of rectangle
length=6
breadth=4
area=length*breadth
print("area of rectangle is:",area)

#3.area of triangal
base=8
height=5
area=0.5*base*height
print("area of triangle is:",area)

#4.perimeter of square:
side=6
perimetet=4*side
print("perimeter of square is:",perimetet)

#5.perimeter of rectangle
length=5
breadth=3
perimetet=2*(length+breadth)
print("perimeter of rectangle is:",perimetet)

#6.perimeter of triangle
side1=5
side2=6
side3=7
perimeter=side1+side2+side3
print("Perimeter of triangle is",perimetet)

#7.break amount into 1000s,500s,and remaning change
amount=3700
thousand=amount//1000
amount=amount%1000
five_hundres=amount//500
amount=amount%500
remaining=amount
print("1000s:",thousand)
print("500s:",five_hundres)
print("remaining:",remaining)

8.convert seconds into hours,minutes,and seconds
total_seconds=3672
hours=total_seconds//3600
total_seconds=total_seconds%3600
minutes=total_seconds//60
seconds=total_seconds%6
print("hours:",hours)
print("minutes:",minutes)
print("seconds:",seconds)

#9.sum of marks(mathes,physics,chemistry)
maths=85
physics=90
chemistry=88
sum=maths+physics+chemistry
print(sum)

#10.average of marks(maths,physics,chemistry)
maths=85
physics=90
chemistry=88
average=(maths+physics+chemistry)/3
print(average)


2.DPF

1.check even or odd
number=6
if(number%2==0):
    print("a number is evven:",number)
else:
    print("a number is odd")

# 2.divisible by 5 but not by 10
number=25
if(number%5==0 and number%10!=0):
    print("number divisible by 5 :",number)
else:
    print("number divisible by 10:",number)

#3.smallest among two number
A=4
B=7
if(A<B):
    print("smaller value:",A)
else:
    print("smaller value:",B)

#4.biggest among two numbers
A=4
B=7
if(A>B):
    print("biggest value:",A)
else:
    print("biggest value:",B)
#5.divisible by 2,3,and 6
number=18
if(number%2==0 and number%3==0 and number%6==0):
    print("satisfy")
else:
    print("not satisfy")

#6.voting eligibility
age=19
if(age>=18):
    print(" eligible to vote")
else:
    print("not eligible to vote ")

#7.student pass/fail based on all subjects>=35
maths=20
physics=38
chemistry=25
if(maths>=35 and physics>=35 and chemistry>=35):
    print("pass")
else:
    print("fail")

# 8.student pass if passed any two subjects
maths=40
physics=20
chemistry=36
if(maths>=35 or physics>=35 or chemistry>=35):
    print("pass")
else:
    print("fail")

# 9.student pass if passed any two subjects
maths=40
physics=20
chemistry=36
passed_subjects=0
if maths>=35:
    passed_subjects+=1
    if physics>=35:
        passed_subjects+=1
        if chemistry>=35:
            passed_subjects+=1
            if passed_subjects>=2:
                print("pass")
            else:
                print("fail")

# 10.biggest among three number
a=7
b=4
c=9
if(a>=b and a>=c):
    print("a is biggest number:",a)
elif(b>=a and b>=c):
    print("b is biggest:",b)
else:
    print("c is biggest :",c)

# 11.prime number check
n=7
for i in range(1,n+1):
    if n%i==0:
        print("prime")

# 12.perfect square or not
number=49
if number**2==0:
    print(square)

# 13.second biggest among three number
a=10
b=25
c=18
if(a>b and a>c):
    print("a is biggest number:",a)
elif(b>a and b>c):
    print("b is biggest number:",b)
else:
    print("c is biggest number:",c)

# 14.leap year or not
year=2014
if(year%4==0):
    print("it is leep eyer")
else:
    print("it is not leep eyer")'''
    
# 3 PDF
'''# 1.prime number feom 1 to n
n=5
for i in range(1,n+1):
    print(i,end="")'''
'''
# 2.prime numbers  from m to n
m=3
n=7
for i in range(3,8):
    print(i,end="")'''

# 3.prime numbers from n to m in revers
'''n=10
m=6
for i in range(10,5,-1):
    print(i)
'''
#4.prime numbers from n to 1 in reverse
'''n=5
for i in range(n,0,-1):
    print(i,end="")'''

# 5.sum of n natureal numbers
# n=5
# sum=0
# for i in range(1,6):
#     sum+=i
# print(sum)

# 6.factorial of a number
# n=5
# for i in range(1,5+1):
#    5*=i
#    print(i)

# sum of natural numbers
# n=5
sum=0
for i in range(5):
    sum+=i
    print(i)














































































    


#list functions
'''# append in the list
x=[1,2,3,4,5]
x.append(6)
print(x)
# extend multiple valuse cak add in the lind
v=[1,2,3,4,5]
v.extend([6,7,8,9])
print(v)
# insert 
z=[9,8,65,4,54]
z.insert(1,20)
print(z)
# remove
a=[12,32,51,98]
a.remove(32)
print(a)'''
# pop
# x=[12,13,14,15,16]
# x.pop(14)
# print(x)

# count
# x=[1,2,1,4,1,6]
# print(x.count(1))
# index
# z=[1,2,3,4,5,6,7]
# print(z.index(5))

# # clear
# x=[1,2,3,4,56,7,8]
# x.clear()
# print(x)

# sort
# a=[1,2,3,4,5,67,8,9]
# a.sort()
# print(a)

# reverse
# z=[1,2,3,45,6,7]
# z.reverse()
# print(z)

# copy
# z=[1,2,34,5,6,7,8]
# z.copy()
# print(z)


# string methodes
# len
# z="aneela"
# print(len(z))
# upper
# print(z.upper())
# print(z.lower())
# print(z.lstrip())
# print(z.rstrip())
# print(z.strip())
# print(z.count("a"))
# print(z.replace("aneela","naresh"))
# print(z.find("n"))
# print("aneela",startwith("an"))
# print(z.split(""))
# list=["i","am","a","python","developer"]
# print("".join(list))
# print("123".isdigit())
# print("abc".isalpha)
# print("abc123".isalnum())
# print("HELL".isupper())
# print("hello".swapcase())




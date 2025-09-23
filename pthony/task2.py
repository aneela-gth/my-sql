# #1.area of square
# side=5
# area=side*side
# print("area of sqare is:",area)

# #2.area of rectangle
# length=6
# breadth=4
# area=length*breadth
# print("area of rectangle is:",area)

# #3.area of triangal
# base=8
# height=5
# area=0.5*base*height
# print("area of triangle is:",area)

# #4.perimeter of square:
# side=6
# perimetet=4*side
# print("perimeter of square is:",perimetet)

# #5.perimeter of rectangle
# length=5
# breadth=3
# perimetet=2*(length+breadth)
# print("perimeter of rectangle is:",perimetet)

# #6.perimeter of triangle
# side1=5
# side2=6
# side3=7
# perimeter=side1+side2+side3
# print("Perimeter of triangle is",perimetet)

# #7.break amount into 1000s,500s,and remaning change
# amount=3700
# thousand=amount//1000
# amount=amount%1000
# five_hundres=amount//500
# amount=amount%500
# remaining=amount
# print("1000s:",thousand)
# print("500s:",five_hundres)
# print("remaining:",remaining)

#8.convert seconds into hours,minutes,and seconds
# total_seconds=3672
# hours=total_seconds//3600
# total_seconds=total_seconds%3600
# minutes=total_seconds//60
# seconds=total_seconds%6
# print("hours:",hours)
# print("minutes:",minutes)
# print("seconds:",seconds)

# #9.sum of marks(mathes,physics,chemistry)
# maths=85
# physics=90
# chemistry=88
# sum=maths+physics+chemistry
# print(sum)

# #10.average of marks(maths,physics,chemistry)
# maths=85
# physics=90
# chemistry=88
# average=(maths+physics+chemistry)/3
# print(average)


#2.DPF

# 1.check even or odd
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
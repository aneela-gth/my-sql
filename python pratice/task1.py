#1.check even or odd
x=int(input("enter a number"))
if(x%2==0):
    print("given numbr is even")
else:
    print("givrn numbr is odd")
#2.age group classifier
x=int(input("enter your age"))
if(x<13):
    print("child")
elif( 13<=x<20):
    print("teen")
else:
    print("adult")

#3.check if a given number is positive,negative,or zerog
num=int(input("enter a numbr"))
if(num>0):
    print("the number is a positive")
elif((num<0)):
    print("the number is negative")
else:
    print("the number is zero")
#4.divisibility checker check a number is divisible by both 3 and 5
x=int(input("enter a number"))
if(x%3==0 and x%5==0):
    print(f"{x} is divisibli by  both 3 and 5")
else:
    print( f"{x} is not divisibily by 3 and 5")
#5.find largest of two numbers
a=int(input("enter first number"))
b=int(input("enter second number"))
if(a>b):
    print("largest number:")
elif(b<a):
    print("largest number:")
else:
    print("both numbers are equal")
#6.triangle valldity checker give three sides(eg: s1=15,s2=10,s3=23), check if they can form a triangle(that is ,sum of sny two sides>third side)
s1=int(input("enter value a:"))
s2=int(input("enter value b:"))
s3=int(input("enter value c:"))
if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
    print("is triangle")
else:
    print("can not from a triangle")

#for loop with sequential data:
#1.print each character of a string
str="hello"
for i in str:
 str+=i
 print(i ,end=" ")

 #2.sum of first 10 natural numbers use a for  ioop with range()
sum=0
for x in range(1,11):
    sum+=x
print("sum of  first 10 natural numbers:",sum)

#3. print eveen numbers from 1 to 20
for i in range(2,21):
     if i%2==0:
         print(i)
#4.print elements in list
list=["pen","pencll","ersser"]
for i in list:
        print(i)
#5. print common elementes in two lists
list1=[6,2,4,5,1]
list2=[4,2,7,6,1]
for x in list1:
    if x in list2:
        print(x)
#6.print all elementes in a set
my_set={"apple","banana","cherry"}
for i in my_set:
    print(i)
#7.count how many items are in a set using a loop
colors={"red","blue","green","yellow"}
for x in colors:
    a=len(colors)
print(a)
#8.print all keys and  values in a dicitionary
person={"name":"alice","age":25,"city":"delhi"}
for key, value in person.items():
    print(key,":",value)
# 9. Count how many values in a dictionary are greater than 50
    #  scores = {"math": 45, "english": 55, "science": 80, "history": 40}
scores = {"math": 45, "english": 55, "science": 80, "history": 40}
values = list(scores.values())  # Convert dictionary values to a list
i = 0
count = 0

while i < len(values):
    if values[i] > 50:
        count += 1
    i += 1

print("Number of values greater than 50:", count)

# 10. Create a new dictionary with only items where the value is even
#    data = {"a": 1, "b": 4, "c": 6, "d": 3}
data = {"a": 1, "b": 4, "c": 6, "d": 3}
keys = list(data.keys())
i = 0
new_dict = {}

while i < len(keys):
    key = keys[i]
    if data[key] % 2 == 0:
        new_dict[key] = data[key]
    i += 1

print("New dictionary with even values:", new_dict)
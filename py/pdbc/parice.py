nums=[10,20,30,40]
nums.insert(2,25)
nums.remove(40)
print(nums)
#2.
word="programming"
print(word[0:6])
print(word[-3:])
#3.
word="programming"
if len(word)>5:
    print(word[::2])
else:
    print(word[::-1])
#verables pratice qustiones:
#1.Create variables name, age, and city. Print them in one sentence.
name="aneela"
age=23
city="hyd"
print(f"my name is {name},i am {age},and i live in{city}")
#2.Swapping Variables:
#Create two variables x = 5 and y = 10. Swap their values without using a third variable.
x=5
y=10
x,y=y,x
print("x=",x)
print("y=",y)
#Type Checking
# Create variables of type:
x=3
print(type(x))
y=3.5
print(type(y))
z="anee"
print(type(z))
# a=2
b=3+4j
print(type(b))
# Updating Variables
# Create a variable counter = 0.
# Increase it by 5, then by 10, then subtract 3.
# Print the final value.
counter=0
counter=counter+5
counter=counter+10
counter=counter-3
print("final value of counter:",counter)
# oops
# mehodes lo onlye using self

# method:1

# class add:
#     x=100
#     y=200
#     def sum(self):
#         print("addiction=",self.x+self.y)
# obj=add()
# obj.sum()

# method:2
# class add:
#     x=100
#     y=200
#     def sum(self):
#         return self.x+self.y
# obj=add()
# print("addiction=",obj.sum())
# print("x value=",obj.x)
   


# class mult:
#     x=100
#     y=2
#     def sum(self):
#         print("multipclaction=",self.x*self.y)
# obj=mult()
# obj.sum()


# class car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
# mycar=car("tayato","bule")
# print("brand:",mycar.brand)
# print("color:",mycar.color)


# inheritance:
# baseclass or superclass: it is a class which is ready to give resourches to another class
# derivedclass or sub class:it is a class is ready to take resources from another class

# singleinheritance:

# class robo():
#     def one(self):
#         print("this is baseclass")
# class chitti(robo):
#     def two(self):
#         print("this is derived class")
# obj=chitti()
# obj.one()
# obj.two()

# class dog():
#     def one(self):
#         print("gog is runnig fast")
# class rabbit():
#     def two(self):
#         print("rabbit is running slow")
# obj1=dog()
# obj1.one()
# obj2=rabbit()
# obj2.two()


# class laptop:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
# lap1=laptop("hp",5423)
# print("brand",lap1.brand)
# print("price",lap1.price)


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# std=student("aneela",22)
# print("name",std.name)
# print("name",std.age)

# class book:
#     def __init__(self,titile,author):
#         self.titile=titile
#         self.author=author
#     def info(self):
#      print(f"Title: {self.titile}, Author: {self.author}")
# b1=book("python","jhon")
# b2=book("ai intro","andrew ng")
# b1.info()
# b2.info()

# class bike:
#     def start(self):
#         print("bike started")
# b=bike()
# b.start()

# class Area:
#     def square_area(self, side):
#         return side * side

# obj = Area()
# print(obj.square_area(4))
# print(obj.square_area(6))
# print(obj.square_area(8))


# class Animal:
#     def sound(self):
#         print("Animals make sound")

# class Dog(Animal):
#     pass

# d = Dog()
# d.sound()

# class vehicle:
#     def __init__(self):
#         print("vehicle is moving")

#     def move(self):
#         print("vehicle can move")

# class car(vehicle):
#     def drive(self):
#         print("car is driving")

# c = car()
# c.move()
# c.drive()


# # multilevel:
# class robo:
#     def one(self):
#         print("jhon is bc")
# class sana(robo):
#     def two(self):
#         print("jhon is dc1")
# class chitti(sana):
#     def three(self):
#         print("jhon is dc2")
# obj=chitti()
# obj.one()
# obj.two()
# obj.three()

class Bank:
    def deposit(self, amount):
        print(f"Deposited: {amount}")

class SBI(Bank):
    def roi(self):
        print("SBI Rate of Interest is 5%")

s = SBI()
s.deposit(5000)
s.roi()

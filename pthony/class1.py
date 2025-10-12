# class vehicle:
#     def __init__(selef,brand,modeal):
#         selef.brand=brand
#         selef.modeal=modeal
#     def enginestarted(selef):
#         print(f"{selef.modeal}of{selef.brand}has started")
#     def enginestop(selef):
#         print(f"{selef.modeal}has stoped")
# bike1=vehicle("pulsear","clasiceal303")
# bike1.enginestarted()
# bike1.enginestop()

# encaplucation:
# wraping up of data inside a class or method so that it cannot be acessed directly
# three types of variables:
# 1.public:it can be accessed directly
# 2.protected: _ it can be acessed directly,it is just a naming convention
# 3.private: __ it cannot be accessed directly

# exampleprogram:
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def getBalance(self):
#         print(f'you current  balance is:{self.__balance}')
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f'{amount}has  been credited to you account')
#             print(f'your new balnce is:{self.__balance}')
#         else:
#             print("invalid amount")
    
#     def withdraw(self,amount):
#         if 0<amount<self.__balance:
#             self.__balance-=amount
#             print(f'{amount}has been debited from your account')
#             print(f'')


# custumear1=BankAccount('aneela',50000) 
# custumear1.getBalance()       

# polymorphism:
# stans for many forms
# functions with same name performin differently based on class and objects
# 1.Duck Typing :  if it walks like a duck and quacks like a duck then it is a duck
#---> if an object has certain features then it is considered as an object of certain category, irrespective of its real identy
# 2.method overrriding :
# 3.method.
# 4.operator ovearloading

#  example program:
# class dog:
#     def speak(self):
#         print('dog barks')
#     def walk(self):
#         print('dog walks')
# class cat:
#     def speak(self):
#         print('cat meows')
#     def walk(self):
#         print('cat walks')
# class man:
#     def speak(self):
#         print('man talks')
#     def walk(self):
#         print('man walk') 
# def checking(obj):
#     obj.speak() 
#     obj.walk()
#     print('then it_is a man')  

# dog1=dog()
# cat1=cat()
# man1=man()

# methodoverriding with out inheritance

# class father:
#     def work(self):
#         print('he does work to provide his family')
# class mothor:
#     def work(self):
#         print('she takes care of family')

# father1=father()
# mothor1=mothor()
# father1.work()
# mothor1.work()


# methodoverriding with inheritance
class vehicle:
    def start(self):
        print('vehicle started')
class car(vehicle):
    def start(self):
        print('car started')
car1=car()
car1.start()

# simulating method overloading using default arguments
class math:
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d
m1=math()
print(m1.add(3))
print(m1.add(3,4))
print(m1.add(3,5,6,3))

# operator overloading
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,otherbook):
        return self.pages+otherbook.pages

book1=book(250)
book2=book(300)
print(book1+book2)
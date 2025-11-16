
# enhance--->addin additional features without chnaging the original functionality
# decorator--->it ia a function that enhances other function
# @decorator_name

def sum(a,b):
    if type(a)!="int"or type(b)!="int":
        print("not possible")
    print(a+b)
sum(1,2)
sum("hello",5)
# function-->function is a block of reusable block of scop

# defining a decorator:

def check_msg(func):     #this is the decorator name(main function)
    def wrapper():      #for adding functionalities for the original functions
        print("before original function")
        func()
        print("after the originalmfunction")
    return wrapper
@check_msg   #using a decorator on function
def say_hello():
    print("hello world")
    say_hello()

def good_eveng():
    print("good evening")
good_eveng()


def check_int(fun):
    def wrapper(a,b):
        if type(a)!="int"or type(b)!="int":
            return "invalid inputs"
        res=fun(a,b)
        return res
    return wrapper
@check_int
def sum(a,b):
    print(a+b)
print(sum(1,2))    
print(isinstance(True,bool))
# --------------------------------------------------------------------
def check_int(fun):
    def wrapper(a,b):
        if not isinstance(a,int)or not isinstance(b,int):
            return "invalid inputs"
        res=fun(a,b)  #only when is a return statement in the origineal function
        return res
    return wrapper
@check_int
def sum(a,b):
    print(a+b)
print(sum("1",2)) 

@check_int
def add_num(m,n):
    return m+n 
print(add_num(10,20))
# print(not instance(True,bool))



# -----------------------------------------------------------------------------
def check_str(func):
    def wraper(n):
        if not isinstance(n,str):
            return "not a name"
        res=func(n)
        return res
    return wraper

@check_str
def wish(name):
    return "hello"+name
print(wish("123"))
# ------------------------------------------------------------------------------------
# *args ,**kwargs
def has_zero(org):
    def wrapper(*args):
        if 0 in args:
            res=org("mani")
            return res
        else:
            res=org(*args)
            return res
    return wrapper

@has_zero
def params(*args):
    return args
print(params(1,2,3,4))  #number of parameters pass chyavchyu by using *args
# --------------------------------------------------------------------------------------------------
# task:

def decorator_name(name):
     def wrapper(*args):
        if "nari" in args:
            return "invalid names"
        res=name(*args)
        return res
     return wrapper

@decorator_name
def params(*args):
    return args
print(params("aneela","rani","svani","sunny"))

# ---------------------------------------------------------------------------------------------------------
# def decorator_name(original func as a param):
#     def wrapper(to access prams of original function):
#         res=original(prams)
#         return res
#     return wrapper

# @deccorator_name


def ane_int(color):
    def wrapper(*args):
        if "oreange" in args:
            return "invalid colors"
        res=color(*args)
        return res
    return wrapper
@ane_int
def param(*args):
    return args
print(param("blue","green","red","yellow","pink"))

def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()

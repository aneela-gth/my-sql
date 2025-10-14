import json
import random
from auth import signup
from auth import login
def start():
    ip=int(input("enter choice:"))
    if ip==1:  
     signup()
    elif ip==2:
       login()
    else:
       print("invalid input")
start()
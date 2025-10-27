import json
from auth import signUp


def start():
    print("1. Signup\n2. Login")
    ip = int(input("Enter choice: "))
    if ip == 1:
        signUp()
    elif ip == 2:
        print("Login function not added yet.")
    else:
        print("Invalid input")

start()

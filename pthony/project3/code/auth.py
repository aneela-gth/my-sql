import json
import random

def signup():
    with open("../data/data.json","r")as f:
        username=input("enter username:")
        email=input("enter email:")
        password=input("enter pasword:")
        user_id=generateuserId(username)
        user_info={
            "user-id":user_id,
            "username":username,
            "email":password
        }
        print(f"ur userid is{user_id}")
        users=json.load(f)
        users["users"].append()
    with open("../data/data.json","w")as f:
        json.dump(users,f)
        print("signup is done")

def generateuserId(username):
    user_id=username[0:3]+str(random.randint(9999,99999))
    return user_id
def login():
    user=input("entear username or email")
    password=input("enter password")

    with open("../data/duser_infoata.json","r")as f:
        users_data=json.load(f)
        user_info=users_data["users"]
        for x in user_info:
            if ((user==x["user_id"]) or(user==x["email"])and password==x["password"]):
                print('login sucessfull')
            else:
                print("invalid credentials")
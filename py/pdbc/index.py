import mysql.connector
from db import info
try:
  mysql.connector.connect(**info)
  print('connection succesfull')
except:
  print('not able to connect')




try:
    age=int(input('enter age:'))
    if age<18:
        raise ValueError('childrens are not allowed')
    else:
         print("welocome to the  53r")
except ValueError as e:
       print(e)
except:
     print("unexpected error")






   
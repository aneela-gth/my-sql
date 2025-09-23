import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection suceesful')
except:
    print('not able to connect')
cursor=conn.cursor()

# to create database
query='create database if not exists instagram_data'
cursor.execute(query)

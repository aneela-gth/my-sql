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

# using/selecting databases

cursor.execute('use instagram_data')

#create a table name,email,postes,likes

try:
    create_table_query="""create table  if not exists users_info(name varchar(50),email varchar(50),postes int,likes int);""" 
    cursor.execute(create_table_query)
    print("table created")

except mysql.connector.errors.ProgrammingError as e:
    print(e)

# insert value
'''try:
    insert_data="""insert into users_info values ("aneelabandi","aneela@gmial.com",10,200)"""
    cursor.execute(insert_data)
    print("value inserted")
except:
    print("something went wrong")'''

# insert stngle row of data
'''try:
    data=("naresh","nari@gmail.com",20,500)
    insert_data="""insert into users_info(name,email,postes,likes)values(%s,%s,%s,%s)"""
    cursor.execute(insert_data,data)
    print("data inserted")
except:
    print("someting went worng")
'''

#insert single row using function

'''def insert_single_row(data):
    try:
        insert_data="""insert into users_info(name,email,postes,likes) values(%s,%s,%s,%s)"""
        cursor.execute(insert_data,data)
        print("values inserted")
    except:
        print("something went wrong")
insert_single_row(("akhila","akhi@gmail",15,200))
'''

#insert values input from the user
'''def insert_values(data):
    try:
        insert_data="""insert into users_info (name,email,postes,likes) values(%s,%s,%s,%s)"""
        cursor.execute(insert_data,data)
        print("values inserted")
    except:
        print("something went wrong")
insert_values(((input("enter name:")),(input("enter email:")),(input("enter postes"),(input("enter likes")))))'''

#inserting multiple values using function
'''def insert_values(data):
    try:
        insert_values="""insert into users_info (name,email,posteS,likes) values(%s,%s,%s,%s)"""
        cursor.executemany(insert_values,data)
        print("values inserted....")
    except:
        print("something went wrong")
insert_values([("raju","raju@gmail.com",30,400),
               ("rambabau","ram@gmail.com",28,300),
               ("anusha","anu@gmila.com",12,280),
               ("usha","uaha@gmial.com",24,500)])'''

# get all recods

'''def get_records():
    try:
        get_query="""select * from users_info"""
        cursor.execute(get_query)
        results=cursor.fetchall()
        print("all records in users_info:")
        for row in results:
            print(row)
    except:
          print("something went wrong")
get_records()


'''

# get records using posts

'''def get_records_using_posts(data):
    try:
        get_query="""select * from users_info where postes=%s"""
        cursor.execute(get_query,(data,))
        results=cursor.fetchall()
        print("geting records using postes:")
        for row in results:
            print(row)
    except  Exception as e:
       print("something went wrong:",e)

get_records_using_posts(20)'''

# updating id_name using email       

'''def update_name_by_email(new_name,email):
    try:
        update_query="""update users_info set name =%s where email=%s"""
        cursor.execute(update_query,(new_name,email))
        print("updated successfully....")
    except:
        print("something went wrong")
update_name_by_email("aneela","aneela@gmail.com")
'''

# upadating posts count using name

'''def update_posta_by_name(postes,name):
    try:
        update_query="""update insta_users set postes=posts+%s where name=%s"""
        cursor.execute(update_query,(postes,name))
        print("updated successfully....")
    except:
        print("something went wrong")
updat_posts_by_name("aneelabandi")

'''


cursor.execute(query)
conn.commit()
conn.close()



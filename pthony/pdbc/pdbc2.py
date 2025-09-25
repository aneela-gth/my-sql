import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print("connection successful")
except:
    print("not able not connect")

cursor=conn.cursor()

#to create database

query="CREATE DATABASE if not exists instagram_db"
# print("database created successfully!")

#use database

cursor.execute("use instagram_db")


#create a table insta_users with id_name, email,mobil_no,posts,likes,comments

''


# inserting single value

try:
    data=(1,"aneela","aneelabandi@gmail.com",7674087691,10,150,200)
    insert_query="""insert into insta_users(s_no,id_name,email,mobile_no,posts,likes,comments) values (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(insert_query,data)
    print("value inserted...")
except:
    print("something went wrong")



# inserting multiple values using function

def insert_values(data):
    try:
        insert_query="""insert into insta_users(id_name,email,mobile_no,posts,likes,comments) values (%s,%s,%s,%s,%s,%s)"""
        cursor.executemany(insert_query,data)
        print("values inserted.....")
    except:
        print("something went wrong")
# insert_values([("dad_callme_hari","hari@gmail.com",8897250915,15,300,200),("mr_shannu","shannu@gmail.com",9988774455,150,1000,500),("tharun_nani","nani@gmail.com",9966554488,200,1200,550),("rupani_sreevani","sree@gmail.com",6655449988,100,200,15),("sujana_yata","suppu@gmail.com",9955663322,50,150,10)])
# insert_values([("aneeela_bandi","anee@gmail.com",8855669944,20,150,0),("maggie","meghana@gmail.com",8877445566,1,100,1),("kante_nirosha","niru@gmail.com",8877994455,200,300,15),("navi_naveen","navi@gmail.com",7744556611,150,400,50),("its_me_sathi","sathi@gmail.com",7744556622,2,150,20),("akhil_akhi","akhi@gmail.com",7788332211,500,550,100)])

insert_values([("sushi_dancer","suchi@gmail.com",8521479632,1500,1000,1000),("solo_king","naga@gmail.com",9632587441,100,400,200),("urs_truly_bharath","chandu@gmail.com",8856974122,1200,1000,120)])
    

# get all records

def get_records():
    try:
        get_query="""select * from insta_users"""
        cursor.execute(get_query)
        results=cursor.fetchall()
        print("All records in insta_users:")
        for row in results:
            print(row)
    except:
        print("something went wrong")
get_records()


#get records using posts


def get_records_using_posts(data):
    try:
        get_query="""select * from insta_users where posts=%s"""
        cursor.execute(get_query,(data,))
        results=cursor.fetchall()
        print("Getting records using posts:")
        for row in results:
            print(row)
    except:
        print("something went wrong")
# get_records_using_posts(150)
# get_records_using_posts(100)
get_records_using_posts(2)


#updating id_name using email

def update_id_by_email(new_id_name,email):
    try:
        update_query="""update insta_users set id_name =%s where email=%s"""
        cursor.execute(update_query,(new_id_name,email))
        print("updated successfully....")
    except:
        print("something went wrong")
update_id_by_email("sharanya_katukuri","sharanya@gmail.com")



#updating posts count usind id_name

def update_posts_by_idname(posts,id_name):
    try:
        update_query="""update insta_users set posts=posts+%s where id_name=%s"""
        cursor.execute(update_query,(posts,id_name))
        print("updated successfully....")
    except:
        print("something went wrong")
update_posts_by_idname(124,"sharanya_katukuri")



#get limited recors 

def get_limited_records(limit):
    try:
        query="""select * from insta_users limit %s"""
        cursor.execute(query,(limit,))
        results=cursor.fetchall()
        print("Records:")
        for row in results:
            print(row)
    except:
        print("something went wrong")

# get_limited_records(5)
get_limited_records(10)


#get records by order 

def get_records_order():
    try:
        query="""select * from insta_users order by id_name asc"""
        cursor.execute(query)
        results=cursor.fetchall()
        print("Get all records  by id_name in asc order")
        for row in results:
            print(row)
    except:
        print("something went wrong")

get_records_order()


# delete record using id_name

def delete_recors_by_idname(id_name):
    try:
        query="""delete from insta_users where id_name=%s"""
        cursor.execute(query,(id_name,))
        print("record deleted successfully!!!!")
    except:
        print("something went wrong")

delete_recors_by_idname("sushi_dancer")


#delete record using posts


def delete_record_by_posts(posts):
    try:
        query="""delete from insta_users where posts=%s"""
        cursor.execute(query,(posts,))
        print("delete record successfully......")
    except:
        print("something went wrong")
delete_record_by_posts(500)


#delete record by comments


def delete_record_by_comments(comments):
    try:
        query="""delete from insta_users where comments=%s"""
        cursor.execute(query,(comments,))
        print("record deleted successfully......")
    except:
        print("something went wrong")
delete_record_by_comments(15) 


#delete all records 


def delete_all_records():
    try:
        query="""truncate table insta_users"""
        cursor.execute(query)
        print("deleted all records")
    except:
        print("something went wrong")
delete_all_records()

cursor.execute(query)
conn.commit()
conn.close()

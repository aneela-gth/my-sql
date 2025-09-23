# import mysql.connector
# from db import info

# try:
#     conn=mysql.connector.connect(**info)
#     print('connection successful')
# except:
#     print('not able to connect')
# cursor=conn.cursor()

# #to create database
# query='create database if not exists 10000coders'
# cursor.execute(query)
# #using/selecting databases
# cursor.execute('use 10000coders')

# #creating a tbale withe id,name,eamil,course,join_date
# try:
#     create_table="""create table if not exists students(
#     id int auto_increment primary key,name varchar(100),
#     email varchar(100),course varchar(100),joined_date date );"""
#     cursor.execute(create_table)
#     print('table created successfully')
# except mysql.connector.errors.ProgrammingError as e:
#    print(e)
#    #insert single row of data
# def insertsinglerow(data):
#         try:
#           insertdata=""" insert into students (name,eamil,course,joined_date)values(%s,%s,%s,%s) """
#           cursor.execute(insertdata,data)
#           print()
#         except:
#           print('something went wrong')
# insertsinglerow(('raju','raju@gmail.com','PFC','2025-03-05'))
# insertsinglerow(('naresh','nari@gamil.com','PFS','2025-06-05'))
# insertsinglerow((input('enter name:'),input('enter emil:'),input('enter course'),input('enter joined date')))



# # insert multipe rows at atime
# def insermultiplerows(data):
#     try:
       
#         insertquery="""insert into students (name,email,course,joined_date) values(%s,%s,%s,%s)"""
#         cursor.executemany(insertquery,data)
#         print("multiple rows inserted")
#     except:
#        print('something went wrong')

#        insermultiplerows([("shanu",'ahanu@gmail.com','web','2025-05-06'),
#           ('suppu','suppu@gmail.com','python','2025-05-06'),
#           ('nirosha','niru@gmail.com','python','2025-05-06')])
# def getrecordes():
#     try:
#         querry='select * from students'
#         cursor.execute(query)
#         results=cursor.fetchall()
#         for row in results:
#          print(row)
#     except:
#         print('errot occurred')
# def getstudentsbycourse( course_name):
#     try:
#         query=f'select * from students where courses={'couse_name'}'
#         cursor.execute(query)
#         results=cursor.fetchall()
#         print(results)
#     except:
#         print('something went wrong')

#     getstudentsbycourse('PFS')


# # getrecordes()
# conn.commit()
# cursor.close()
# conn.close()



import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print("connection successful")
except:
    print('not able to connect')

cursor=conn.cursor()    

#to create database
query='CREATE DATABASE if not exists 10Kc'
cursor.execute(query)
#using/selecting database
cursor.execute("use 10kc")

#creating a table
try:
    create_table="""create table if not exists students_new(
    id int auto_increment primary key,name varchar(100),email varchar(100),
    course varchar(100),joined_date date);"""
    cursor.execute(create_table)
    print("table created successfully")
except :
    print("something went wrong")

# try:
#     insertdata=""" insert into students_new values (1,"chinnu","chandu@gmail.com","pfs","2025-02-06")"""
#     cursor.execute(insertdata)
# except:
#     print("something went wrong")  
  
#insert single row of data
# def insertsinglerow(data):
#     try:
#         insertdata=""" insert into students_new (name,email,course,joined_date) values(%s,%s,%s,%s)"""
#         cursor.execute(insertdata,data)
#         print("data inserted")
#     except:
#         print("something went wrong")    
# insertsinglerow(("sujana","sujana@gmail.com","pfs","2025-09-05"))
# insertsinglerow(("puppy","puppy@gmail.com","pfs","2025-07-08"))
# insertsinglerow((input("enter name:"),input(("enter email:"),input("enter course"),input("enter joined date"))))

#insert multiple rows at a time

# try:
#     data=[("shannu","shannu@gmail.com","pfs","2025-04-04"),
#           ("maggie","maggie@gmail.com","pfs","2025-08-02"),
#           ("chitti","chitti@gmail.com","pfs","2025-09-04")]
#     insertquery="""insert into students_new (name,email,course,joined_date) values (%s,%s,%s,%s)"""
#     cursor.executemany(insertquery,data)
# except:
#     print("something went wrong")    
#getting all records
# def getrecords():
#     try:
#         query="select * from students_new"
#         cursor.execute(query)
#         results=cursor.fetchall()
#         for row in results:
#             print(row)
#     except:
#         print("error occured")    
# getrecords()
#getting records by course name
# def getstudentsbycourse(course_name):
#     try:
#         query="""select * from students_new where course= %s"""
#         print(query)
#         cursor.execute(query,(course_name,))
#         results=cursor.fetchall()
#         # print(results)
#         for x in results:
#             print(x)
#     except:
#         print("something wrong")
# getstudentsbycourse("jfs")

#updating email
# def updatestudentemail(student_id, new_email):
#     try:
#         query = """UPDATE students_new 
#                    SET email = %s 
#                    WHERE id = %s"""
#         cursor.execute(query, (new_email, student_id))
#         print(f"Student ID {student_id} email updated to {new_email}")
#     except Exception as e:
#         print("Something went wrong:", e)

# updatestudentemail(1, "abcd@gmail.com")

#deleting a record by email

# def deletestudentbyemail(email):
#     try:
#         query = """DELETE FROM students_new WHERE email = %s"""
#         cursor.execute(query, (email,))
#         conn.commit() 
#         print(f"Record with email {email} deleted successfully.")
#     except Exception as e:
#         print("Something went wrong:", e)

# deletestudentbyemail("suppu@gmail.com")
# deletestudentbyemail("shannu@gmail.com")

#deting a record by name

# def deletestudentbyname(name):
#     try:
#         query = """DELETE FROM students_new WHERE name = %s"""
#         cursor.execute(query, (name,))
#         # conn.commit() 
#         print(f"Record with name {name} deleted successfully.")
#     except Exception as e:
#         print("Something went wrong:", e)

# deletestudentbyname("maggie")
# deletestudentbyname("soumya")


#delete multiple records by cource
# def deleterecordsbycource(course):
#     try:
#         query = """DELETE FROM students_new WHERE course = %s"""
#         cursor.execute(query, (course,))
#         # conn.commit() 
#         print(f"Record with course {course} deleted successfully.")
#     except:
#         print("Something went wrong")
# deleterecordsbycource("jfs")

# def updatecouresbyemail(course,email):
#     try:
#         query="""update students set course=%s where email=%s"""
#         cursor.execute(query,(course,email))
#         print("data update succefully")
#     except:
#         print("something went wrong")
# updatecouresbyemail('PFS','abc@gmail.com')
# def updatenameandcoursebyemail(new_name,new_course,email):
#     try:
#         query="""update students set name=%s,coues=%s,email=%s"""
#         cursor.execute(query,(new_name,new_course,email))
#         print("record is update")
#     except:
#         print("somethng went wrong")
#     updatenameandcoursebyemail('aneela','web','aneela@gmail.com')







conn.commit()
cursor.close()
conn.close()
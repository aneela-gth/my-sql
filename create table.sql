Copyright (c) 2016, 2025, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
 MySQL  JS > \sql
Switching to SQL mode... Commands end with ;
 MySQL  SQL > \c root@localhost
Creating a session to 'root@localhost'
Fetching global names for auto-completion... Press ^C to stop.
Your MySQL connection id is 19 (X protocol)
Server version: 8.0.43 MySQL Community Server - GPL
No default schema selected; type \use <schema> to set one.
 MySQL  localhost:33060+ ssl  SQL > show databases;
+--------------------+
| Database           |
+--------------------+
| 10k                |
| 53r                |
| 53rr               |
| akhi               |
| aneela             |
| information_schema |
| jntu               |
| mysql              |
| nani               |
| new53r             |
| performance_schema |
| sys                |
+--------------------+
12 rows in set (0.0022 sec)
 MySQL  localhost:33060+ ssl  SQL > use 10k;
Default schema set to `10k`.
Fetching global names, object names from `10k` for auto-completion... Press ^C to stop.
 MySQL  localhost:33060+ ssl  10k  SQL > show tables;
+------------------+
| Tables_in_10k    |
+------------------+
| college_students |
| customer         |
| emp              |
+------------------+
3 rows in set (0.0041 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > create table students (id int primary key auto_increment,name varchar(50) not null,email varchar(50) unique,age int check(age>=18),city varchar(50) default 'hyderabad');
Query OK, 0 rows affected (0.0929 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > insert into students (id,name,email,age) values (101,'aneela','anee@123gmail',23);
Query OK, 1 row affected (0.0176 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > insert into students (id,name,email,age) values (102,'suppu','suppu657gmail',22);
Query OK, 1 row affected (0.0321 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > insert into students (id,name,email,age) values (103,'sharanya','sharanya4101gmail',21);
Query OK, 1 row affected (0.0133 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > insert into students (id,name,email,age) values (104,'sreevani','sri989gmail',20);
Query OK, 1 row affected (0.0311 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > insert into students (id,name,email,age) values (105,'shanu','shanu7674gmail',19);
Query OK, 1 row affected (0.0161 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > select * from students;
+-----+----------+-------------------+-----+-----------+
| id  | name     | email             | age | city      |
+-----+----------+-------------------+-----+-----------+
| 101 | aneela   | anee@123gmail     |  23 | hyderabad |
| 102 | suppu    | suppu657gmail     |  22 | hyderabad |
| 103 | sharanya | sharanya4101gmail |  21 | hyderabad |
| 104 | sreevani | sri989gmail       |  20 | hyderabad |
| 105 | shanu    | shanu7674gmail    |  19 | hyderabad |
+-----+----------+-------------------+-----+-----------+
5 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > alter table students add column phone int unique;
Query OK, 0 rows affected (0.1521 sec)

Records: 0  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  10k  SQL > select * from students;
+-----+----------+-------------------+-----+-----------+-------+
| id  | name     | email             | age | city      | phone |
+-----+----------+-------------------+-----+-----------+-------+
| 101 | aneela   | anee@123gmail     |  23 | hyderabad |  NULL |
| 102 | suppu    | suppu657gmail     |  22 | hyderabad |  NULL |
| 103 | sharanya | sharanya4101gmail |  21 | hyderabad |  NULL |
| 104 | sreevani | sri989gmail       |  20 | hyderabad |  NULL |
| 105 | shanu    | shanu7674gmail    |  19 | hyderabad |  NULL |
+-----+----------+-------------------+-----+-----------+-------+
5 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > alter table students modify column age smallint;
Query OK, 5 rows affected (0.1384 sec)

Records: 5  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  10k  SQL > select * from students;
+-----+----------+-------------------+-----+-----------+-------+
| id  | name     | email             | age | city      | phone |
+-----+----------+-------------------+-----+-----------+-------+
| 101 | aneela   | anee@123gmail     |  23 | hyderabad |  NULL |
| 102 | suppu    | suppu657gmail     |  22 | hyderabad |  NULL |
| 103 | sharanya | sharanya4101gmail |  21 | hyderabad |  NULL |
| 104 | sreevani | sri989gmail       |  20 | hyderabad |  NULL |
| 105 | shanu    | shanu7674gmail    |  19 | hyderabad |  NULL |
+-----+----------+-------------------+-----+-----------+-------+
5 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > alter table students drop column city;
Query OK, 0 rows affected (0.0449 sec)

Records: 0  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  10k  SQL > select * from students;
+-----+----------+-------------------+-----+-------+
| id  | name     | email             | age | phone |
+-----+----------+-------------------+-----+-------+
| 101 | aneela   | anee@123gmail     |  23 |  NULL |
| 102 | suppu    | suppu657gmail     |  22 |  NULL |
| 103 | sharanya | sharanya4101gmail |  21 |  NULL |
| 104 | sreevani | sri989gmail       |  20 |  NULL |
| 105 | shanu    | shanu7674gmail    |  19 |  NULL |
+-----+----------+-------------------+-----+-------+
5 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  10k  SQL > insert into students (id,name,email,age) values (106,'nani','shanu7674gmail',18);
ERROR: 1062: Duplicate entry 'shanu7674gmail' for key 'students.email'
 MySQL  localhost:33060+ ssl  10k  SQL >












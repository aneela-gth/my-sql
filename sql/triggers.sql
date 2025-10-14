MySQL Shell 8.0.43

Copyright (c) 2016, 2025, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
 MySQL  JS > \sql
Switching to SQL mode... Commands end with ;
 MySQL  SQL > \c root@localhost
Creating a session to 'root@localhost'
Fetching global names for auto-completion... Press ^C to stop.
Your MySQL connection id is 26 (X protocol)
Server version: 8.0.43 MySQL Community Server - GPL
No default schema selected; type \use <schema> to set one.
 MySQL  localhost:33060+ ssl  SQL > show databases;
+--------------------+
| Database           |
+--------------------+
| 10000coders        |
| 10k                |
| 10kc               |
| 53r                |
| 53rr               |
| akhi               |
| aneela             |
| information_schema |
| instagram_data     |
| jntu               |
| mysql              |
| nani               |
| new53r             |
| performance_schema |
| sys                |
| trig               |
+--------------------+
16 rows in set (0.0024 sec)
 MySQL  localhost:33060+ ssl  SQL > use trig;
Default schema set to `trig`.
Fetching global names, object names from `trig` for auto-completion... Press ^C to stop.
 MySQL  localhost:33060+ ssl  trig  SQL > CREATE TABLE dept(
                                       -> deptno INT PRIMARY KEY,
                                       -> DNAME VARCHAR(20),
                                       -> loc VARCHAR(20)
                                       -> );
Query OK, 0 rows affected (0.1033 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO dept (deptno, dname, loc) VALUES (10, 'ACCOUNTING', 'NEW YORK');
Query OK, 1 row affected (0.0366 sec)
 MySQL  localhost:33060+ ssl  trig  SQL >  INSERT INTO dept (deptno, dname, loc) VALUES (20, 'RESEARCH', 'DALLAS');
Query OK, 1 row affected (0.0111 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO dept (deptno, dname, loc) VALUES (30, 'SALES', 'CHICAGO');
Query OK, 1 row affected (0.0295 sec)
 MySQL  localhost:33060+ ssl  trig  SQL >  INSERT INTO dept (deptno, dname, loc) VALUES (40, 'OPERATIONS', 'BOSTON');
Query OK, 1 row affected (0.0054 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > CREATE TABLE emp(
                                       -> empno INT PRIMARY KEY,
                                       -> ename VARCHAR(20),
                                       -> job VARCHAR(20),
                                       -> mgr INT,
                                       -> hiredate DATE,
                                       -> sal DECIMAL(10,2),
                                       -> comm DECIMAL(10,2),
                                       -> deptno INT,
                                       -> FOREIGN KEY (deptno) REFERENCES dept(deptno)
                                       -> );
Query OK, 0 rows affected (0.1271 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20);
Query OK, 1 row affected (0.0346 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30);
Query OK, 1 row affected (0.0311 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30);
Query OK, 1 row affected (0.0327 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, NULL, 20);
Query OK, 1 row affected (0.0301 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30);
Query OK, 1 row affected (0.0343 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850, NULL, 30);
Query OK, 1 row affected (0.0324 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, NULL, 10);
Query OK, 1 row affected (0.0298 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19', 3000, NULL, 20);
Query OK, 1 row affected (0.0131 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17', 5000, NULL, 10);
Query OK, 1 row affected (0.0074 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500, 0, 30);
Query OK, 1 row affected (0.0316 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23', 1100, NULL, 20);
Query OK, 1 row affected (0.0098 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950, NULL, 30);
Query OK, 1 row affected (0.0295 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000, NULL, 20);
Query OK, 1 row affected (0.0300 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, NULL, 10);
Query OK, 1 row affected (0.0289 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > select * from dept;
+--------+------------+----------+
| deptno | DNAME      | loc      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | SALES      | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
4 rows in set (0.0027 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > select  * from emp;
+-------+--------+-----------+------+------------+---------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal     | comm    | deptno |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
14 rows in set (0.0023 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > create table info_trigger
                                       -> (id int auto_increment primary key,
                                       -> ev_type varchar(60),
                                       -> info varchar(60),
                                       -> log_time timestamp default current_timestamp);
Query OK, 0 rows affected (0.0783 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > desc info_trigger;
+----------+-------------+------+-----+-------------------+-------------------+
| Field    | Type        | Null | Key | Default           | Extra             |
+----------+-------------+------+-----+-------------------+-------------------+
| id       | int         | NO   | PRI | NULL              | auto_increment    |
| ev_type  | varchar(60) | YES  |     | NULL              |                   |
| info     | varchar(60) | YES  |     | NULL              |                   |
| log_time | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+----------+-------------+------+-----+-------------------+-------------------+
4 rows in set (0.0048 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter $$
 MySQL  localhost:33060+ ssl  trig  SQL > create trigger insert_into
                                       -> before insert on emp
                                       -> for each row
                                       -> begin
                                       -> set new.ename=trim(new.ename);
                                       -> insert into info_trigger(ev_type,info)
                                       -> values ('before insert on emp', concat
                                       -> ('ename=',new.ename));
                                       -> end $$
Query OK, 0 rows affected (0.0443 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter;
ERROR: DELIMITER must be followed by a 'delimiter' character or string
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter ;
 MySQL  localhost:33060+ ssl  trig  SQL > insert into emp(empno,ename) values (1234,'  aneela  ');
Query OK, 1 row affected (0.0381 sec)
 MySQL  localhost:33060+ ssl  trig  SQL >  select * from emp;
+-------+--------+-----------+------+------------+---------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal     | comm    | deptno |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  1234 | aneela | NULL      | NULL | NULL       |    NULL |    NULL |   NULL |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
15 rows in set (0.0011 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > select * from info_trigger;
+----+----------------------+--------------+---------------------+
| id | ev_type              | info         | log_time            |
+----+----------------------+--------------+---------------------+
|  1 | before insert on emp | ename=aneela | 2025-10-13 09:50:36 |
+----+----------------------+--------------+---------------------+
1 row in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter $$
 MySQL  localhost:33060+ ssl  trig  SQL > create trigger after_insert
                                       -> after insert on emp
                                       -> for each row
                                       ->  begin
                                       -> insert into info_trigger (ev_type,info) values
                                       ->  ('after insert on emp', concat('empno=',new.empno,'ename=',new.ename));
                                       -> end$$
Query OK, 0 rows affected (0.0393 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter ;
 MySQL  localhost:33060+ ssl  trig  SQL > insert into emp(empno,ename) values (4321,'harish');
Query OK, 1 row affected (0.0087 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > select * from emp;
+-------+--------+-----------+------+------------+---------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal     | comm    | deptno |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  1234 | aneela | NULL      | NULL | NULL       |    NULL |    NULL |   NULL |
|  4321 | harish | NULL      | NULL | NULL       |    NULL |    NULL |   NULL |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
16 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  trig  SQL >  select * from info_trigger;
+----+----------------------+------------------------+---------------------+
| id | ev_type              | info                   | log_time            |
+----+----------------------+------------------------+---------------------+
|  1 | before insert on emp | ename=aneela           | 2025-10-13 09:50:36 |
|  2 | before insert on emp | ename=harish           | 2025-10-13 09:53:49 |
|  3 | after insert on emp  | empno=4321ename=harish | 2025-10-13 09:53:49 |
+----+----------------------+------------------------+---------------------+
3 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter $$
 MySQL  localhost:33060+ ssl  trig  SQL > create trigger be_update
                                       -> before update on emp
                                       -> for each row
                                       -> begin
                                       -> if new.sal < (old.sal *0.5) then
                                       -> signal sqlstate '45000'
                                       -> set message_text='erroe: salary reduction cannot exceed 50%';
                                       ->  end if;
                                       -> end $$
Query OK, 0 rows affected (0.0404 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter ;
 MySQL  localhost:33060+ ssl  trig  SQL > update emp set sal=100 where ename='smith';
ERROR: 1644: erroe: salary reduction cannot exceed 50%
 MySQL  localhost:33060+ ssl  trig  SQL > update emp set sal=500 where ename='smith';
Query OK, 1 row affected (0.0315 sec)

Rows matched: 1  Changed: 1  Warnings: 0
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter $$
 MySQL  localhost:33060+ ssl  trig  SQL > create trigger after_update
                                       -> after update on emp
                                       ->  for each row
                                       ->  begin
                                       ->   insert into info_trigger(ev_type,info) values
                                       ->  ('after update on emp', concat('oldsal=',old.sal,'newsal=',new.sal));
                                       ->  end $$
Query OK, 0 rows affected (0.0232 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter ;
 MySQL  localhost:33060+ ssl  trig  SQL > select * from emp;
+-------+--------+-----------+------+------------+---------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal     | comm    | deptno |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  1234 | aneela | NULL      | NULL | NULL       |    NULL |    NULL |   NULL |
|  4321 | harish | NULL      | NULL | NULL       |    NULL |    NULL |   NULL |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  500.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
16 rows in set (0.0035 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > update emp set sal=sal+50 where ename='ward';
Query OK, 1 row affected (0.0114 sec)

Rows matched: 1  Changed: 1  Warnings: 0
 MySQL  localhost:33060+ ssl  trig  SQL >  select * from info_trigger;
+----+----------------------+------------------------------+---------------------+
| id | ev_type              | info                         | log_time            |
+----+----------------------+------------------------------+---------------------+
|  1 | before insert on emp | ename=aneela                 | 2025-10-13 09:50:36 |
|  2 | before insert on emp | ename=harish                 | 2025-10-13 09:53:49 |
|  3 | after insert on emp  | empno=4321ename=harish       | 2025-10-13 09:53:49 |
|  4 | after update on emp  | oldsal=1250.00newsal=1300.00 | 2025-10-13 09:58:59 |
+----+----------------------+------------------------------+---------------------+
4 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > update emp set sal=25000 where ename='sharanya';
Query OK, 0 rows affected (0.0013 sec)

Rows matched: 0  Changed: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  trig  SQL > update emp set sal=10000 where ename='harish';
Query OK, 1 row affected (0.0312 sec)

Rows matched: 1  Changed: 1  Warnings: 0
 MySQL  localhost:33060+ ssl  trig  SQL >  select * from info_trigger;
+----+----------------------+------------------------------+---------------------+
| id | ev_type              | info                         | log_time            |
+----+----------------------+------------------------------+---------------------+
|  1 | before insert on emp | ename=aneela                 | 2025-10-13 09:50:36 |
|  2 | before insert on emp | ename=harish                 | 2025-10-13 09:53:49 |
|  3 | after insert on emp  | empno=4321ename=harish       | 2025-10-13 09:53:49 |
|  4 | after update on emp  | oldsal=1250.00newsal=1300.00 | 2025-10-13 09:58:59 |
|  5 | after update on emp  | NULL                         | 2025-10-13 09:59:28 |
+----+----------------------+------------------------------+---------------------+
5 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter $$
 MySQL  localhost:33060+ ssl  trig  SQL > create trigger be_delete
                                       -> before delete on emp
                                       -> for each row
                                       ->  begin
                                       -> if old.sal>20000 then
                                       -> signal sqlstate '45000'
                                       ->  set message_text= 'error: u cant delete an emplyoee with salary > 20000';
                                       -> end if;
                                       -> end$$
Query OK, 0 rows affected (0.0412 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delimiter ;
 MySQL  localhost:33060+ ssl  trig  SQL > delete from emp where ename='sharanya';
Query OK, 0 rows affected (0.0037 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > delete from emp where ename='harish';
Query OK, 1 row affected (0.0326 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > select * from emp;
+-------+--------+-----------+------+------------+---------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal     | comm    | deptno |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  1234 | aneela | NULL      | NULL | NULL       |    NULL |    NULL |   NULL |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  500.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1300.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
15 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > select * from info_trigger;
+----+----------------------+------------------------------+---------------------+
| id | ev_type              | info                         | log_time            |
+----+----------------------+------------------------------+---------------------+
|  1 | before insert on emp | ename=aneela                 | 2025-10-13 09:50:36 |
|  2 | before insert on emp | ename=harish                 | 2025-10-13 09:53:49 |
|  3 | after insert on emp  | empno=4321ename=harish       | 2025-10-13 09:53:49 |
|  4 | after update on emp  | oldsal=1250.00newsal=1300.00 | 2025-10-13 09:58:59 |
|  5 | after update on emp  | NULL                         | 2025-10-13 09:59:28 |
+----+----------------------+------------------------------+---------------------+
5 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  trig  SQL > show triggers;
+--------------+--------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------+----------------------+----------------------+--------------------+
| Trigger      | Event  | Table | Statement                                                                                                                                     | Timing | Created                | sql_mode                                                                                                              | Definer        | character_set_client | collation_connection | Database Collation |
+--------------+--------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------+----------------------+----------------------+--------------------+
| insert_into  | INSERT | emp   | begin
set new.ename=trim(new.ename);
insert into info_trigger(ev_type,info)
values ('before insert on emp', concat
('ename=',new.ename));
end | BEFORE | 2025-10-13 09:49:12.89 | ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES | root@localhost | utf8mb4              | utf8mb4_0900_ai_ci   | utf8mb4_0900_ai_ci |
| after_insert | INSERT | emp   | begin
insert into info_trigger (ev_type,info) values
 ('after insert on emp', concat('empno=',new.empno,'ename=',new.ename));
end             | AFTER  | 2025-10-13 09:53:32.32 | ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES | root@localhost | utf8mb4              | utf8mb4_0900_ai_ci   | utf8mb4_0900_ai_ci |
| be_update    | UPDATE | emp   | begin
if new.sal < (old.sal *0.5) then
signal sqlstate '45000'
set message_text='erroe: salary reduction cannot exceed 50%';
 end if;
end     | BEFORE | 2025-10-13 09:56:30.64 | ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES | root@localhost | utf8mb4              | utf8mb4_0900_ai_ci   | utf8mb4_0900_ai_ci |
| after_update | UPDATE | emp   | begin
  insert into info_trigger(ev_type,info) values
 ('after update on emp', concat('oldsal=',old.sal,'newsal=',new.sal));
 end             | AFTER  | 2025-10-13 09:58:29.01 | ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES | root@localhost | utf8mb4              | utf8mb4_0900_ai_ci   | utf8mb4_0900_ai_ci |
| be_delete    | DELETE | emp   | begin
if old.sal>20000 then
signal sqlstate '45000'
 set message_text= 'error: u cant delete an emplyoee with salary > 20000';
end if;
end    | BEFORE | 2025-10-13 10:00:55.02 | ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES | root@localhost | utf8mb4              | utf8mb4_0900_ai_ci   | utf8mb4_0900_ai_ci |
+--------------+--------+-------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------+------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------+----------------------+----------------------+--------------------+
5 rows in set (0.0049 sec)
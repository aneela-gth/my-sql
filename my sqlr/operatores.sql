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
Your MySQL connection id is 16 (X protocol)
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
+--------------------+
15 rows in set (0.0027 sec)
 MySQL  localhost:33060+ ssl  SQL > use aneela;
Default schema set to `aneela`.
Fetching global names, object names from `aneela` for auto-completion... Press ^C to stop.
 MySQL  localhost:33060+ ssl  aneela  SQL > show tables;
+------------------+
| Tables_in_aneela |
+------------------+
| dept             |
| emp              |
| employess        |
| info_trigger     |
| insert_before    |
| insert_info      |
| studentes        |
+------------------+
7 rows in set (0.0049 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp;
+-------+--------+-----------+------+------------+----------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal      | comm    | deptno |
+-------+--------+-----------+------+------------+----------+---------+--------+
|     1 | abcd   | clerk     | NULL | NULL       |     NULL |    NULL |   NULL |
|  1234 | ganesh | SAELMAN   | 7698 | 1981-02-22 | 12345.00 |  500.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 |  2975.00 |    NULL |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 |  1250.00 | 1400.00 |     20 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 |  2850.00 |    NULL |     30 |
|  7782 | raju   | MANAGER   | 7839 | 1981-06-09 |  2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1982-12-09 |  3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 30000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 |  1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1983-01-12 |  1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |   950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 |  3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 |  1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+----------+---------+--------+
13 rows in set (0.0568 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,job,sal,(sal+500) as increased_salary from emp;
+-------+--------+-----------+----------+------------------+
| empno | ename  | job       | sal      | increased_salary |
+-------+--------+-----------+----------+------------------+
|     1 | abcd   | clerk     |     NULL |             NULL |
|  1234 | ganesh | SAELMAN   | 12345.00 |         12845.00 |
|  7521 | WARD   | SALESMAN  |  2975.00 |          3475.00 |
|  7566 | JONES  | MANAGER   |  1250.00 |          1750.00 |
|  7698 | BLAKE  | MANAGER   |  2850.00 |          3350.00 |
|  7782 | raju   | MANAGER   |  2450.00 |          2950.00 |
|  7788 | SCOTT  | ANALYST   |  3000.00 |          3500.00 |
|  7839 | KING   | PRESIDENT | 30000.00 |         30500.00 |
|  7844 | TURNER | SALESMAN  |  1500.00 |          2000.00 |
|  7876 | ADAMS  | CLERK     |  1100.00 |          1600.00 |
|  7900 | JAMES  | CLERK     |   950.00 |          1450.00 |
|  7902 | FORD   | ANALYST   |  3000.00 |          3500.00 |
|  7934 | MILLER | CLERK     |  1300.00 |          1800.00 |
+-------+--------+-----------+----------+------------------+
13 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename as employee_salary,sal as original_salary,(sal*2) as double_salary from emp;
+-----------------+-----------------+---------------+
| employee_salary | original_salary | double_salary |
+-----------------+-----------------+---------------+
| abcd            |            NULL |          NULL |
| ganesh          |        12345.00 |      24690.00 |
| WARD            |         2975.00 |       5950.00 |
| JONES           |         1250.00 |       2500.00 |
| BLAKE           |         2850.00 |       5700.00 |
| raju            |         2450.00 |       4900.00 |
| SCOTT           |         3000.00 |       6000.00 |
| KING            |        30000.00 |      60000.00 |
| TURNER          |         1500.00 |       3000.00 |
| ADAMS           |         1100.00 |       2200.00 |
| JAMES           |          950.00 |       1900.00 |
| FORD            |         3000.00 |       6000.00 |
| MILLER          |         1300.00 |       2600.00 |
+-----------------+-----------------+---------------+
13 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal,comm from emp where comm>(0.1 * sal);
+-------+-------+---------+---------+
| empno | ename | sal     | comm    |
+-------+-------+---------+---------+
|  7566 | JONES | 1250.00 | 1400.00 |
+-------+-------+---------+---------+
1 row in set (0.0199 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal from emp where sal>(sal*12);
Empty set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select empno,ename,sal,(sal*12 ) as annual_salary from emp where (sal*12)>30000;
+-------+--------+----------+---------------+
| empno | ename  | sal      | annual_salary |
+-------+--------+----------+---------------+
|  1234 | ganesh | 12345.00 |     148140.00 |
|  7521 | WARD   |  2975.00 |      35700.00 |
|  7698 | BLAKE  |  2850.00 |      34200.00 |
|  7788 | SCOTT  |  3000.00 |      36000.00 |
|  7839 | KING   | 30000.00 |     360000.00 |
|  7902 | FORD   |  3000.00 |      36000.00 |
+-------+--------+----------+---------------+
6 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select ename,job,(sal+comm) as net_salary from emp;
+--------+-----------+------------+
| ename  | job       | net_salary |
+--------+-----------+------------+
| abcd   | clerk     |       NULL |
| ganesh | SAELMAN   |   12845.00 |
| WARD   | SALESMAN  |       NULL |
| JONES  | MANAGER   |    2650.00 |
| BLAKE  | MANAGER   |       NULL |
| raju   | MANAGER   |       NULL |
| SCOTT  | ANALYST   |       NULL |
| KING   | PRESIDENT |       NULL |
| TURNER | SALESMAN  |    1500.00 |
| ADAMS  | CLERK     |       NULL |
| JAMES  | CLERK     |       NULL |
| FORD   | ANALYST   |       NULL |
| MILLER | CLERK     |       NULL |
+--------+-----------+------------+
13 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job,(sal+coalesce(comm,0)) as net_income from emp;
+--------+-----------+------------+
| ename  | job       | net_income |
+--------+-----------+------------+
| abcd   | clerk     |       NULL |
| ganesh | SAELMAN   |   12845.00 |
| WARD   | SALESMAN  |    2975.00 |
| JONES  | MANAGER   |    2650.00 |
| BLAKE  | MANAGER   |    2850.00 |
| raju   | MANAGER   |    2450.00 |
| SCOTT  | ANALYST   |    3000.00 |
| KING   | PRESIDENT |   30000.00 |
| TURNER | SALESMAN  |    1500.00 |
| ADAMS  | CLERK     |    1100.00 |
| JAMES  | CLERK     |     950.00 |
| FORD   | ANALYST   |    3000.00 |
| MILLER | CLERK     |    1300.00 |
+--------+-----------+------------+
13 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select ename,sal from emp where sal=3000;
+-------+---------+
| ename | sal     |
+-------+---------+
| SCOTT | 3000.00 |
| FORD  | 3000.00 |
+-------+---------+
2 rows in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal>2500;
+--------+----------+
| ename  | sal      |
+--------+----------+
| ganesh | 12345.00 |
| WARD   |  2975.00 |
| BLAKE  |  2850.00 |
| SCOTT  |  3000.00 |
| KING   | 30000.00 |
| FORD   |  3000.00 |
+--------+----------+
6 rows in set (0.0010 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal between 1000 and 2000;
+--------+---------+
| ename  | sal     |
+--------+---------+
| JONES  | 1250.00 |
| TURNER | 1500.00 |
| ADAMS  | 1100.00 |
| MILLER | 1300.00 |
+--------+---------+
4 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,job from emp where job='manager';
+-------+-------+---------+
| empno | ename | job     |
+-------+-------+---------+
|  7566 | JONES | MANAGER |
|  7698 | BLAKE | MANAGER |
|  7782 | raju  | MANAGER |
+-------+-------+---------+
3 rows in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,hiredate from emp where hiredate>'1981-01-01';
+-------+--------+------------+
| empno | ename  | hiredate   |
+-------+--------+------------+
|  1234 | ganesh | 1981-02-22 |
|  7521 | WARD   | 1981-02-22 |
|  7566 | JONES  | 1981-04-02 |
|  7698 | BLAKE  | 1981-05-01 |
|  7782 | raju   | 1981-06-09 |
|  7788 | SCOTT  | 1982-12-09 |
|  7839 | KING   | 1981-11-17 |
|  7844 | TURNER | 1981-09-08 |
|  7876 | ADAMS  | 1983-01-12 |
|  7900 | JAMES  | 1981-12-03 |
|  7902 | FORD   | 1981-12-03 |
|  7934 | MILLER | 1982-01-23 |
+-------+--------+------------+
12 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job,sal from emp where job='clerk' and sal<1500;
+--------+-------+---------+
| ename  | job   | sal     |
+--------+-------+---------+
| ADAMS  | CLERK | 1100.00 |
| JAMES  | CLERK |  950.00 |
| MILLER | CLERK | 1300.00 |
+--------+-------+---------+
3 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,job from emp where job='salesman' or job='clerk';
+-------+--------+----------+
| empno | ename  | job      |
+-------+--------+----------+
|     1 | abcd   | clerk    |
|  7521 | WARD   | SALESMAN |
|  7844 | TURNER | SALESMAN |
|  7876 | ADAMS  | CLERK    |
|  7900 | JAMES  | CLERK    |
|  7934 | MILLER | CLERK    |
+-------+--------+----------+
6 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal,deptno from emp where sal between 1000 and 2000 and deptno=30;
+-------+--------+---------+--------+
| empno | ename  | sal     | deptno |
+-------+--------+---------+--------+
|  7844 | TURNER | 1500.00 |     30 |
+-------+--------+---------+--------+
1 row in set (0.0029 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename ,job from emp where job<>'MANAGER';
+-------+--------+-----------+
| empno | ename  | job       |
+-------+--------+-----------+
|     1 | abcd   | clerk     |
|  1234 | ganesh | SAELMAN   |
|  7521 | WARD   | SALESMAN  |
|  7788 | SCOTT  | ANALYST   |
|  7839 | KING   | PRESIDENT |
|  7844 | TURNER | SALESMAN  |
|  7876 | ADAMS  | CLERK     |
|  7900 | JAMES  | CLERK     |
|  7902 | FORD   | ANALYST   |
|  7934 | MILLER | CLERK     |
+-------+--------+-----------+
10 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal,comm from emp where comm is null;
+-------+--------+----------+------+
| empno | ename  | sal      | comm |
+-------+--------+----------+------+
|     1 | abcd   |     NULL | NULL |
|  7521 | WARD   |  2975.00 | NULL |
|  7698 | BLAKE  |  2850.00 | NULL |
|  7782 | raju   |  2450.00 | NULL |
|  7788 | SCOTT  |  3000.00 | NULL |
|  7839 | KING   | 30000.00 | NULL |
|  7876 | ADAMS  |  1100.00 | NULL |
|  7900 | JAMES  |   950.00 | NULL |
|  7902 | FORD   |  3000.00 | NULL |
|  7934 | MILLER |  1300.00 | NULL |
+-------+--------+----------+------+
10 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp where hiredate between '1981-01-01' and '1981-12-31';
+-------+--------+-----------+------+------------+----------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal      | comm    | deptno |
+-------+--------+-----------+------+------------+----------+---------+--------+
|  1234 | ganesh | SAELMAN   | 7698 | 1981-02-22 | 12345.00 |  500.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 |  2975.00 |    NULL |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 |  1250.00 | 1400.00 |     20 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 |  2850.00 |    NULL |     30 |
|  7782 | raju   | MANAGER   | 7839 | 1981-06-09 |  2450.00 |    NULL |     10 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 30000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 |  1500.00 |    0.00 |     30 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |   950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 |  3000.00 |    NULL |     20 |
+-------+--------+-----------+------+------------+----------+---------+--------+
9 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job,deptno from emp where deptno in(10,20,30);
+--------+-----------+--------+
| ename  | job       | deptno |
+--------+-----------+--------+
| ganesh | SAELMAN   |     30 |
| WARD   | SALESMAN  |     30 |
| JONES  | MANAGER   |     20 |
| BLAKE  | MANAGER   |     30 |
| raju   | MANAGER   |     10 |
| SCOTT  | ANALYST   |     20 |
| KING   | PRESIDENT |     10 |
| TURNER | SALESMAN  |     30 |
| ADAMS  | CLERK     |     20 |
| JAMES  | CLERK     |     30 |
| FORD   | ANALYST   |     20 |
| MILLER | CLERK     |     10 |
+--------+-----------+--------+
12 rows in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename from emp where ename like 'S%';
+-------+-------+
| empno | ename |
+-------+-------+
|  7788 | SCOTT |
+-------+-------+
1 row in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select empno,ename from emp where ename like '%N';
Empty set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename from emp where ename like '%A%';
+-------+--------+
| empno | ename  |
+-------+--------+
|     1 | abcd   |
|  1234 | ganesh |
|  7521 | WARD   |
|  7698 | BLAKE  |
|  7782 | raju   |
|  7876 | ADAMS  |
|  7900 | JAMES  |
+-------+--------+
7 rows in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,job,mgr from emp where mgr is null;
+-------+-------+-----------+------+
| empno | ename | job       | mgr  |
+-------+-------+-----------+------+
|     1 | abcd  | clerk     | NULL |
|  7839 | KING  | PRESIDENT | NULL |
+-------+-------+-----------+------+
2 rows in set (0.0011 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,job,sal,comm from emp where comm is null;
+-------+--------+-----------+----------+------+
| empno | ename  | job       | sal      | comm |
+-------+--------+-----------+----------+------+
|     1 | abcd   | clerk     |     NULL | NULL |
|  7521 | WARD   | SALESMAN  |  2975.00 | NULL |
|  7698 | BLAKE  | MANAGER   |  2850.00 | NULL |
|  7782 | raju   | MANAGER   |  2450.00 | NULL |
|  7788 | SCOTT  | ANALYST   |  3000.00 | NULL |
|  7839 | KING   | PRESIDENT | 30000.00 | NULL |
|  7876 | ADAMS  | CLERK     |  1100.00 | NULL |
|  7900 | JAMES  | CLERK     |   950.00 | NULL |
|  7902 | FORD   | ANALYST   |  3000.00 | NULL |
|  7934 | MILLER | CLERK     |  1300.00 | NULL |
+-------+--------+-----------+----------+------+
10 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select empno,ename,job,sal,comm from emp where comm is  not null;
+-------+--------+----------+----------+---------+
| empno | ename  | job      | sal      | comm    |
+-------+--------+----------+----------+---------+
|  1234 | ganesh | SAELMAN  | 12345.00 |  500.00 |
|  7566 | JONES  | MANAGER  |  1250.00 | 1400.00 |
|  7844 | TURNER | SALESMAN |  1500.00 |    0.00 |
+-------+--------+----------+----------+---------+
3 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job,sal from emp where sal is null;
+-------+-------+------+
| ename | job   | sal  |
+-------+-------+------+
| abcd  | clerk | NULL |
+-------+-------+------+
1 row in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select * from dept;
+--------+------------+----------+
| deptno | dname      | loc      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | developer  | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
4 rows in set (0.0282 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from dept where loc is null;
Empty set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job from emp where job like 'M%';
+-------+---------+
| ename | job     |
+-------+---------+
| JONES | MANAGER |
| BLAKE | MANAGER |
| raju  | MANAGER |
+-------+---------+
3 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename from emp where ename like'_____';
+-------+-------+
| empno | ename |
+-------+-------+
|  7566 | JONES |
|  7698 | BLAKE |
|  7788 | SCOTT |
|  7876 | ADAMS |
|  7900 | JAMES |
+-------+-------+
5 rows in set (0.0011 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp where job like '%MAN';
+-------+--------+----------+------+------------+----------+--------+--------+
| empno | ename  | job      | mgr  | hiredate   | sal      | comm   | deptno |
+-------+--------+----------+------+------------+----------+--------+--------+
|  1234 | ganesh | SAELMAN  | 7698 | 1981-02-22 | 12345.00 | 500.00 |     30 |
|  7521 | WARD   | SALESMAN | 7698 | 1981-02-22 |  2975.00 |   NULL |     30 |
|  7844 | TURNER | SALESMAN | 7698 | 1981-09-08 |  1500.00 |   0.00 |     30 |
+-------+--------+----------+------+------------+----------+--------+--------+
3 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp where ename like'%S';
+-------+-------+---------+------+------------+---------+---------+--------+
| empno | ename | job     | mgr  | hiredate   | sal     | comm    | deptno |
+-------+-------+---------+------+------------+---------+---------+--------+
|  7566 | JONES | MANAGER | 7839 | 1981-04-02 | 1250.00 | 1400.00 |     20 |
|  7876 | ADAMS | CLERK   | 7788 | 1983-01-12 | 1100.00 |    NULL |     20 |
|  7900 | JAMES | CLERK   | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
+-------+-------+---------+------+------------+---------+---------+--------+
3 rows in set (0.0012 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp where ename like'%AA%';
Empty set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp where ename like 'S%H';
Empty set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal,(sal*0.15) as bonus,(sal+(sal*0.15)) as total_salary from emp;
+-------+--------+----------+-----------+--------------+
| empno | ename  | sal      | bonus     | total_salary |
+-------+--------+----------+-----------+--------------+
|     1 | abcd   |     NULL |      NULL |         NULL |
|  1234 | ganesh | 12345.00 | 1851.7500 |   14196.7500 |
|  7521 | WARD   |  2975.00 |  446.2500 |    3421.2500 |
|  7566 | JONES  |  1250.00 |  187.5000 |    1437.5000 |
|  7698 | BLAKE  |  2850.00 |  427.5000 |    3277.5000 |
|  7782 | raju   |  2450.00 |  367.5000 |    2817.5000 |
|  7788 | SCOTT  |  3000.00 |  450.0000 |    3450.0000 |
|  7839 | KING   | 30000.00 | 4500.0000 |   34500.0000 |
|  7844 | TURNER |  1500.00 |  225.0000 |    1725.0000 |
|  7876 | ADAMS  |  1100.00 |  165.0000 |    1265.0000 |
|  7900 | JAMES  |   950.00 |  142.5000 |    1092.5000 |
|  7902 | FORD   |  3000.00 |  450.0000 |    3450.0000 |
|  7934 | MILLER |  1300.00 |  195.0000 |    1495.0000 |
+-------+--------+----------+-----------+--------------+
13 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal as salary_usd,(sal*83) as salary_inr from emp;
+-------+--------+------------+------------+
| empno | ename  | salary_usd | salary_inr |
+-------+--------+------------+------------+
|     1 | abcd   |       NULL |       NULL |
|  1234 | ganesh |   12345.00 | 1024635.00 |
|  7521 | WARD   |    2975.00 |  246925.00 |
|  7566 | JONES  |    1250.00 |  103750.00 |
|  7698 | BLAKE  |    2850.00 |  236550.00 |
|  7782 | raju   |    2450.00 |  203350.00 |
|  7788 | SCOTT  |    3000.00 |  249000.00 |
|  7839 | KING   |   30000.00 | 2490000.00 |
|  7844 | TURNER |    1500.00 |  124500.00 |
|  7876 | ADAMS  |    1100.00 |   91300.00 |
|  7900 | JAMES  |     950.00 |   78850.00 |
|  7902 | FORD   |    3000.00 |  249000.00 |
|  7934 | MILLER |    1300.00 |  107900.00 |
+-------+--------+------------+------------+
13 rows in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,job,sal,comm,(comm/sal) as comm_to_sal_ratio from emp where job='salesman';
+-------+--------+----------+---------+------+-------------------+
| empno | ename  | job      | sal     | comm | comm_to_sal_ratio |
+-------+--------+----------+---------+------+-------------------+
|  7521 | WARD   | SALESMAN | 2975.00 | NULL |              NULL |
|  7844 | TURNER | SALESMAN | 1500.00 | 0.00 |          0.000000 |
+-------+--------+----------+---------+------+-------------------+
2 rows in set (0.0025 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal as monthly_salary,(sal*12) as yearly_salary from emp;
+--------+----------------+---------------+
| ename  | monthly_salary | yearly_salary |
+--------+----------------+---------------+
| abcd   |           NULL |          NULL |
| ganesh |       12345.00 |     148140.00 |
| WARD   |        2975.00 |      35700.00 |
| JONES  |        1250.00 |      15000.00 |
| BLAKE  |        2850.00 |      34200.00 |
| raju   |        2450.00 |      29400.00 |
| SCOTT  |        3000.00 |      36000.00 |
| KING   |       30000.00 |     360000.00 |
| TURNER |        1500.00 |      18000.00 |
| ADAMS  |        1100.00 |      13200.00 |
| JAMES  |         950.00 |      11400.00 |
| FORD   |        3000.00 |      36000.00 |
| MILLER |        1300.00 |      15600.00 |
+--------+----------------+---------------+
13 rows in set (0.0019 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select empno,ename,sal,hiredate from emp where sal>1500 and year(hiredate)=1981;
+-------+--------+----------+------------+
| empno | ename  | sal      | hiredate   |
+-------+--------+----------+------------+
|  1234 | ganesh | 12345.00 | 1981-02-22 |
|  7521 | WARD   |  2975.00 | 1981-02-22 |
|  7698 | BLAKE  |  2850.00 | 1981-05-01 |
|  7782 | raju   |  2450.00 | 1981-06-09 |
|  7839 | KING   | 30000.00 | 1981-11-17 |
|  7902 | FORD   |  3000.00 | 1981-12-03 |
+-------+--------+----------+------------+
6 rows in set (0.0220 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp where job <>'CLERK' and sal>2000;
+-------+--------+-----------+------+------------+----------+--------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal      | comm   | deptno |
+-------+--------+-----------+------+------------+----------+--------+--------+
|  1234 | ganesh | SAELMAN   | 7698 | 1981-02-22 | 12345.00 | 500.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 |  2975.00 |   NULL |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 |  2850.00 |   NULL |     30 |
|  7782 | raju   | MANAGER   | 7839 | 1981-06-09 |  2450.00 |   NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1982-12-09 |  3000.00 |   NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 30000.00 |   NULL |     10 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 |  3000.00 |   NULL |     20 |
+-------+--------+-----------+------+------------+----------+--------+--------+
7 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select empno,ename,job,sal,comm from emp where comm is not null and sal<2000;
+-------+--------+----------+---------+---------+
| empno | ename  | job      | sal     | comm    |
+-------+--------+----------+---------+---------+
|  7566 | JONES  | MANAGER  | 1250.00 | 1400.00 |
|  7844 | TURNER | SALESMAN | 1500.00 |    0.00 |
+-------+--------+----------+---------+---------+
2 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select empno,ename,hiredate from emp where hiredate >'1981-12-12';
+-------+--------+------------+
| empno | ename  | hiredate   |
+-------+--------+------------+
|  7788 | SCOTT  | 1982-12-09 |
|  7876 | ADAMS  | 1983-01-12 |
|  7934 | MILLER | 1982-01-23 |
+-------+--------+------------+
3 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select empno,ename,deptno from emp where deptno in (10,20);
+-------+--------+--------+
| empno | ename  | deptno |
+-------+--------+--------+
|  7782 | raju   |     10 |
|  7839 | KING   |     10 |
|  7934 | MILLER |     10 |
|  7566 | JONES  |     20 |
|  7788 | SCOTT  |     20 |
|  7876 | ADAMS  |     20 |
|  7902 | FORD   |     20 |
+-------+--------+--------+
7 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >






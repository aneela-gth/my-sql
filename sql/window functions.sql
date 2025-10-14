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
Your MySQL connection id is 17 (X protocol)
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
15 rows in set (0.0252 sec)
 MySQL  localhost:33060+ ssl  SQL > use aneela;
Default schema set to `aneela`.
Fetching global names, object names from `aneela` for auto-completion... Press ^C to stop.
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
13 rows in set (0.0243 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select ename,sal,rank() over (order by sal desc) as salary_rank from emp;
+--------+----------+-------------+
| ename  | sal      | salary_rank |
+--------+----------+-------------+
| KING   | 30000.00 |           1 |
| ganesh | 12345.00 |           2 |
| SCOTT  |  3000.00 |           3 |
| FORD   |  3000.00 |           3 |
| WARD   |  2975.00 |           5 |
| BLAKE  |  2850.00 |           6 |
| raju   |  2450.00 |           7 |
| TURNER |  1500.00 |           8 |
| MILLER |  1300.00 |           9 |
| JONES  |  1250.00 |          10 |
| ADAMS  |  1100.00 |          11 |
| JAMES  |   950.00 |          12 |
| abcd   |     NULL |          13 |
+--------+----------+-------------+
13 rows in set (0.0308 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal,dense_rank() over (order by sal desc) as salary_rank from emp;
+--------+----------+-------------+
| ename  | sal      | salary_rank |
+--------+----------+-------------+
| KING   | 30000.00 |           1 |
| ganesh | 12345.00 |           2 |
| SCOTT  |  3000.00 |           3 |
| FORD   |  3000.00 |           3 |
| WARD   |  2975.00 |           4 |
| BLAKE  |  2850.00 |           5 |
| raju   |  2450.00 |           6 |
| TURNER |  1500.00 |           7 |
| MILLER |  1300.00 |           8 |
| JONES  |  1250.00 |           9 |
| ADAMS  |  1100.00 |          10 |
| JAMES  |   950.00 |          11 |
| abcd   |     NULL |          12 |
+--------+----------+-------------+
13 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal,dense_rank() over(partition by deptno order by sal desc) as dept_salary_rank from emp;
+--------+--------+----------+------------------+
| ename  | deptno | sal      | dept_salary_rank |
+--------+--------+----------+------------------+
| abcd   |   NULL |     NULL |                1 |
| KING   |     10 | 30000.00 |                1 |
| raju   |     10 |  2450.00 |                2 |
| MILLER |     10 |  1300.00 |                3 |
| SCOTT  |     20 |  3000.00 |                1 |
| FORD   |     20 |  3000.00 |                1 |
| JONES  |     20 |  1250.00 |                2 |
| ADAMS  |     20 |  1100.00 |                3 |
| ganesh |     30 | 12345.00 |                1 |
| WARD   |     30 |  2975.00 |                2 |
| BLAKE  |     30 |  2850.00 |                3 |
| TURNER |     30 |  1500.00 |                4 |
| JAMES  |     30 |   950.00 |                5 |
+--------+--------+----------+------------------+
13 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal,avg(sal) over (partition by deptno) as dept_avg_salary from emp;
+--------+--------+----------+-----------------+
| ename  | deptno | sal      | dept_avg_salary |
+--------+--------+----------+-----------------+
| abcd   |   NULL |     NULL |            NULL |
| raju   |     10 |  2450.00 |    11250.000000 |
| KING   |     10 | 30000.00 |    11250.000000 |
| MILLER |     10 |  1300.00 |    11250.000000 |
| JONES  |     20 |  1250.00 |     2087.500000 |
| SCOTT  |     20 |  3000.00 |     2087.500000 |
| ADAMS  |     20 |  1100.00 |     2087.500000 |
| FORD   |     20 |  3000.00 |     2087.500000 |
| ganesh |     30 | 12345.00 |     4124.000000 |
| WARD   |     30 |  2975.00 |     4124.000000 |
| BLAKE  |     30 |  2850.00 |     4124.000000 |
| TURNER |     30 |  1500.00 |     4124.000000 |
| JAMES  |     30 |   950.00 |     4124.000000 |
+--------+--------+----------+-----------------+
13 rows in set (0.0021 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal, max(sal) over (partition by deptno) as dept_max_salary from emp;
+--------+--------+----------+-----------------+
| ename  | deptno | sal      | dept_max_salary |
+--------+--------+----------+-----------------+
| abcd   |   NULL |     NULL |            NULL |
| raju   |     10 |  2450.00 |        30000.00 |
| KING   |     10 | 30000.00 |        30000.00 |
| MILLER |     10 |  1300.00 |        30000.00 |
| JONES  |     20 |  1250.00 |         3000.00 |
| SCOTT  |     20 |  3000.00 |         3000.00 |
| ADAMS  |     20 |  1100.00 |         3000.00 |
| FORD   |     20 |  3000.00 |         3000.00 |
| ganesh |     30 | 12345.00 |        12345.00 |
| WARD   |     30 |  2975.00 |        12345.00 |
| BLAKE  |     30 |  2850.00 |        12345.00 |
| TURNER |     30 |  1500.00 |        12345.00 |
| JAMES  |     30 |   950.00 |        12345.00 |
+--------+--------+----------+-----------------+
13 rows in set (0.0025 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select ename,sal,sum(sal) over (order by sal) as running_total from emp;
+--------+----------+---------------+
| ename  | sal      | running_total |
+--------+----------+---------------+
| abcd   |     NULL |          NULL |
| JAMES  |   950.00 |        950.00 |
| ADAMS  |  1100.00 |       2050.00 |
| JONES  |  1250.00 |       3300.00 |
| MILLER |  1300.00 |       4600.00 |
| TURNER |  1500.00 |       6100.00 |
| raju   |  2450.00 |       8550.00 |
| BLAKE  |  2850.00 |      11400.00 |
| WARD   |  2975.00 |      14375.00 |
| SCOTT  |  3000.00 |      20375.00 |
| FORD   |  3000.00 |      20375.00 |
| ganesh | 12345.00 |      32720.00 |
| KING   | 30000.00 |      62720.00 |
+--------+----------+---------------+
13 rows in set (0.0024 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal,sal-avg(sal) over (partition by deptno) as diff_from_dept_avg from emp;
+--------+--------+----------+--------------------+
| ename  | deptno | sal      | diff_from_dept_avg |
+--------+--------+----------+--------------------+
| abcd   |   NULL |     NULL |               NULL |
| raju   |     10 |  2450.00 |       -8800.000000 |
| KING   |     10 | 30000.00 |       18750.000000 |
| MILLER |     10 |  1300.00 |       -9950.000000 |
| JONES  |     20 |  1250.00 |        -837.500000 |
| SCOTT  |     20 |  3000.00 |         912.500000 |
| ADAMS  |     20 |  1100.00 |        -987.500000 |
| FORD   |     20 |  3000.00 |         912.500000 |
| ganesh |     30 | 12345.00 |        8221.000000 |
| WARD   |     30 |  2975.00 |       -1149.000000 |
| BLAKE  |     30 |  2850.00 |       -1274.000000 |
| TURNER |     30 |  1500.00 |       -2624.000000 |
| JAMES  |     30 |   950.00 |       -3174.000000 |
+--------+--------+----------+--------------------+
13 rows in set (0.0221 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal,min(sal) over (partition by deptno) as dept_min_salary,max(sal) over (partition by deptno) as dept_max_salary from emp;
+--------+--------+----------+-----------------+-----------------+
| ename  | deptno | sal      | dept_min_salary | dept_max_salary |
+--------+--------+----------+-----------------+-----------------+
| abcd   |   NULL |     NULL |            NULL |            NULL |
| raju   |     10 |  2450.00 |         1300.00 |        30000.00 |
| KING   |     10 | 30000.00 |         1300.00 |        30000.00 |
| MILLER |     10 |  1300.00 |         1300.00 |        30000.00 |
| JONES  |     20 |  1250.00 |         1100.00 |         3000.00 |
| SCOTT  |     20 |  3000.00 |         1100.00 |         3000.00 |
| ADAMS  |     20 |  1100.00 |         1100.00 |         3000.00 |
| FORD   |     20 |  3000.00 |         1100.00 |         3000.00 |
| ganesh |     30 | 12345.00 |          950.00 |        12345.00 |
| WARD   |     30 |  2975.00 |          950.00 |        12345.00 |
| BLAKE  |     30 |  2850.00 |          950.00 |        12345.00 |
| TURNER |     30 |  1500.00 |          950.00 |        12345.00 |
| JAMES  |     30 |   950.00 |          950.00 |        12345.00 |
+--------+--------+----------+-----------------+-----------------+
13 rows in set (0.0212 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,hiredate,sal,row_number() over (order by hiredate asc) as hire_rank from emp;
+--------+------------+----------+-----------+
| ename  | hiredate   | sal      | hire_rank |
+--------+------------+----------+-----------+
| abcd   | NULL       |     NULL |         1 |
| ganesh | 1981-02-22 | 12345.00 |         2 |
| WARD   | 1981-02-22 |  2975.00 |         3 |
| JONES  | 1981-04-02 |  1250.00 |         4 |
| BLAKE  | 1981-05-01 |  2850.00 |         5 |
| raju   | 1981-06-09 |  2450.00 |         6 |
| TURNER | 1981-09-08 |  1500.00 |         7 |
| KING   | 1981-11-17 | 30000.00 |         8 |
| JAMES  | 1981-12-03 |   950.00 |         9 |
| FORD   | 1981-12-03 |  3000.00 |        10 |
| MILLER | 1982-01-23 |  1300.00 |        11 |
| SCOTT  | 1982-12-09 |  3000.00 |        12 |
| ADAMS  | 1983-01-12 |  1100.00 |        13 |
+--------+------------+----------+-----------+
13 rows in set (0.0209 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from(select ename,sal,row_number() over (order by sal desc) as rnk from emp)as t where rnk=2;
+--------+----------+
| ename  | sal      |
+--------+----------+
| ganesh | 12345.00 |
+--------+----------+
1 row in set (0.0022 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal,percent_rank() over (partition by deptno order by sal) as pct_rank from emp;
+--------+--------+----------+--------------------+
| ename  | deptno | sal      | pct_rank           |
+--------+--------+----------+--------------------+
| abcd   |   NULL |     NULL |                  0 |
| MILLER |     10 |  1300.00 |                  0 |
| raju   |     10 |  2450.00 |                0.5 |
| KING   |     10 | 30000.00 |                  1 |
| ADAMS  |     20 |  1100.00 |                  0 |
| JONES  |     20 |  1250.00 | 0.3333333333333333 |
| SCOTT  |     20 |  3000.00 | 0.6666666666666666 |
| FORD   |     20 |  3000.00 | 0.6666666666666666 |
| JAMES  |     30 |   950.00 |                  0 |
| TURNER |     30 |  1500.00 |               0.25 |
| BLAKE  |     30 |  2850.00 |                0.5 |
| WARD   |     30 |  2975.00 |               0.75 |
| ganesh |     30 | 12345.00 |                  1 |
+--------+--------+----------+--------------------+
13 rows in set (0.0024 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >
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
Your MySQL connection id is 18 (X protocol)
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
15 rows in set (0.0035 sec)
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
7 rows in set (0.0043 sec)
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
13 rows in set (0.0023 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal>(select avg(sal) from emp);
+--------+----------+
| ename  | sal      |
+--------+----------+
| ganesh | 12345.00 |
| KING   | 30000.00 |
+--------+----------+
2 rows in set (0.0021 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno from emp where deptno=(select deptno from emp where ename='smith');
Empty set (0.0217 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno from emp where deptno=(select deptno from emp where ename='ford');
+-------+--------+
| ename | deptno |
+-------+--------+
| JONES |     20 |
| SCOTT |     20 |
| ADAMS |     20 |
| FORD  |     20 |
+-------+--------+
4 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >  select ename,sal from emp where sal>all(select sal from emp where deptno=30);
+-------+----------+
| ename | sal      |
+-------+----------+
| KING  | 30000.00 |
+-------+----------+
1 row in set (0.0211 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal=(select max(sal) from emp);
+-------+----------+
| ename | sal      |
+-------+----------+
| KING  | 30000.00 |
+-------+----------+
1 row in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,dname from dept where deptno not in (select distinct deptno from emp);
Empty set (0.0218 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,deptno,sal from emp e where sal>(select avg(sal) from emp where deptno=e.deptno);
+--------+--------+----------+
| ename  | deptno | sal      |
+--------+--------+----------+
| ganesh |     30 | 12345.00 |
| SCOTT  |     20 |  3000.00 |
| KING   |     10 | 30000.00 |
| FORD   |     20 |  3000.00 |
+--------+--------+----------+
4 rows in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,hiredate from emp where hiredate <(select min(hiredate) from emp where deptno=20);
+--------+------------+
| ename  | hiredate   |
+--------+------------+
| ganesh | 1981-02-22 |
| WARD   | 1981-02-22 |
+--------+------------+
2 rows in set (0.0021 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job from emp where job in (select distinct job from emp where deptno=10);
+--------+-----------+
| ename  | job       |
+--------+-----------+
| abcd   | clerk     |
| JONES  | MANAGER   |
| BLAKE  | MANAGER   |
| raju   | MANAGER   |
| KING   | PRESIDENT |
| ADAMS  | CLERK     |
| JAMES  | CLERK     |
| MILLER | CLERK     |
+--------+-----------+
8 rows in set (0.0214 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal >(select sal from emp where ename='allen');
Empty set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal >(select sal from emp where ename='miller');
+--------+----------+
| ename  | sal      |
+--------+----------+
| ganesh | 12345.00 |
| WARD   |  2975.00 |
| BLAKE  |  2850.00 |
| raju   |  2450.00 |
| SCOTT  |  3000.00 |
| KING   | 30000.00 |
| TURNER |  1500.00 |
| FORD   |  3000.00 |
+--------+----------+
8 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal=(select max(sal) from emp where sal<(select max(sal) from emp));
+--------+----------+
| ename  | sal      |
+--------+----------+
| ganesh | 12345.00 |
+--------+----------+
1 row in set (0.0023 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno from emp group by deptno having avg(sal)>(select avg(sal) from emp);
+--------+
| deptno |
+--------+
|     10 |
+--------+
1 row in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,e.sal,e.mgr,m.ename as manager_name,m.sal as manager_sal from emp e join emp m on e.mgr=m.empno where e.sal>m.sal;
+--------+----------+------+--------------+-------------+
| ename  | sal      | mgr  | manager_name | manager_sal |
+--------+----------+------+--------------+-------------+
| ganesh | 12345.00 | 7698 | BLAKE        |     2850.00 |
| WARD   |  2975.00 | 7698 | BLAKE        |     2850.00 |
| SCOTT  |  3000.00 | 7566 | JONES        |     1250.00 |
| FORD   |  3000.00 | 7566 | JONES        |     1250.00 |
+--------+----------+------+--------------+-------------+
4 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,hiredate from emp where hiredate >(Select max(hiredate) from emp where deptno=10);
+-------+------------+
| ename | hiredate   |
+-------+------------+
| SCOTT | 1982-12-09 |
| ADAMS | 1983-01-12 |
+-------+------------+
2 rows in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,sal from emp where sal> any(select sal from emp where deptno=20);
+--------+----------+
| ename  | sal      |
+--------+----------+
| ganesh | 12345.00 |
| WARD   |  2975.00 |
| JONES  |  1250.00 |
| BLAKE  |  2850.00 |
| raju   |  2450.00 |
| SCOTT  |  3000.00 |
| KING   | 30000.00 |
| TURNER |  1500.00 |
| FORD   |  3000.00 |
| MILLER |  1300.00 |
+--------+----------+
10 rows in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job,deptno from emp where job=(select job from emp where ename='ford') and deptno <> (select deptno from emp where ename='ford');
Empty set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select ename,job,deptno from emp where job=(select job from emp where ename='miller') and deptno <> (select deptno from emp where ename='miller');
+-------+-------+--------+
| ename | job   | deptno |
+-------+-------+--------+
| ADAMS | CLERK |     20 |
| JAMES | CLERK |     30 |
+-------+-------+--------+
2 rows in set (0.0020 sec)
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
Your MySQL connection id is 67 (X protocol)
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
12 rows in set (0.0027 sec)
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
13 rows in set (0.0493 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from dept;
+--------+------------+----------+
| deptno | dname      | loc      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | developer  | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
4 rows in set (0.0212 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,max(sal) from emp where deptno=10;
+--------+----------+
| deptno | max(sal) |
+--------+----------+
|     10 | 30000.00 |
+--------+----------+
1 row in set (0.0269 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,max(sal) from emp group by deptno;
+--------+----------+
| deptno | max(sal) |
+--------+----------+
|   NULL |     NULL |
|     10 | 30000.00 |
|     20 |  3000.00 |
|     30 | 12345.00 |
+--------+----------+
4 rows in set (0.0021 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,max(sal) from emp group by deptno having max(sal)> 3000;
+--------+----------+
| deptno | max(sal) |
+--------+----------+
|     10 | 30000.00 |
|     30 | 12345.00 |
+--------+----------+
2 rows in set (0.0216 sec).
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,max(sal) from emp group by deptno having max(sal)> 3000 order by max(sal);
+--------+----------+
| deptno | max(sal) |
+--------+----------+
|     30 | 12345.00 |
|     10 | 30000.00 |
+--------+----------+
2 rows in set (0.0220 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,max(sal) from emp group by deptno having max(sal)> 3000 order by max(sal) limit;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,max(sal) from emp group by deptno having max(sal)> 3000 order by max(sal) limit 1;
+--------+----------+
| deptno | max(sal) |
+--------+----------+
|     30 | 12345.00 |
+--------+----------+
1 row in set (0.0208 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp order by sal desc;
+-------+--------+-----------+------+------------+----------+---------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal      | comm    | deptno |
+-------+--------+-----------+------+------------+----------+---------+--------+
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 30000.00 |    NULL |     10 |
|  1234 | ganesh | SAELMAN   | 7698 | 1981-02-22 | 12345.00 |  500.00 |     30 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1982-12-09 |  3000.00 |    NULL |     20 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 |  3000.00 |    NULL |     20 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 |  2975.00 |    NULL |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 |  2850.00 |    NULL |     30 |
|  7782 | raju   | MANAGER   | 7839 | 1981-06-09 |  2450.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 |  1500.00 |    0.00 |     30 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 |  1300.00 |    NULL |     10 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 |  1250.00 | 1400.00 |     20 |
|  7876 | ADAMS  | CLERK     | 7788 | 1983-01-12 |  1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |   950.00 |    NULL |     30 |
|     1 | abcd   | clerk     | NULL | NULL       |     NULL |    NULL |   NULL |
+-------+--------+-----------+------+------------+----------+---------+--------+
13 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp order by sal desc limit 5;
+-------+--------+-----------+------+------------+----------+--------+--------+
| empno | ename  | job       | mgr  | hiredate   | sal      | comm   | deptno |
+-------+--------+-----------+------+------------+----------+--------+--------+
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 30000.00 |   NULL |     10 |
|  1234 | ganesh | SAELMAN   | 7698 | 1981-02-22 | 12345.00 | 500.00 |     30 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1982-12-09 |  3000.00 |   NULL |     20 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 |  3000.00 |   NULL |     20 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 |  2975.00 |   NULL |     30 |
+-------+--------+-----------+------+------------+----------+--------+--------+
5 rows in set (0.0019 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from emp order by sal desc limit 5 offset 4;
+-------+--------+----------+------+------------+---------+------+--------+
| empno | ename  | job      | mgr  | hiredate   | sal     | comm | deptno |
+-------+--------+----------+------+------------+---------+------+--------+
|  7521 | WARD   | SALESMAN | 7698 | 1981-02-22 | 2975.00 | NULL |     30 |
|  7698 | BLAKE  | MANAGER  | 7839 | 1981-05-01 | 2850.00 | NULL |     30 |
|  7782 | raju   | MANAGER  | 7839 | 1981-06-09 | 2450.00 | NULL |     10 |
|  7844 | TURNER | SALESMAN | 7698 | 1981-09-08 | 1500.00 | 0.00 |     30 |
|  7934 | MILLER | CLERK    | 7782 | 1982-01-23 | 1300.00 | NULL |     10 |
+-------+--------+----------+------+------------+---------+------+--------+
5 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >
 5 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,sum(sal) from emp group by deptno;
+--------+----------+
| deptno | sum(sal) |
+--------+----------+
|   NULL |     NULL |
|     10 | 33750.00 |
|     20 |  8350.00 |
|     30 | 20620.00 |
+--------+----------+
4 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select job,sum(sal) from emp group by job;
+-----------+----------+
| job       | sum(sal) |
+-----------+----------+
| clerk     |  3350.00 |
| SAELMAN   | 12345.00 |
| SALESMAN  |  4475.00 |
| MANAGER   |  6550.00 |
| ANALYST   |  6000.00 |
| PRESIDENT | 30000.00 |
+-----------+----------+
6 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,e.job,d.dname,d.loc from emp e join dept d on d.deptno = e.deptno;
+--------+-----------+------------+----------+
| ename  | job       | dname      | loc      |
+--------+-----------+------------+----------+
| raju   | MANAGER   | ACCOUNTING | NEW YORK |
| KING   | PRESIDENT | ACCOUNTING | NEW YORK |
| MILLER | CLERK     | ACCOUNTING | NEW YORK |
| JONES  | MANAGER   | RESEARCH   | DALLAS   |
| SCOTT  | ANALYST   | RESEARCH   | DALLAS   |
| ADAMS  | CLERK     | RESEARCH   | DALLAS   |
| FORD   | ANALYST   | RESEARCH   | DALLAS   |
| ganesh | SAELMAN   | developer  | CHICAGO  |
| WARD   | SALESMAN  | developer  | CHICAGO  |
| BLAKE  | MANAGER   | developer  | CHICAGO  |
| TURNER | SALESMAN  | developer  | CHICAGO  |
| JAMES  | CLERK     | developer  | CHICAGO  |
+--------+-----------+------------+----------+
12 rows in set (0.0022 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.dname,e.deptno,d.deptno from emp e inner join dept d on d.deptno=e.deptno;
+--------+------------+--------+--------+
| ename  | dname      | deptno | deptno |
+--------+------------+--------+--------+
| raju   | ACCOUNTING |     10 |     10 |
| KING   | ACCOUNTING |     10 |     10 |
| MILLER | ACCOUNTING |     10 |     10 |
| JONES  | RESEARCH   |     20 |     20 |
| SCOTT  | RESEARCH   |     20 |     20 |
| ADAMS  | RESEARCH   |     20 |     20 |
| FORD   | RESEARCH   |     20 |     20 |
| ganesh | developer  |     30 |     30 |
| WARD   | developer  |     30 |     30 |
| BLAKE  | developer  |     30 |     30 |
| TURNER | developer  |     30 |     30 |
| JAMES  | developer  |     30 |     30 |
+--------+------------+--------+--------+
12 rows in set (0.0021 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,e.deptno,d.dname,d.deptno from emp e inner join dept d on d.deptno=e.deptno;
+--------+--------+------------+--------+
| ename  | deptno | dname      | deptno |
+--------+--------+------------+--------+
| raju   |     10 | ACCOUNTING |     10 |
| KING   |     10 | ACCOUNTING |     10 |
| MILLER |     10 | ACCOUNTING |     10 |
| JONES  |     20 | RESEARCH   |     20 |
| SCOTT  |     20 | RESEARCH   |     20 |
| ADAMS  |     20 | RESEARCH   |     20 |
| FORD   |     20 | RESEARCH   |     20 |
| ganesh |     30 | developer  |     30 |
| WARD   |     30 | developer  |     30 |
| BLAKE  |     30 | developer  |     30 |
| TURNER |     30 | developer  |     30 |
| JAMES  |     30 | developer  |     30 |
+--------+--------+------------+--------+
12 rows in set (0.0019 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,e.deptno,d.dname,d.deptno from emp e inner join dept d on d.deptno=e.deptno where e.job='salemana;
                                         '> ^C
 MySQL  localhost:33060+ ssl  aneela  SQL > select count(empno) from emp;
+--------------+
| count(empno) |
+--------------+
|           13 |
+--------------+
1 row in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select deptno,count(empno) from emp group by deptno;
+--------+--------------+
| deptno | count(empno) |
+--------+--------------+
|   NULL |            1 |
|     10 |            3 |
|     20 |            4 |
|     30 |            5 |
+--------+--------------+
4 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select dname,count(empno) from emp group by deptno;
ERROR: 1054: Unknown column 'dname' in 'field list'
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,count(e.mpno) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
ERROR: 1054: Unknown column 'e.mpno' in 'field list'
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,count(empno) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
+------------+--------------+
| dname      | count(empno) |
+------------+--------------+
| ACCOUNTING |            3 |
| RESEARCH   |            4 |
| developer  |            5 |
+------------+--------------+
3 rows in set (0.0223 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,count(*) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
+------------+----------+
| dname      | count(*) |
+------------+----------+
| ACCOUNTING |        3 |
| RESEARCH   |        4 |
| developer  |        5 |
+------------+----------+
3 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,max(sal) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
+------------+----------+
| dname      | max(sal) |
+------------+----------+
| ACCOUNTING | 30000.00 |
| RESEARCH   |  3000.00 |
| developer  | 12345.00 |
+------------+----------+
3 rows in set (0.0017 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,min(sal) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
+------------+----------+
| dname      | min(sal) |
+------------+----------+
| ACCOUNTING |  1300.00 |
| RESEARCH   |  1100.00 |
| developer  |   950.00 |
+------------+----------+
3 rows in set (0.0223 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,avg(sal) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
+------------+--------------+
| dname      | avg(sal)     |
+------------+--------------+
| ACCOUNTING | 11250.000000 |
| RESEARCH   |  2087.500000 |
| developer  |  4124.000000 |
+------------+--------------+
3 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,avg(e.sal) from emp e  join dept d on e.deptno=d.deptno group by d.deptno;
+------------+--------------+
| dname      | avg(e.sal)   |
+------------+--------------+
| ACCOUNTING | 11250.000000 |
| RESEARCH   |  2087.500000 |
| developer  |  4124.000000 |
+------------+--------------+
3 rows in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.dname,avg(e.sal) from emp e  join dept d on e.job=d.deptno group by d.deptno;
ERROR: 1054: Unknown column 'e.dname' in 'field list'
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,count(*),e.ename,d.loc  from emp e join dept d  d.deptno=e.deptno group by d.dname,d.loc;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'd.deptno=e.deptno group by d.dname,d.loc' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select d.dname,count(*),d.loc  from emp e join dept d  d.deptno=e.deptno group by d.dname,d.loc;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'd.deptno=e.deptno group by d.dname,d.loc' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select * from dept;
+--------+------------+----------+
| deptno | dname      | loc      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | developer  | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
4 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.dname from emp e left join dept d on e.deptno=d.deptno;
+--------+------------+
| ename  | dname      |
+--------+------------+
| abcd   | NULL       |
| ganesh | developer  |
| WARD   | developer  |
| JONES  | RESEARCH   |
| BLAKE  | developer  |
| raju   | ACCOUNTING |
| SCOTT  | RESEARCH   |
| KING   | ACCOUNTING |
| TURNER | developer  |
| ADAMS  | RESEARCH   |
| JAMES  | developer  |
| FORD   | RESEARCH   |
| MILLER | ACCOUNTING |
+--------+------------+
13 rows in set (0.0022 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.dname from dept dleft join emp e on e.deptno=d.deptno;
ERROR: 1054: Unknown column 'd.dname' in 'field list'
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.dname from dept d left join emp e on e.deptno=d.deptno;
+--------+------------+
| ename  | dname      |
+--------+------------+
| raju   | ACCOUNTING |
| KING   | ACCOUNTING |
| MILLER | ACCOUNTING |
| JONES  | RESEARCH   |
| SCOTT  | RESEARCH   |
| ADAMS  | RESEARCH   |
| FORD   | RESEARCH   |
| ganesh | developer  |
| WARD   | developer  |
| BLAKE  | developer  |
| TURNER | developer  |
| JAMES  | developer  |
| NULL   | OPERATIONS |
+--------+------------+
13 rows in set (0.0022 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,m.ename from emp e join emp m on e.mgr=m.empno;
+--------+-------+
| ename  | ename |
+--------+-------+
| ganesh | BLAKE |
| WARD   | BLAKE |
| JONES  | KING  |
| BLAKE  | KING  |
| raju   | KING  |
| SCOTT  | JONES |
| TURNER | BLAKE |
| ADAMS  | SCOTT |
| JAMES  | BLAKE |
| FORD   | JONES |
| MILLER | raju  |
+--------+-------+
11 rows in set (0.0027 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,m.ename avg(sal) from  emp e join emp m on e.sal=m.sal
                                         -> ;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(sal) from  emp e join emp m on e.sal=m.sal' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,m.ename avg(sal) from  emp e join emp m on e.mgr=m.empno where e.sal>m.sal;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(sal) from  emp e join emp m on e.mgr=m.empno where e.sal>m.sal' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,e.sal,m.ename,m.sal from emp e join emp m on e.mgr=m.empno where e.sal>m.sal;
+--------+----------+-------+---------+
| ename  | sal      | ename | sal     |
+--------+----------+-------+---------+
| ganesh | 12345.00 | BLAKE | 2850.00 |
| WARD   |  2975.00 | BLAKE | 2850.00 |
| SCOTT  |  3000.00 | JONES | 1250.00 |
| FORD   |  3000.00 | JONES | 1250.00 |
+--------+----------+-------+---------+
4 rows in set (0.0018 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.ename from emp e joinn emp d e.mgr=d.deptno;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'joinn emp d e.mgr=d.deptno' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename from emp e joinn emp d  where e.mgr is null;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'joinn emp d  where e.mgr is null' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL >
  MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.dname from emp e left join dept d  on e.deptno=d.deptno union select e.ename,d.dname from emp e right join dept d on e.deptno=d.deptno;
+--------+------------+
| ename  | dname      |
+--------+------------+
| abcd   | NULL       |
| ganesh | developer  |
| WARD   | developer  |
| JONES  | RESEARCH   |
| BLAKE  | developer  |
| raju   | ACCOUNTING |
| SCOTT  | RESEARCH   |
| KING   | ACCOUNTING |
| TURNER | developer  |
| ADAMS  | RESEARCH   |
| JAMES  | developer  |
| FORD   | RESEARCH   |
| MILLER | ACCOUNTING |
| NULL   | OPERATIONS |
+--------+------------+
14 rows in set (0.0238 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.ename from  emp e crouse join dept d;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'crouse join dept d' at line 1
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.ename from  emp e cross join dept d;
ERROR: 1054: Unknown column 'd.ename' in 'field list'
 MySQL  localhost:33060+ ssl  aneela  SQL > select e.ename,d.dname from  emp e cross join dept d;
+--------+------------+
| ename  | dname      |
+--------+------------+
| abcd   | OPERATIONS |
| abcd   | developer  |
| abcd   | RESEARCH   |
| abcd   | ACCOUNTING |
| ganesh | OPERATIONS |
| ganesh | developer  |
| ganesh | RESEARCH   |
| ganesh | ACCOUNTING |
| WARD   | OPERATIONS |
| WARD   | developer  |
| WARD   | RESEARCH   |
| WARD   | ACCOUNTING |
| JONES  | OPERATIONS |
| JONES  | developer  |
| JONES  | RESEARCH   |
| JONES  | ACCOUNTING |
| BLAKE  | OPERATIONS |
| BLAKE  | developer  |
| BLAKE  | RESEARCH   |
| BLAKE  | ACCOUNTING |
| raju   | OPERATIONS |
| raju   | developer  |
| raju   | RESEARCH   |
| raju   | ACCOUNTING |
| SCOTT  | OPERATIONS |
| SCOTT  | developer  |
| SCOTT  | RESEARCH   |
| SCOTT  | ACCOUNTING |
| KING   | OPERATIONS |
| KING   | developer  |
| KING   | RESEARCH   |
| KING   | ACCOUNTING |
| TURNER | OPERATIONS |
| TURNER | developer  |
| TURNER | RESEARCH   |
| TURNER | ACCOUNTING |
| ADAMS  | OPERATIONS |
| ADAMS  | developer  |
| ADAMS  | RESEARCH   |
| ADAMS  | ACCOUNTING |
| JAMES  | OPERATIONS |
| JAMES  | developer  |
| JAMES  | RESEARCH   |
| JAMES  | ACCOUNTING |
| FORD   | OPERATIONS |
| FORD   | developer  |
| FORD   | RESEARCH   |
| FORD   | ACCOUNTING |
| MILLER | OPERATIONS |
| MILLER | developer  |
| MILLER | RESEARCH   |
| MILLER | ACCOUNTING |
+--------+------------+
52 rows in set (0.0025 sec)
 MySQL  localhost:33060+ ssl  aneela  SQL >











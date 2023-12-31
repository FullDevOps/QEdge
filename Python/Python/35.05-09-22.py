# 35th day 35.05.09.22
##Programs in PDBC to MySQL::-
# ------------------------------------

#Program(MySQLDBCreate.py)
# (Program to create mysql new database "mydb" & verify it)

#Program(MySQLDBCreate.py)
#(Program to create mysql new database "mydb" & verify it)

#create database
import mysql.connector;

conn = mysql.connector.connect( host="localhost", user="root",password="root", port=3306);
mycursor = conn.cursor();

#drop mydb-database
mycursor.execute("drop DATABASE sample");
print("Database dropped successfully");

#mycursor.execute("CREATE DATABASE mydb;");
#print("Database Created successfully");

#verify databases
mycursor.execute("SHOW DATABASES;");
print(mycursor);    #iterable-obj(used with loops) list-of-tuples
for x in mycursor:
   print(x)


# NOTE:-
# = MySQL command
mysql> show databases;
mysql> create database mydb;
mysql> show databases;
# -------------------------------
mysql> use mydb;
mysql> show tables;
# -------------------------------
mysql> drop database mydb;
mysql> show databases;

# Ex:-
#Program (DBEx2.py)
# (Program to create Employees-table in Oracle-DB/MYSQL)


***Create mydb-database & keep it ready****
(and after that create tables under mydb-database)
(inside database, we create tables)
NOTE:- (MYSQL commands for table-creation)
mysql> show databases;
mysql> use mydb;
mysql> show tables;
mysql> create table employees
    (
    eno int,
    ename varchar(10),
    esal int,
    eaddr varchar(20)
    );
mysql> show tables;
mysql> describe employees;
mysql> drop table employees;
mysql> show tables;


#Program (DBEx2.py)
#Program to create Employees-table Oracle-DB/MYSQL

#mysql
import mysql.connector;
try:
	conn = mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	print(conn);
	print();
	mycursor=conn.cursor();
	#mycursor.execute("create table employees(eno int,ename varchar(10), esal int, eaddr varchar(10))");
	#print(mycursor);
	#print()
	#for x in mycursor:
	#	print(x)
	#print();
	#print("Table Created Successfully");
	#print()
	mycursor.execute("show tables;");
	for x in mycursor:
		print(x)
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();



# ------------------------------------------------------------
# Ex2a:- 
#Program (DBEx2a.py)
# (Program to drop Employees-table in Oracle-DB/MYSQL)
# -------------------------------
# **connect to mysql-database**

mysql> show databases
mysql> use mydb
mysql> show tables
mysql> drop table Employees
mysql> show tables
mysql>create table employees
    (
    eno int,
    ename varchar(10),
    esal int,
    eaddr varchar(10)
    );
mysql> show tables	
# -------------------------------


#Program (DBEx2a.py)
#Program to drop Employees-table from Oracle-DB/MySQL

#mysql
import mysql.connector;
try:
	conn = mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	print(conn);
	print()
	mycursor=conn.cursor();
	mycursor.execute("drop table employees");
	print(mycursor);
	print()
	print("Table Dropped Successfully");
	print()
	mycursor.execute("show tables;");
	for x in mycursor:
		print(x)
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();
        



# -------------------------------------------------------------------
# Ex3:- (create table once-again and insert the records)
#Program (DBEx3.py)
# (Program to insert record into Employees-table of Oracle-DB/MYSQL)
# ---------------------------------------

(MY-SQL commands)
mysql> show tables;
mysql> create table employees
         (
         eno int,
         ename varchar(10),
         esal int,
         eaddr varchar(10)
         );
mysql> show tables;
mysql> describe employees;
mysql> select * from employees;
mysql> insert into employees values(1001,'Sai',5600,'Hyd');
mysql> select * from employees;
mysql> delete from employees where eno=1001;
mysql> select * from employees;
(dont use below-cmds)
#mysql> drop table employees;
#mysql> show tables;


#Program (DBEx3.py)
#(Program to create & insert record into Employees-table of Oracle-DB/MYSQL)

#mysql
import mysql.connector;
try:
	conn = mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	mycursor=conn.cursor();
	mycursor.execute("insert into employees values(1001,'Sai',5600,'Hyd')");
	print()
	for x in mycursor:
		print(x)
	conn.commit();
	print("Record Inserted Successfully");
	mycursor.execute("select * from employees;")
	print()
	for x in mycursor:
		print(x)
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();

"""
-------------------------------------------------
Ex4:-
Program (DBEx4.py)
(Program to insert multiple-records into Employees-table of Oracle-DB/MYSQL using executemany())
%s (string)  #preferable is %s(auto. converted to respective dtype on DB)
%d (integer)
%f (float)
==** %char means unknown value in sql-command in execute() function


NOTE:-
1)
= For inserting 1-record, mysql-command is,
mysql> insert into employees values(1001,'Sai',5600,'Hyd'); //static-values
****cursorObj.execute("insert into employees values(1001,'Sai',5600,'Hyd')");

2)
= For inserting multiple-records at a time from Python-Program,
sqlcmd = "insert into employees values(%s,%s,%s,%s)"
(here, we use executemany() with 2-input-para)
Ex:-
	cursorObj.executemany(sqlcmd,listoftuples)
records = [(1002,'Ram',3600,'Secbad'),		
				(1003,'Ali',4600,'HiTech'),
				(1004,'Tom',2600,'KPHB')];

"""
#Program (DBEx4.py)
#(Program to insert multiple-records into Employees-table of Oracle-DB /MYSQL using executemany())

#mysql
import mysql.connector;
try:
	conn = mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	mycursor=conn.cursor();
	sqlcmd = "insert into employees(eno,ename,esal,eaddr) values(%s,%s,%s,%s)";
	#%s means unknown values
	#list of tuples
	listofrecords = [
		(1002,'Ram',3600,'Secbad'),		
		(1003,'Ali',4600,'HiTech'),
		(1004,'Tom',2600,'KPHB')
            ];
	mycursor.executemany(sqlcmd,listofrecords);
	conn.commit();
	print(mycursor.rowcount)
	print("Record(s) Inserted Successfully");
	print()
	mycursor.execute("select * from employees");
	for x in mycursor:
		print(x)
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();


# NOTE:-
# = mycursor.rowcount var is available for insert/update/del commands...


# ------------------------------------------------------
# ***(Assignment)*** (DBEx41.py)
# = For inserting 1-record with dynamic-input,
print("Enter Employee-Data ::");
empno = input("Enter emp-no ::");
ename = input("Enter emp-name ::");
esal = input("Enter Salary ::");
eaddr = input("Enter Address ::");
# ****sqlcmd="insert into employees(eno,ename,esal,eaddr) values("+empno+",'"+ename+"',"+esal+",'"+eaddr+"')";
    # cursorObj.execute(sqlcmd);

# ----------------------------------------------------------

#-- 36th day 35.06-09-22
# ****PDBC other programs***
# ----------------------------------------------
# Ex5:-
#Program (DBEx5.py)
# (Program to insert multiple-records into Employees-table of Oracle-DB/MYSQL using execute() with dynamic-input) - using loop
'''
NOTE:-
(***)
sqlcmd = "insert into employees values(%s,%s,%s,%s)";
cursorObj.execute(sqlcmd,(eno,ename,esal,eaddr));	#tuple-of-values

=*** Always use conn.commit() in try-block & conn.rollback() in except-block
'''

#Program (DBEx5.py)
#(Program to insert multiple-records into Employees-table of Oracle-DB/MYSQL using execute() with dynamic-input using loop)


#mysql
import mysql.connector;
try:
	conn = mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	mycursor=conn.cursor();
	while True:
		print("Enter Employee-Data :");
		eno=int(input("EmpNo : "));
		ename=input("Emp-Name : ");
		esal=float(input("Emp-Salary : "));
		eaddr=input("Emp-Addr : ");
		sqlcmd = "insert into employees values(%s,%s,%s,%s)";
		mycursor.execute(sqlcmd,(eno,ename,esal,eaddr));	#tuple-of-values
		print("Record Inserted Successfully");
		option=input("Do you want to insert one more record(Yes|No)? ");
		if option=="No":
			conn.commit();
			break;
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();	
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();


# ------------------------------------------------------------------
# Ex6:- (Update-Operation on Table-data)
#Program (DBEx6.py)
# (Program to update Employees-Sal with Increment-Sal of Oracle-DB/MYSQL using Dynamic-Input)

# NOTE:-
sqlcmd="update employees set esal=esal+%s where esal<%s";
cursorObj.execute(sqlcmd,(increment,salrange));	#tuple-of-values
print("Records Updated Successfully ::",cursorObj.rowcount);

#Program (DBEx6.py)
#(Program to update Employees-Sal with Increment-Sal of Oracle-DB/MYSQL using Dynamic-Input)


#MYSQL
#Increment-Sal by 400 whose sal is less than 4000
import mysql.connector;
try:
	conn = mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	mycursor=conn.cursor();
	increment = float(input("Enter Increment Salary : "));
	salrange = float(input("Enter Salary Range : "));
	sqlcmd="update employees set esal=esal+%s where esal<%s";
	mycursor.execute(sqlcmd,(increment,salrange));	#tuple-of-values
	print("Records Updated Successfully ::",mycursor.rowcount);
	conn.commit();
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();		
		
# ------------------------------------------------------------------
# ==> Programs on PDBC(MySQL)
# (Deleting the records)
# ##Programs on Python DBC (MySQL)
# Ex7:-
# #Program (DBEx7.py)
# (Program to delete Employees-Record whose sal is greater than provided Sal using Dynamic-Input)
# #delete all emps whose sal is > than 5000
# (%s-->string) #unknown values (pass with execute(sqlcmd,unknown))
# (%d-->integer)
# (%f-->floating)
# Format-specifiers(unknown) used for dynamic-input-values in SQL-query

# NOTE:-
sqlcmd="delete from employees where esal > %f";	#%s

cursorObj.execute(sqlcmd%cutoffsal);	
#for single-value use SQLCmd%single-value

print(cursorObj.rowcount,"Records Deleted Successfully");


#Program (DBEx7.py)
#Program to delete Employees-Record whose sal is greater than provided Sal using Dynamic-Input
#delete all emps whose sal is > than 5000


#MySQL
import mysql.connector;
try:
	conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="mydb");	#port=3306
	mycursor=conn.cursor();
	cutoffsal = float(input("Enter Cutoff Salary : "));
	sqlcmd="delete from employees where esal > %f";	    #%s
	mycursor.execute(sqlcmd%cutoffsal);	
    #for single-value use SQLCmd%value
	print(mycursor.rowcount,"Records Deleted Successfully");
	conn.commit();
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();		



	

# ------------------------------------------------------------------
# => (select command with fetchone())
# Ex8:-
#Program (DBEx8.py)
#Program to select all Emps-Info using fetchone() method
# NOTE:-
empno=input("Enter Employee-No :: ");
cursorObj.execute("select * from employees where eno="+empno);
row=cursorObj.fetchone();
if row is not None:
	print(row);
else:
	print("NO Such Record is there");


#Program (DBEx8.py)
#Program to select all Emps-Info using fetchone() method


#MySQLDB
import mysql.connector;
try:
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydb", port=3306);
	mycursor=conn.cursor();
	mycursor.execute("select * from employees where eno='1004'");
	row=mycursor.fetchone();
	print(row);
	print()
	for x in row:
		print(x);
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();		


# NOTe:-
# = Here commit() is not-required
# = it is used only for insert/update/delete


# -----------------------------------------------------------------
# => (select command with fetchall())
# //Programs 
# Ex9:-
#Program (DBEx9.py)
#Program to select all Emps-Info using fetchall() method
# NOTE:-
cursorObj.execute("select * from employees");
data=cursorObj.fetchall();
print(data);		#list of tuples
#[(),(),(),(),()]
for row in data:
	print("Emp-No :",row[0]);
	print("Emp-Name :",row[1]);
	print("Emp-Sal :",row[2]);
	print("Emp-Addr :",row[3]);
	print("\n");

# =*** insert/update/delete directly on DB-command prompt are auto-committed
# =** insert/update/delete are manaully committed done from Python program

#Program (DBEx9.py)
#Program to select all Emps-Info using fetchall() method

#MySQLDB
import mysql.connector;
try:
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	mycursor=conn.cursor();
	mycursor.execute("select * from employees");
	data=mycursor.fetchall();
	print(data);		#list of tuples
	for row in data:
		print("Emp-No :",row[0]);
		print("Emp-Name :",row[1]);
		print("Emp-Sal :",row[2]);
		print("Emp-Addr :",row[3]);
		print("\n");
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
# => (select command with fetchmany())
# Ex10:-
#Program (DBEx10.py)
#Program to select all Emps-Info using fetchmany() method & provide required no.of rows as dynamic-input
# NOTE:-
cursorObj.execute("select * from employees");
n=int(input("Enter No.of Required Rows :"));
data=cursorObj.fetchmany(n);	
print(data);	#list of tuples [(row1),(row2),(row3),....]
for row in data:
	print(row);
cursorObj.close();


#Program (DBEx10.py)
#Program to select all Emps-Info using fetchmany() method & provide required no.of rows as dynamic-input


#MySQLDB
import mysql.connector;
try:
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydb",port=3306);
	mycursor=conn.cursor();
	mycursor.execute("select * from employees");
	n=int(input("Enter No.of Required Rows :"));
	data=mycursor.fetchmany(n);	
	print(data);	#list of tuples [(row1),(row2),(row3),....]
	print()
	for row in data:
		print(row);
	#mycursor.close();
except mysql.connector.DatabaseError as e:
	print("Error in executing SQL-cmd :",e);
	if conn:
		conn.rollback();
finally:
	if mycursor:
		mycursor.close();
	if conn:	
		conn.close();	

''''
=================================================================
==> Other MySQL sql-commands::- (For Practice)
mysql> insert into employees(eno,ename,eaddr)
    -> values(1007,'Hari','Amrpt');
Query OK, 1 row affected (0.00 sec)

mysql> select * from employees;
+------+---------+------+--------+
| eno  | ename   | esal | eaddr  |
+------+---------+------+--------+
| 1002 | Ram     | 4000 | Secbad |
| 1003 | Ali     | 4600 | HiTech |
| 1004 | Tom     | 3000 | KPHB   |
| 1005 | Anup    | 4500 | DSNR   |
| 1006 | Krishna | 4950 | KPHP   |
| 1007 | Hari    | NULL | Amrpt  |
+------+---------+------+--------+
6 rows in set (0.00 sec)

-------------------------------------------------------------
mysql> insert into employees
    -> values(1008,'Ravi',NULL,NULL);
Query OK, 1 row affected (0.00 sec)

mysql> select * from employees;
+------+---------+------+--------+
| eno  | ename   | esal | eaddr  |
+------+---------+------+--------+
| 1002 | Ram     | 4000 | Secbad |
| 1003 | Ali     | 4600 | HiTech |
| 1004 | Tom     | 3000 | KPHB   |
| 1005 | Anup    | 4500 | DSNR   |
| 1006 | Krishna | 4950 | KPHP   |
| 1007 | Hari    | NULL | Amrpt  |
| 1008 | Ravi    | NULL | NULL   |
+------+---------+------+--------+
7 rows in set (0.00 sec)

-------------------------------------------------------------
mysql> update employees
    -> set esal=5000
    -> where eno=1007;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from employees;
+------+---------+------+--------+
| eno  | ename   | esal | eaddr  |
+------+---------+------+--------+
| 1002 | Ram     | 4000 | Secbad |
| 1003 | Ali     | 4600 | HiTech |
| 1004 | Tom     | 3000 | KPHB   |
| 1005 | Anup    | 4500 | DSNR   |
| 1006 | Krishna | 4950 | KPHP   |
| 1007 | Hari    | 5000 | Amrpt  |
| 1008 | Ravi    | NULL | NULL   |
+------+---------+------+--------+
7 rows in set (0.00 sec)

-------------------------------------------------------------
mysql> update employees
    -> set esal=5600,eaddr='KOTI'
    -> where eno=1008;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from employees;
+------+---------+------+--------+
| eno  | ename   | esal | eaddr  |
+------+---------+------+--------+
| 1002 | Ram     | 4000 | Secbad |
| 1003 | Ali     | 4600 | HiTech |
| 1004 | Tom     | 3000 | KPHB   |
| 1005 | Anup    | 4500 | DSNR   |
| 1006 | Krishna | 4950 | KPHP   |
| 1007 | Hari    | 5000 | Amrpt  |
| 1008 | Ravi    | 5600 | KOTI   |
+------+---------+------+--------+
7 rows in set (0.00 sec)

-------------------------------------------------------------
mysql> delete from employees
    -> where eaddr='KPHB';
Query OK, 1 row affected (0.00 sec)

mysql> select * from employees;
+------+---------+------+--------+
| eno  | ename   | esal | eaddr  |
+------+---------+------+--------+
| 1002 | Ram     | 4000 | Secbad |
| 1003 | Ali     | 4600 | HiTech |
| 1005 | Anup    | 4500 | DSNR   |
| 1006 | Krishna | 4950 | KPHP   |
| 1007 | Hari    | 5000 | Amrpt  |
| 1008 | Ravi    | 5600 | KOTI   |
+------+---------+------+--------+
6 rows in set (0.00 sec)
-------------------------------------------------------------

mysql> delete from employees
    -> where eaddr='KPHP' and ename='Krishna';
Query OK, 1 row affected (0.00 sec)

mysql> select * from employees;
+------+-------+------+--------+
| eno  | ename | esal | eaddr  |
+------+-------+------+--------+
| 1002 | Ram   | 4000 | Secbad |
| 1003 | Ali   | 4600 | HiTech |
| 1005 | Anup  | 4500 | DSNR   |
| 1007 | Hari  | 5000 | Amrpt  |
| 1008 | Ravi  | 5600 | KOTI   |
+------+-------+------+--------+
5 rows in set (0.00 sec)
-------------------------------------------------------------

mysql> update employees
    -> set ename='Ravindra'
    -> where eno=1008;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from employees;
+------+----------+------+--------+
| eno  | ename    | esal | eaddr  |
+------+----------+------+--------+
| 1002 | Ram      | 4000 | Secbad |
| 1003 | Ali      | 4600 | HiTech |
| 1005 | Anup     | 4500 | DSNR   |
| 1007 | Hari     | 5000 | Amrpt  |
| 1008 | Ravindra | 5600 | KOTI   |
+------+----------+------+--------+
5 rows in set (0.00 sec)

-------------------------------------------------------------
mysql> select eno,ename from employees
    -> where esal>4500;
+------+----------+
| eno  | ename    |
+------+----------+
| 1003 | Ali      |
| 1007 | Hari     |
| 1008 | Ravindra |
+------+----------+
3 rows in set (0.00 sec)

-------------------------------------------------------------
mysql> select eno,ename from employees
    -> where esal<=4500 and eaddr='DSNR';
+------+-------+
| eno  | ename |
+------+-------+
| 1005 | Anup  |
+------+-------+
1 row in set (0.00 sec)

mysql>
-------------------------------------------------------------


==================================================================
==>>> Regular Expressions in Python:-
= Representation of strings in particular-format or particular-pattern is done with Regular-Expressions(proper-required-format)
=> tech-def:-
	= It is a declarative mechanism to represent Strings in particular-format or particular-pattern or proper-format
Ex:-
1) RegEx is used to represent Mobile-No's 
(10-digits with +91)
Ex:- +91XXXXXXXXXX
Ex:- +91-9XXXXXXXXX	(8/7/6)
2) Used to represent Email-Id pattern 
Ex:-
	userid@domain.xxx
	userid@domain.xx.xx

=> RegEx are used in below apps:-
1) Validation-Frameworks or Validation-Logics
2) Pattern Matching Apps (Ex:- Ctrl+F in Windows, grep in Unix)
3) Developing Translators like Compilers/Interpreters etc
4) Developing Digital Circuits
5) Developing Comm. Protocols like TCP/IP, UDP etc


==> Working with Regular-Expressions:-
NOTE:-
= "re" module in Python is used to work with RegEx
= this module provides different functions to work with RegEx

1) compile()
= Gives RegexObject i.e, converts pattern to RegexObject
Ex:-
	pattern = re.compile("ab");
	
2) pattern.finditer("org-string")	#finditer()
= Gives and Iterator(Looping like) object 
i.e, Match-object for every Match

3)
= On Match-object, we use below methods,
	i) start()  -> Gives start-index of the match
	ii) end()	-> Gives end+1 index of the match
	iii) group()-> Gives the matched string
'''
# Ex:-
#Program (RegEx1.py)
#Program (RegEx1.py)
#Regex with compile() & finditer()


#compile() and finditer()
import re;
#step1
pattern=re.compile("ab");	
print(pattern)
print(type(pattern))		#re.Pattern-object

#search pattern
#step-2

matcher=pattern.finditer("abaababaaab");	#Match-obj is callable-iterator-obj
print(matcher)
print(type(matcher))

#step3
count=0;
for mm in matcher:
	count+=1;
	print(mm.start(),"\t",mm.end(),"\t",mm.group())
	
print("The No.of Occurrence :",count);



#direct-case w.o compile()
#passing pattern directly to finditer()
import re;
count=0;
matcher=re.finditer("ba","abaababaaaba");	#Match-obj(call-iterator-obj)
for mm in matcher:
	count+=1;
	print(mm.start(),"\t",mm.end(),"\t",mm.group());
	
print("The No.of Occurrence :",count);


# NOTE:-
# = We can also pass pattern-string directly to finditer() function
Ex:- re.finditer("pattern","org-string")


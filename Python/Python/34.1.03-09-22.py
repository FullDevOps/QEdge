# 34th day 34.1.03-09-22

"""
=======================================================================================================================
==>>> Database-Programming in Python:-
=======================================================================================================================
(Python Database Connectivity)
= Data which is processed in program in temporary
i.e, once execution is done it is erased from memory and for next-execution again we have to give new-input
= Files stores program data permanently and is less secure and less efficient
= For this we have Database storage system for Secure-Access and Efficient-Access of data

=> Basically we have 2-types of Storage Areas in any Programming:-
1) Temporary Storage
2) Permanent Storage

1) Temporary Storage:-
= Here program-data is stored temporarily till program execution process only
Ex:-
Python Variables, List, Tuple, Set, Frozen-Set, Dictionary etc

2) Permanent Storage:-
= Here program-data is stored permanently
= Also called as Persistent Storage
Ex:-
Computer-Files, DataBases, Data Warehouses, Big Data etc



==> File Systems:-
= They are Local Computer OS file-system
= Suitable for storing less amount of data
Limitations:-
	= Cannont store Huge Amount of data
	= All Operations are Manual (Insert/Update/Delete)
	= No Security to data (Anyone can open and access file-data)
	= Cannot prevent duplicate data
	= Have Inconsistency of data (Wrong-data)
= To overcome above limitations, we go for DataBases

==> DataBase System:-
= Here we can store Huge amount of data (Tables)
= Provides Query Language for DB Operations
= Data-Security is provided with Username & Password
= Provides constraints(conditions) on Table-Data (Duplicate data can be avoided)
Limitations:-
	= Cannot hold Tera bytes of data
	= Supports only Structured Table data 
	= No support for Semi-Structured data (like XML)
	= No support for Unstructured data (Images/Audio/Video files)
= To overcome above limitations, we can go for Data ware Houses, Big-Data etc




==> Python DB Programming:-
= It allows us to communicate with DB & its tables to perform DB Operations (Create tables, insert, update, delete, selecting-data)
= Using Python we send SQL-commands to DB for operations
= We can communicate with diff DB's like Oracle, MySql, Sql-Server, Ingress, Postgre, GadFly, Sqlite3(django), MongoDB, DB2 etc
= Python provides separate module for each DB

***Python DB Drivers***
--------------------------
Ex:-
	mysql.connector module (MY-SQL DB)***
	cx_Oracle module (Oracle DB)###
	
	pymssql module (MS-SQL Server)***
	
NOTE:-
= These are 3rd-party lib-modules for DB-prog
= Such lib-modules, should be installed & used in prog	
= It is done as follows
Ex:-
cmd> pip install mysql-connector-python
(mysql_connector_python-8.0.30)
cmd> pip install cx_Oracle
(internet connection is compulsory)
	
= Verify this
(in Py.Interactive-Mode)
>>>help("modules")
(it provides complete modules available in our py-software)


==> MySQL Software installation::-
(MySQL 5.0 or later) latest is MySQL 8.0
(www.mysql.com/downloads/installer/)
NOTE:-
	1)install MySQL workbench 8.0.30
	2)install MySQL server 8.0.30
	(portno:3306)
	(uname:root; pwd:root; repwd:root)
	(service-name: MYSQL80)
	(Execute-button)

=> How to verify/open mysql8.0.30 cmd-line-utility::-
1)click-windows-start-btn -----> goto "MYSQL" folder ----> select "MySql command line client"

2) give pwd:root (for root-user)
3) 
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> use mysql;
Database changed

mysql> show tables;
+------------------------------------------------------+
| Tables_in_mysql                                      |
+------------------------------------------------------+
| columns_priv                                         |
| component                                            |
| db                                                   |
| default_roles                                        |
| engine_cost                                          |
| func                                                 |
| general_log                                          |
| global_grants                                        |
| gtid_executed                                        |
| help_category                                        |
| help_keyword                                         |
| help_relation                                        |
| help_topic                                           |
| innodb_index_stats                                   |
| innodb_table_stats                                   |
| password_history                                     |
| plugin                                               |
| procs_priv                                           |
| proxies_priv                                         |
| replication_asynchronous_connection_failover         |
| replication_asynchronous_connection_failover_managed |
| replication_group_configuration_version              |
| replication_group_member_actions                     |
| role_edges                                           |
| server_cost                                          |
| servers                                              |
| slave_master_info                                    |
| slave_relay_log_info                                 |
| slave_worker_info                                    |
| slow_log                                             |
| tables_priv                                          |
| time_zone                                            |
| time_zone_leap_second                                |
| time_zone_name                                       |
| time_zone_transition                                 |
| time_zone_transition_type                            |
| user                                                 |
+------------------------------------------------------+
37 rows in set (0.00 sec)


mysql> create database sampledb;
Query OK, 1 row affected (0.00 sec)
(Query means command)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sampledb           |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use sampledb;
Database changed

mysql> show tables;
Empty set (0.00 sec)

mysql> exit
(closes mysql-cmd-line client-app)
(butp-server-8.0.30 is still running, and we can connect from python-prog)




NOW,(*****)	
==> Steps for Pythons DB Programming:-
Step1:-
= Import DB specific DBase module
Ex:-
	import mysql.connector;
	import cx_Oracle;
	
	

Step2:-
= Make or Establish connection b/w Python-Program & DB
= It is done with connect() function
Ex:-
conn = mysql.connector.connect(host="localhost",user="root", password="root",port="3306",database="mydb");

(or)
conn = cx_Oracle.connect("scott/tiger@localhost/xe");/orcl



Step3:-
= For executing SQL-cmds and hold result, we use special-object of "Cursor" class
= For this cursor() function is used
Ex:-
	mycursor = conn.cursor();


Step4:-
= Now, execute SQL-queries using execute() of Cursor-class
Syntax:-
 execute(sqlquery); #Single-Query
 executescript(sqlqueries); #String of SQL-Queries with ;
 executemany(); #Executes Parameterized Query (with-vars)
Ex:-
	mycursor.execute("select * from employees");
		
=*** Once the command is executed from python-prog, cursor-object gets & stores(holds) the result

		
Step5:-
= Commit or rollback the transaction based on requirement (DML operations) i.e, insert/update/delete
Ex:-
	conn.commit()	#Saves changes to DB
	conn.rollback()	#Undo the changes to DB
	
Step6:-	
= Fetch/Getting the result-data using cursor object (for select-queries)
Ex:-
	fetchone()	#for single-row
	fetchall()	#for multiple-rows(list of rows)
	fetchmany(n)	#for first n-rows only
(Each-row is tuple)	
	
Ex1:-
	data = mycursor.fetchone();
	print(data);
Ex2:-
	data = mycursor.fetchall();
	for row in data:
		print(row);
Ex3:-
	data = mycursor.fetchmany(5);
	for row in data:
		print(row);		
		
Step7:-
= After DB-operations, it is recommended to close the resources used in program in reverse order of opening
Ex:-
	mycursor.close();
	conn.close();
	
Step8::-
= Finally, verify output of the DB program
	
	
NOTE:-
= Some important methods used in Python-DB Programming
Ex:-
	connect()
	cursor()
	------------
	execute()
	executescript()
	executemany()
	-------------
	commit()
	rollback()
	------------
	fetchone()
	fetchall()
	fetchmany(n)
	fetch()
	------------
	close()
=** These methods are common for different Databases



(just refer for understanding)
***********************************************************
==> Working with Oracle/MYSQL Database:-
= For making communication b/w Python-Programming and Databases, we required some translator 
(translates Python-Program calls to DB Specific calls & vice-versa)
= Technically it is called "Driver/Connector" 
==Diagram==
Python(prog-lang) ------<driver>------ Database(storage-s/w)


Ex:-
= For Oracle, we require "cx_Oracle" driver
= "cx_Oracle" is Python-Extension-Module
= It allows us to access Oracle DB
= Used in Python2 and Python3
= It works with all versions or Oracle (8,9,10,11,12,18,19 etc)

=> Installing cx_Oracle:-
= Open Windows Command-prompt (Not Python command-prompt)
= Use below commands,
Ex:-
cmd> pip install cx_Oracle
cmd> pip install cx_Oracle --upgrade
....
....
(Latest Version is : cx-Oracle-8.2.1)

=> Verify Installation:-
= From Python console(prompt), use this command
>>> help("modules");
(Provides list of all pre-defined modules installed in the system)
 
=> MYSQL Driver/Module:-
cmd> pip install mysql-connector-python
(8.0.27 is Last version)
cmd> pip install mysql-connector-python --upgrade
(8.0.27 is Last version)

(****)
MYSQL 5.5 or 8.0.30
==> Downloading & Installing MySQL softare::-
https://dev.mysql.com/downloads/installer/


C:\Program Files (x86)\MySQL\MySQL Server 5.5\bin>mysql -u root -p
Enter password: ****

NOTE:-
= Open oracle and mysql command-prompts


==> Working with MySQL DB directly::-
(DB-SQL-commands)
= to work with any DB directly, we use SQL commands

==> Open MYSQL Command Line::-
click(Start-button) ----> select MySQL from Programs ---> select MYSQL 5.5/8.0.30 ----> select "MYSQL command-line"
(enter pwd:root)

==> Some basic commands::-
mysql> show databases;
(4-default-DBs)

mysql> use test;
Database changed

mysql> show tables;
Empty set

mysql> exit
(closes mysql-cmd-line)
***********************************************************




==>> Start with Programming::-
=*** For mysql use port=3306/3308 for connection
//Programs on PDBC with MySQL/Oracle(32-bit)
Ex1:-
#Program (DBEx1.py)
(Program to connect with MYSQL and print its version)

NOTE:-
= MySQLConnection is a class, using which we store connection obj. to MYSQL DB
"""
#Program (DBEx1.py)
#Program to connect with MySQL and print its version/connection)


#MySQL
import mysql.connector;	#module for mysql
conn = mysql.connector.connect(host="localhost",user="root", password="root",port=3306);

print(conn);
print(type(conn))

conn.close();

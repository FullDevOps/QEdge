# 21st day 21.17-08-22

"""
==> Constructor inside class:- (__init__())
(Refer-notes)
= It is special-method in a class
= Its name is __init__(self)
= It is executed automatically when object is created
(s1 = Student())
#Student() -> Student-class constructor
= Its main purpose is declare and initialize instance-variables(obj-vars)
(rollno/name/height)
= It is executed only once per object creation (auto)
= It takes atleast 1-parameter 
i.e, self(current-obj Ex:- s1/s2)
= It is optional in a class, If it is not given then python provides default-constructor
Ex:-
	def __init__(self):
		pass;	#body-w.o-stmts
"""
##Program (ConstructorEx1.py)
##Program to define constructor in python-class
##Program (ConstructorEx1.py)
##Program to define constructor in python-class

class A:
	'''class-A definition'''
	def __init__(self):
		print("Class-A constructor is called");
		self.x=int(input("Enter X value :: "));
		self.y=int(input("Enter Y value :: "));
	def show(self):
		print(self.x,self.y)
		

#obj-creations		
obj1 = A()		#__init__() constructor is call auto	
obj2 = A()
obj3 = A()

print()
print("Obj1-data");
obj1.show();
	
print()
print("Obj2-data");
obj2.show();

print()
print("Obj3-data");
obj3.show();

"""
------------------------------------------------------
==> Constructor with input-parameters::-
-------------------------------------------------
(refer-notes)
= constructor is sp.method of a class (__init__())
= it is called automatically, when object is created
Ex:-
	s1 = Student(); #Student-class const-call
= constructor is used to declare & initialize instance-variables(obj-vars)
= for constructor, "self"(current-obj) is 1st-para
= for this constructor, we can pass our own  extra-input-parameters
Ex:-
	def __init__(self,r,n,h):
		self.rollno=r;
		self.sname=n;
		self.height=h;
=*** we can use these extra-input-parameters, to initialize our instance-variables(obj-vars)
"""	

##Program (ConstructorEx2.py)
##Program to define constructor with para(args) in python-class
##Program (ConstructorEx2.py)
##Program to define constructor with para(args) in python-class

class Student:
	'''Student-class definition'''
	def __init__(self,r,n,h):
		self.rollno=r;
		self.sname=n;
		self.height=h;
	def display(self):
		print(self.rollno,self.sname,self.height)
		

s1 = Student(1001,"Sai",6.0); #i/p-para to const.
s2 = Student(1002,"Ram",5.9);

print("s1-details");
s1.display();
print()
print("s2-details");
s2.display();

"""
NOTE:-
= for __init__(self,....) constructor, current-obj(s1/s2) is passed auto to self(1st-para)

NOTE:-
= We can take input-parameters to constructors same-names as that of instance-variables(obj-vars)
Ex:-
	def __init__(self,rollno,name,height):
		self.rollno=rollno;
		self.name=name;
		self.height=height;
(obj-vars are assigned with local-vars)	
"""


"Assignment"
#Employee2.py
#Program to demo Employee-class with constructor input-parameters, instance-vars, instance-methods & self-var using objects
# (empno,ename,job,sal)
e1 = Employee(1122,"Sai Kumar","Manager",6500.50)
e2 = Employee(1133,"Ram Kumar","HR",5500.50)


"Assignment"
#Customer2.py
#Program to demo Customer-class with constructor input-parameters, instance-vars, instance-methods & self-var using objects
# (custid,custacno,custname,custbal)
c1 = Customer(123456,9876543210,"Sai",50000)
c2 = Customer(112233,9988776655,"Ram",60000)


"""
=====================================================
==> self variable in Methods:-
= it is sp-var of a class
= is used as input-parameter to constructor & methods
Ex:-
	def __init__(self):
		.....
	def display(self):
		.....
= self means current-obj under execution
===Diagram===
s1 = Student()
s2 = Student()
s3 = Student()
s1.display()
s2.display()
s3.display()

NOTE:-
= it is sp-obj-ref-var of a class
= it is used only inside a class
"""
##Program (Student11.py)
#Program to demo self-var in Methods of a class

#class-def
class Student11:
	"Student11 class definition"
	def __init__(self,rollno,name,height):
		self.rollno=rollno;
		self.name=name;
		self.height=height;	
		
	def display(self):
		print("RollNo : {}\nName : {}\nHeight : {}".format(self.rollno,self.name,self.height) );
	
s1 = Student11(1001,"Sai",6.0);
s2 = Student11(1002,"Ram",5.9);
s3 = Student11(1003,"Ali",5.6);
print()
s1.display()
print()
s2.display();
print()
s3.display()

"""
==> Difference between Constructors & Methods:-
(refer-notes)
1)
= Constructor name is fixed-name __init__()
= Method-name can be any user-defined name (display()/accept()/show())
2)
= Constructor is called & executed automatically when object is created (s1 = Student())
= Method is called manually & executed (s1.display())
3)
= Constructor is called & executed only once per object
= Method can be called & executed any no.of times per object
4)
= Constructor is used to declare and initialize Instance-Variables(obj-var)
= Method is used to write Buss.Logic in a class


----------------------------------------------------------
**==> Types of Variables in a Python-class:-
= In python-class, we have 3-types of variables,
1) Instance-Variables (Object-Vars)	#separate for every-obj
2) Static-Variables (Common-Vars)	#common for all-objs
3) Local-Variables (Method-Vars)	#define inside-a-method
-------------------------------------
4) Class-vars (sp-vars inside class-methods)



(Working with Instance-Variables)
=>1) Instance-Variables:- (Object-Level Vars)
(Refer-notes)
= Instance means Object
(Hence called as Object-vars)
= They are separate for every object of a class (separate-copy)
==Diagram== (rollno,name,height)
s1 = Student();		s1 -----> [(rollno,name,height)]
s2 = Student();		s2 -----> [(rollno,name,height)]
s3 = Student();		s3 -----> [(rollno,name,height)]

=> How to work(use) with Instance-Vars??
i) Inside class with self-var
ii) Outside class with obj.ref.var.name
"""

##Program (InstanceVarsEx1.py)
##Program to define & work with instance-vars in python-program(class)
##Program (InstanceVarsEx1.py)
##Program to define & work with instance-vars in python-program(class) 3-cases

class Student:
	def __init__(self):	
		self.rollno=1001;
		self.sname="Sai";
		self.height=6.2;
	def display(self):
		print(self.rollno,self.sname,self.height);
		

#case-1(inside class)
s1 = Student()
print("s1-obj details ::");
s1.display() 

#case-2(outside class) #it is not advisable
print()
s2 = Student()
s2.rollno=1002
s2.sname="Ram"
s2.height=5.9
print("s2-obj details ::");
print(s2.rollno,s2.sname,s2.height);



"Assignment"
##Program (InstanceVarsEx2.py)
####Program to define instance-vars in python-program(class) 3-cases using Employee-class
# (empno,ename,job,sal)

"Assignment"
##Program (InstanceVarsEx3.py)
####Program to define instance-vars in python-program(class) 3-cases using Customer-class
# (cacno,cname,bal,caddr)

"""
======================================================
==>2) Static-Variables (Common Vars):-
**= These Variables are common for all the objects of a class
***= Such vars are declared directly in a class 
(basically w.o constructor or w.o method)
= For all objs only 1-copy of memory is allocated and shared with all objs of that class

=> How to access(use)??
	(2-ways)
	=** Static-Variables are accessed with 
		Classname or 
		Objname
	(Classname is preferable) 
	(Both inside/outside class)
	
==Diagram==
[s1:-rollno/name/height]--->[course,college]<-----[s2:-rollno/name/height]
[s3],[s4]
#here course/college etc are static-vars of a class
#here rollno/name/height are instance-vars
"""
# //Program
##Program (StaticVarsEx1.py)
#Program to demo Static-Vars in a python-class

class StaticVars:
	'''Static-Variables in a python-class'''
	c=11;	#c is static-var(common-var for all objs)
	def __init__(self):
		self.x=10;
		self.y=20;
	def display(self):
		print(self.x);
		print(self.y);
		print(StaticVars.c);	#self.c
	
	
obj1 = StaticVars();		#obj1---->[x:10,y:20]<----(C:11)
print("For obj1 ::");
obj1.display();

print();
obj2 = StaticVars();	
#obj2---->[x:10,y:20]<----(C:11)
obj2.x=100;
obj2.y=200;
#obj2---->[x:100,y:200]<----(C:11)
print("For obj2 ::");
obj2.display();

print()
print("Using Classname or Obj.name ::");
print(StaticVars.c);
print(obj1.c);
print(obj2.c);


print()
#sp-case1
#modify static-var using classname
StaticVars.c=22		
print("After modify class-var using classname");
print(StaticVars.c);
print(obj1.c);
print(obj2.c);

print()
#sp-case2
print("Modify instance-var using obj1");
obj1.x=1000
obj1.y=2000
obj1.display();
obj2.display();



# NOTE:-
# = Instance-Vars are separate-copy for every-object
# = Static-Vars are common-copy(sharable) for all-objects
# = Changes(Modify) done to Instance-Vars are updated to that obj only
# = Changes(Modify) done to Static-Vars are updated to  every-obj




"""
============================================================================================================
***3) Local-Variables:-
= Variables declared/defined inside particular-method of a class is called Local-Variables (Method-Vars)
= Such vars are created when method is executed and destroyed once method execution is completed
= Local-Variables have local-access and direct-access in that method-only but not outside the method
(input-para/args are also local-vars)
(local-access & direct-access)

Ex:- 
"""
##Program (LocalVariables.py)
#Prog to demo Local-Variables inside method of a class

class LocalVariables:
	'''LocalVariables class-definition'''
	def m1(self):
		print("Inside m1() of class")
		x=10;		#x is local-var to m1()
		print(x);
		#print(y)
	def m2(self):
		print("Inside m2() of class")
		y=20;		#y is local-var to m2()
		print(y);	
		#print(x);	#NameError... (x is not-defined)
		
obj = LocalVariables();
obj.m1();
obj.m2();



# NOTE:-
# = Instance-Vars use obj-name(self)
# = Class-vars use Classname
# = Local-vars use direct-name (No obj-name, No classname)








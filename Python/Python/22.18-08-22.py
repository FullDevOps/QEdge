# 22nd day 22.18-08-22

"""
***==> Types of Methods in a Python-class:-
= In class, we have 3-types of methods,
1) Instance-Methods (obj-methods)
2) Static-Methods (common-methods)
3) Class-Methods  (sp-methods with class-var)


1) Instance-Methods:-
(Instance means object)
= Methods whose Functionality(work) is diff. for every object are called Instance-Methods
= For Instance-Methods, we pass "self" variable (as 1st-para)
(self is current-obj)
Ex:-
def m1(self):	#self means current-obj under execution
def display(self):
= In these methods, we access instance-vars using "self" var
s1[self.rollno/name/height]
s2[self.rollno/name/height]
....
= Accessing them,
	a) Inside class using self-var	(self.m1())
	b) Outside class using Obj.Ref.Var.Name (s1.display())

Ex:-
"""
##Program (InstanceMethods1.py)
# (Prog to define Instance-Methods in a class)
#Prog to define Instance-Methods in a class

class Student:
	def __init__(self,rollno,name,avg):
		self.rollno=rollno;
		self.name=name;
		self.avg=avg;
	def display(self):
		print(self.rollno);
		print(self.name);
		print(self.avg);
	def grade(self):
		if(avg>=75):
			print("Distinction");
		elif(avg>=65):
			print("1st Class");
		elif(avg>=50):
			print("2nd Class");	
		elif(avg>=35):
			print("3rd Class");
		else:
			print("FAILED");

n = int(input("Enter No.of Students :"));
for i in range(n):
	rollno=int(input("Enter-Rollno :"));
	name=input("Enter-Name :");
	avg=float(input("Enter-Avg-Marks :"));
	studObj = Student(rollno,name,avg);
	studObj.display();
	studObj.grade();
	print();

# NOTE:-
# = For Instance-Methods, compulsory we have self(input-parameter)


"""
===>>
2) Static-Methods:-
= They are general utility methods 
(common func. for all objs of a class)
= Such methods are declared with "@staticmethod" decorator
= Here we do-not pass "self" as input-parameter
= In this method, we DO-NOT use instance-vars
=> Accessing:-
	a) Using Classname	Ex:- Classname.staticmethod()
	b) Using Obj.Ref.Var	Ex:- obj.staticmethod()
	=**	preferable is class-name
	
Ex:-
"""
##Program (StaticMethods.py)
#Prog to demo Static-Methods in a class

class StaticMethods:
	@staticmethod
	def sum(x,y):
		print(x+y);
	@staticmethod
	def sub(x,y):
		print(x-y);
	@staticmethod
	def prod(x,y):
		print(x*y);	

#using classname(w.o creating obj -> preferable)
print("Using Classname");
StaticMethods.sum(11,3);
StaticMethods.sub(11,3);
StaticMethods.prod(11,3);

print()
#using obj-ref-name
print("Using Obj.Name");
obj = StaticMethods();
obj.sum(11,33);
obj.sub(11,33);
obj.prod(11,33);


"""
==>>
3) Class Methods:- (with class-var(special))
= In this method, we mainly use/access Static-Vars/Methods of class or create object of a class
= It is declared using "@classmethod" decorator (annotation)
= For such methods, we provide sp.class-variables as parameter
(sp-var as parameter known as class-method class-ref-var)
(it is 1st parameter, mainly used to access static-vars/methods of class)
(class-ref-var acts like classname)
(it refers to class-def in memory)
= it can take parameters (after class-method-class-var)
=> Accessing,
	a) Using classname	Ex:- Classname.classmethod()
	b) Using Obj.Ref.Var Ex:- obj.classmethod()
	(preferable is Classname)
Ex:-
"""
##Program (ClassMethods.py)	
#Prog to demo Class-Methods in a class

class ClassMethods:
	c=11;	#static-var(common for all objs of class)
	def __init__(self):
		self.x=10;	#instance-vars
		self.y=20;
	@staticmethod
	def m1():
		print("Static-Method m1()")
	def m2(self):
		print("Instance-Method m2()",self.x,self.y)
	@classmethod
	def m3(clsvar):
		print("Static-Var :",ClassMethods.c,clsvar.c);
		ClassMethods.m1()
		clsvar.m1()
		obj1 = ClassMethods();
		obj1.m2()
		obj2 = clsvar()
		obj2.m2()
		
	
#using classname
ClassMethods.m3();
print()
#obj-ref-var
obj = ClassMethods()
obj.m3()


"""
NOTE:-
= Instance-Methods & Static-Methods are mainly used in a class
= Class-Methods are rarely used in a class(Sp-case with class-var)

======================================================
==> Passing Object of One-class to Another-class:-
(Passing class-object as parameter to method)
= We can pass object of one-class to another-class and access its members in another-class using obj as parameter to method
= Adv, is Reusability of code
(i.e, re-use one class members in another-class)
==Diagram==

Ex:-
"""
##Program (ObjectAsPara.py)
#Prog to demo passing object as parameter

#1st-class
class Student:
	def __init__(self,rollno,name,height):
		self.rollno=rollno;
		self.name=name;
		self.height=height;
	def show(self):
		print(self.rollno);
		print(self.name);	
		print(self.height);
	
#2nd-class(here we use 1st-class)
class Demos:
	@staticmethod
	def update(studobj):	#studobj=s1(alias)
		studobj.height=studobj.height+0.2;
		studobj.show();	


#main-prog
s1 = Student(1001,"Sai",6.0);
s1.show();
print()
Demos.update(s1);
print()
s1.show();

"""
NOTE:-
= Here any changes done with formal-parameter object-ref(studobj) are updated/reflected to actual-argument object-ref(s1)


====================================================
==>> Inner-Classes in Python:-
= Defining one-class inside another-class is called Inner-Class
(class-with-in-class)
Ex:-
class Car:	#outer-class
	....
	....
	class Engine:	#inner-class
		....
		....
= Here without "class Car", there is no-chance of "class Engine"
NOTE:-
=** Hence, Inner-class are part of Outer-class
= Hence Inner-Class obj is created using Outer-class obj
Syntax:
	outObj = OuterClass();	#1st create obj of outer-class
	inObj = outObj.InnerClass();	#2nd using outer-class 
							#object create inner-class obj
							
Ex:-
"""
##Program (InnerClass.py)
#Program to demo Inner-Class

class Outer:
	def __init__(self):
		print("Outer-class-Constructor obj created");
	class Inner:
		def __init__(self):
			print("Inner-class-Constructor obj created");
		def m1(self):
			print("Inner-Class m1() method");


#case-1		
out = Outer();		#step1
inn = out.Inner();	#step2
inn.m1();
'''

'''
#case-2(w.o using Outer-class obj.ref.name)
inn2 = Outer().Inner();
inn2.m1();


#case-3(w.o both Outer-class & Inner-class obj.ref.var)
Outer().Inner().m1();



# NOTE:- (prev-program)
# = We can access Inner-Class members in different ways,
# 1) (with obj.ref's)
out = Outer();
inn = out.Inner();
inn.m1();
# 2) (with only inner-class obj-ref)
inn = Outer().Inner();
inn.m1();
# 3) (w.o any obj-refs)
Outer().Inner().m1();





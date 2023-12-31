# 23rd day 23.19-08-22

"""
==> Garbage Collection:-
= It means deleting unnecessary objects from program during execution and saving the memory for performance of prog (speedy-execution)
= In traditional P.Langs like C/C++, programmer does GC manually
(Hence, we had OutOfMemory issues)

= In python, it is done automatically in background using GC-Assistant (destroys useless objs)
= If any obj does not have any reference-var then such obj is eligible for GC
Ex:-
	s1[] ---> [rollno/name/height]
	del s1;
	s1[] 		 [rollno/name/height] is ready for GC
	
=> How to enable/disable GC in Python-prog?
= By default GC is enabled in program, however we can disable it also
= "gc module" is used for this and below methods,
1) gc.isenabled()	#gives True if it is enabled
2) gc.disable()		#disables GC explicitly
3) gc.enable()		#enables GC explicitly

Ex:-
"""
##Program (GCEx1.py)
# (Prog to demo GC)
#Prog to demo GC

import gc;
import time;

print(gc.isenabled());
time.sleep(5);

gc.disable();
print("GC is disabled in program");
time.sleep(5);
print(gc.isenabled());

gc.enable();
print("GC is Enabled in program");
time.sleep(5);
print(gc.isenabled());

"""
========================================================
==> Destructor in Python-Class:-
= It is special method to remove/close unnecessary resources/objs in a program
= It is,
Ex:
	__del__(self):
		...
		...
		...
= Just before destroying any object in program by GC, GC always calls destructor-method to perform cleaning-activity
Ex:- (closing DB-conn, Network-conn, close-files etc)
= Once destructor-method execution is done, GC automatically destroys that unnecessary-object

NOTE:-
= destructor-method does only cleaning-activity but not actual destroying of object

[cleaning-activity(closing-objs) ------> destroying-objs]
(it is called automatically in program)

Ex:-
"""
##Program (DestructorEx1.py)
# (Prog to demo destructor-method)
#Prog to demo destructor-method

import time;
class Demo:
	def __init__(self):
		print("Object Created & Initialized");
	def __del__(self):
		print("Object Resource Cleaning is getting done...");
	
obj1 = Demo();
obj2 = Demo();
time.sleep(5);
time.sleep(5);
print("End of Prog");

"""
NOTE:-
= destructor-method (__del__) is automatically called at end-of the program & then finally GC is done automatically in memory


====================================================
***==> Using members of one-class inside Another-class:-
(class-members =vars + methods)
Ex:-
	class A (x,y,m1())
	class B (p,q,m2())
(How to use class-A members(x,y,m1) in class-B)

=** It is done in 2-ways,
1) By Composition (has-a-relationship)
2) By Inheritance (is-a-relationship/kind-of-relationship)


Now,
***1) By Composition:::- 
(Has-a-relationship):-
(Having object of another class in our class)
= By using Classname or by creating object of another class in your class
= Advantage is, "Code-Reusability"
"""
###Program (CompositionEx1.py)
# (Prog to demo composition)

###Program (CompositionEx1.py)
#Prog to demo composition in python-classes (using object/classname)

class A:
	def __init__(self):
		self.x=10;
		self.y=20;
	def m1(self):
		print("Class-A m1() method",self.x,self.y);

class B:
	def __init__(self):
		aobj1=A();		#inside const create obj
		aobj1.m1();
	def m2(self):
		aobj2=A();		#inside method create obj
		aobj2.m1();
	@staticmethod
	def m3(aobj3):		#obj as para(aobj3=aobj)
		aobj3.m1()
	
#case-1
bobj = B();

print()
#case-2
bobj.m2()

print()
#case-3
aobj= A();
B.m3(aobj)

"""
========================================================
2) By using Inheritance (is-a-relationship):-
(child-class is-a kind-of base-class)
Def:-
	= Getting data-props(vars), methods and constructors from Parent-class to Child-class is called Inheritance
= Hence Parent-class members can be Re-used in child-class
= Child-class extends Parent-class Functionality
= Child-class is more powerful than Parent-class functionality

==Diagram==
	class A		(Parent) x,y,m1()		#Base/Super
		|
		|
	class B(A) (Child)	p,q,m2() + x,y,m1()	#Derived/Sub

Syntax:-
	class Childclass(Parentclass):

=** Just create child-class object and access both Parent-class members & Child-class members
= Advantage, is Re-usability of code w.o PC object

Ex:-
##Program (InheritanceEx1.py)	
(Prog to demo Inheritance)
=** W.O Base-class object, only with child-class object, we can access B.C members in S.C using its object (Re-usability)


NOTE:-
= All the methods of Parent-class are available to Child-class
= Hence using Child-class obj.ref.var we can access both Parent-class methods and Child-class methods
Ex:-
//Program (InheritanceEx1.py)
(Prog to demo Inheritance)

NOTE:-
= Like methods, from Parent-class vars (data-props) are available to Child-class
Ex:-
"""
# //Program (InheritanceEx1.py)
# (Prog to demo Inheritance)
##Program (InheritanceEx1.py)	
#Prog to demo Inheritance in python-coding


#case-1 (PC all mem in Child-class)
class Pclass:
	a=10;
	def __init__(self):
		self.b=20;
	def m1(self):
		print("Parent-class Instance m1() Method");
	@classmethod
	def m2(self):
		print("Parent-class Class m2() Method");
	@staticmethod
	def m3():
		print("Parent-class Static m3() Method");
		
class Cclass(Pclass):
	pass;		#indicates body W.O any stmts
	#in child-class (a,b,m1,m2,m3 are inherited)

cobj = Cclass();
print(cobj.a);
print(cobj.b);
cobj.m1();
cobj.m2();
cobj.m3();
'''


'''
#case-2
class Pclass:
	def m1(self):
		print("Parent-class m1() instance-method");
class Cclass(Pclass):
	def m2(self):
		print("Child-class m2() instance-method");

obj = Cclass();
obj.m1();
obj.m2();


#case-3(***)
class Pclass:
	a=10;
	def __init__(self):
		self.b=20;
	
class Cclass(Pclass):
	c=30;
	def __init__(self):
		super().__init__(); #calls BC/PC constructor
		self.d=40;

obj = Cclass();
print(obj.a);
print(obj.b);
print(obj.c);
print(obj.d);


# NOTE:-
# = using super() function, we can call parent-class constructors/methods with same-name in child-class from child-class
# = If we comment the line "super().__init__();" then "var b" is not available to Child-class


"""
========================================================================================
===> Parent-Child Constructors:-
(sp-cases in Inheritance)
= Whenever we are creating Child-class objs then child-class constructor is executed
==Diagram===
= If there is no child-class constructor then parent-class constructor is executed auto.
(but parent-class obj is not created)
==Diagram===
= From child-class constructor, we can reuse parent-class constructor using super() function
==Diagram===
"""

# Ex:-
##Program (ParentChildConstructor.py)
#Prog to demo Parent and Child-class constructors

class A:
	def __init__(self):
		print("parent-class constructor");
		print(id(self));
		print(type(self));

class B(A):
	def __init__(self):
		super().__init__()
		print("child-class constructor");
		print(id(self));
		print(type(self));
	#pass;		#body W.O any stmts

	
obj = B();
print()
print(id(obj));	
print(type(obj));



# NOTE:-
# = pass stmt indicates body without any stmts



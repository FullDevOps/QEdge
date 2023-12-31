# 24th day 24.20-08-22

"""
==> Types of Inheritance:-
(PC----->CC)
= Python has 6-types of Inheritance. They are,
1) Single Inheritance
2) Multi-Level Inheritance
3) Hierarchical Inheritance
4) Multiple Inheritance
5) Hybrid Inheritance
--------------------------
6) Cyclic Inheritance (Not-supported)


**********
1) Single Inheritance:-
= In this, single parent-class gives derivation to single child-class
==Diagram==
	class A:	#1-PC(x,y,m1())
		|
		|
	class B(A):	#only 1-CC (p,q,m2() + x,y,m1())
	
obj = B()
obj.x
obj.y
obj.m1()
-----------
obj.p
obj.q
obj.m2()
"""

# Ex:-
##Program (SingleInheritance.py)
#Prog to demo Single-Inheritance (Single PC --> Single CC)

class A:
	def __init__(self):
		self.x=10;
		self.y=20;
	def m1(self):
		print("Parent-class-A m1() Method",self.x,self.y);
class B(A):
    #x,y,m1,__init__()
	def __init__(self):
		super().__init__()
		self.p=100;
		self.q=200;
	def m2(self):	#m1() is inherited from class-A
		print("Child-class-B m2() Method",self.p,self.q);
		
obj = B();
obj.m1();
obj.m2();		

		

"""
2) Multi-Level Inheritance:-
= In this, it is extension of Single-Inheritance, in which Child-class acts a Parent-class for next-derivation(next-child-class)
==Diagram==
	class A:	#PC	(level-0) x,y,m1()
		|
		|
	class B(A):	#CC	(level-1) p,q,m2() + x,y,m1()
		|
		|
	class C(B):	#CC	(level-2) m,n,m3()+p,q,m2() + x,y,m1()
	
obj = C();
obj.x,y,m1()
obj.p,q,m2();
obj.m,n,m3();	
	
	
Ex:-
"""
##Program (MultiLevelInheritance.py)
#Prog to demo Multi-Level-Inheritance

class A:
	def __init__(self):
		self.x=10;
		self.y=20;
	def m1(self):
		print("Parent-class A m1() Method",self.x,self.y);
class B(A):
	def __init__(self):
		super().__init__()
		self.p=100;
		self.q=200;
	def m2(self):	#m1()
		print("Child-class B m2() Method",self.p,self.q);
class C(B):
	def __init__(self):
		super().__init__()
		self.m=1000;
		self.n=2000;
	def m3(self):	#m1(), m2()
		print("Child-class C m3() Method",self.m,self.n);
		
obj = C();
obj.m1();
obj.m2();
obj.m3();


"""
3) Hierarchical Inheritance:-
= In this, single Parent-class gives derivation to multiple Child-classes
==Diagram==
			class A:	(x,y,m1)
				|
				|
		---------------------
		|					|
	class B(A):		   class C(A):
	p,q,m2()/x,y,m1()	m,n,m3()/x,y,m1()
	
obj1=B() ---> obj.x,y,m1,p,q,m2
obj2=C() ---> obj.x,y,m1,m,n,m3	

"""
# Ex:-
#Program (HierarchicalInheritance.py)
#Prog to demo Hierarchical-Inheritance


class A:
	def __init__(self):
		self.x=10;
		self.y=20;
	def m1(self):
		print("Parent-class A m1() Method",self.x,self.y);
class B(A):
	def __init__(self):
		super().__init__() #x,y
		self.p=100;
		self.q=200;
	def m2(self):	#m1()
		print("Child-class B m2() Method",self.p,self.q);
class C(A):
	def __init__(self):
		super().__init__() #x,y
		self.m=1000;
		self.n=2000;
	def m3(self):	#m1()
		print("Child-class C m3() Method",self.m,self.n);

print("Using class-B obj1 :");
obj1 = B();
obj1.m1();
obj1.m2();
print()
print("Using class-C obj2 :");
obj2 = C();
obj2.m1();
obj2.m3();

"""
4) Multiple Inheritance:-
= In this, multiple Parent-classes gives derivation to single Child-class
==Diagram==
	class A: m1()	class B: m2()
		\			/
		 \		   /
		class C(A,B): m3()[m1,m2]

# Ex:-
//Program (MultipleInheritance.py)
(Prog to demo Multiple-Inheritance)

***NOTE:-
= If same method-name/__init__() is inherited from both Parent-classes then 1st-parent-class method in order is considered or taken in Child-class

Ex:-
"""
#Prog to demo Multiple-Inheritance
#Program (MultipleInheritance.py)


#basic-case
class A:
	def __init__(self):
		self.x=10;
		self.y=20;
	def m1(self):
		print("Parent-class A m1() Method",self.x,self.y);
class B:
	def __init__(self):
		self.p=11;
		self.q=22;
	def m2(self):
		print("Parent-class B m2() Method",self.p,self.q);
		
class C(A,B):	#A is 1st Parent-class & B is 2nd Parent-cls 
	def __init__(self):
		super().__init__() #x,y but not p,q
		self.m=100;
		self.n=200;
		
	def m3(self):
		print("Child-class C m3() Method",self.m,self.n);

		
class D(B,A):	#B is 1st Parent-class & A is 2nd Parent-cls 
	def __init__(self):
		super().__init__() #p,q but not x,y
		self.r=111;
		self.s=222;
	def m4(self):
		print("Child-class D m4() Method",self.r,self.s);

print("Using class-C obj1");		
obj1 = C();
obj1.m1();
#obj1.m2();
obj1.m3();

print()
print("Using class-D obj2");		
obj2 = D();
#obj2.m1();
obj2.m2();
obj2.m4();




#sp-case in multiple-inheritance
#Prog to demo Multiple-Inheritance with same-method-names(m1()) in multiple-Parent-Classes(A,B)

class A:
	def m1(self):
		print("Parent-class A m1() Method");
class B:
	def m1(self):
		print("Parent-class B m1() Method");
class C(A,B):
	def m3(self):	#1st-Parent-class(A) m1() only
		print("Child-class C m3() Method");
class D(B,A):		
	def m4(self):	#1st-Parent-class(B) m1() only
		print("Child-class D m4() Method");		
		
obj1 = C();
obj1.m1();
obj1.m3();
print()
obj2 = D();
obj2.m1();
obj2.m4();



"""
NOTE:-
= In multiple-inheritance, we can access only 1st parent-class constructor at a time from child-class constructor
i.e, 
	super().__init__()
(alternatively take accept1() & accept2() method in Parent-Classes to define instance-vars)

=*** whenever we have same-method-name in multiple parent-classes, in child-class it takes only 1st-parent method but not 2nd-parent-method


5) Hybrid Inheritance:-
= In this, it is combination of 2 or more single, multi-level, hierarchical, multiple inheritances
==Diagram==
				class A:	[m1]
					|
				class B(A):	[m2]m1
				/		  \	
			class C(B):	  class D(B):	
			m3[m1,m2]		m4[m1,m2]

A--->B (Single-Inheritance)
B--->C,D (Hierarchical-Inheritance)

Ex:-
"""
# //Program (HybridInheritance.py)
# (Prog to demo Hybrid-Inheritance)
#Prog to demo Hybrid-Inheritance
#Program (HybridInheritance.py)

class A:
	def m1(self):
		print("Class A m1() Method");
class B(A):
	def m2(self):	#m1
		print("Class B m2() Method");
class C(B):
	def m3(self):	#m1,m2
		print("Class C m3() Method");
class D(B):
	def m4(self):	#m1,m2
		print("Class D m4() Method");		
		
print("Using Class-C obj1 :");		
obj1 = C();
obj1.m1();
obj1.m2();
obj1.m3();
print("Using Class-D obj2 :");
obj2 = D();
obj2.m1();
obj2.m2();
obj2.m4();

"""
6) Cyclic-Inheritance:-
= In this, inheritance is done in cyclic way
= It is not supported in Python (as it is not required)
Ex:-
class A(A):		#Here we get Name-Error ('A' is not defined)
	pass;
= inheritance to itself

Ex:- (A->B and vice-versa)
==Diagram==
class A(B):		#Here we get Name-Error ('B' is not defined)
	pass;
class B(A):	
	pass;
= inheritance again-back to itself



(****sp-cases*****)
**==> super() function:-
(it is used in inheritance concept)
(Parent-class & Child-class)

=** It is pre-defined method, using which we can call/access parent-class constructors, vars and methods from child-class
(provided Parent-class & Child-class have same member-names)

=> CASE1::- (PC & CC const.&method same-names)
Ex1:-
#Program (SuperEx1.py)
NOTE:-
= Here using super(), we are accessing parent-class constructor and display() provided they have same-name
"""
#Program to demo super()
#Program (SuperEx1.py)

class A:		#1-const, x,y prop, 1-display(self)
	def __init__(self,x,y):
		self.x=x;
		self.y=y;
	def display(self):
		print(self.x);
		print(self.y);

class B(A):
	def __init__(self,x,y,p,q):
		super().__init__(x,y);
		self.p=p;
		self.q=q;
	def display(self):
		super().display();
		print(self.p);
		print(self.q);
		
bobj = B(10,20,100,200);
bobj.display();


"""
**CASE-2**
Ex2:-
#Program (SuperEx2.py)
NOTE:-
= Here super(), is used to call various members of Parent-class (instance/static/class)
"""
#Program (SuperEx2.py)
#Program to demo super() with P.C any members

class A:
	x=10;
	def __init__(self):
		self.y=20;
		print(self.y);
	def m1(self):
		print("Pclass-A m1() instance-method");
	@classmethod	
	def m2(clsvar):
		print("Pclass-A m2() class-method");	
	@staticmethod	
	def m3():
		print("Pclass-A m3() static-method");	
		
class B(A):
	def __init__(self):
		print(super().x);
		super().__init__();
		super().m1();
		super().m2();
		super().m3();
		
bobj = B();



"""
=> Case-3
=>Ex3:-
==> How to call method of a particular Parent-class:-
= In multiple-parent-classes, how to access particular parent-class members with same-name using super()
==Diagram===
	A m1()
	|
	|
	B m1()
	|
	|
	C m1()
	|
	|
	D m1()
	|
	|
	|
	E** m1(), m1(),m1(),m1(),m1()


= We use below cases,
1) super(D,self).m1();
= It calls m1() of Parent-class of class-D
2) A.m1(self);
= It calls m1() of Parent-class-A
=** in both the case self-var is compulsory
"""
# Ex:-
#Program (SuperEx3.py)
#Program (SuperEx3.py)

class A:
	def m1(self):
		print("Class-A m1()");
class B(A):
	def m1(self):
		print("Class-B m1()");
class C(B):
	def m1(self):
		print("Class-C m1()");		
class D(C):
	def m1(self):
		print("Class-D m1()");
class E(D):
	def m1(self):
		print("Class-E m1()");
		A.m1(self);
		B.m1(self);
		C.m1(self);
		D.m1(self);
		print()
		super(C,self).m1();  #***

eobj = E();
eobj.m1();		










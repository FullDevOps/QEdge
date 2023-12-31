# 26th day 26.23-08-22

"""
3) Overriding in Python-Polymorphism:-
(related to Inheritance i.e, PC & CC)
= It is done in 2-ways,
i) Method-Overriding
ii) Constructor-Overriding


i) Method-Overriding:- (Re-placing/Re-Writing)
= This concept is related to Inheritance (BC & SC)
= Parent-class members are available to Child-class
Def:-
	Re-defining Parent-class methods in Child-class with same-name & same-signature is called Method-Overriding
(here no-of-args, dtype-of-args, order-of-args SAME)
= Hence, always Child-class methods are more powerful than Parent-class methods

Ex:-
"""
# //Program (MethodOverriding1.py)
#Program (MethodOverriding1.py)
#Program to demo Method-Overriding in Inheritance

class Pclass:
	def m1(self):	#0-args
		print("Parent-class m1() method");
		
class Cclass(Pclass):
	def m1(self):	#0-args redefined
		print("Child-class powerful m1() method");
		super().m1();
		
obj = Cclass();
obj.m1();		


# NOTE:-
# = From Child-class Overriding methods, we can call Parent-class Overridden methods using super() method

"""
ii) Constructor-Overriding:- (re-placing/re-writing in SC)
= This concept is related to Inheritance (BC & SC)
= Parent-class members are available to Child-class

Def:-
	Re-defining Parent-class constructor in Child-class with same-name & same-signature is called Constructor-Overriding
(here no-of-args, dtype-of-args, order-of-args SAME)

= Here we redefine powerful-constructor in sub-class

Ex:-
//Program (ConstructorOverriding1.py)
#Program (ConstructorOverriding1.py)

class Pclass:
	def __init__(self):     #0-args
		print("Parent-class Constructor");
        
class Cclass(Pclass):
	pass;
	#def __init__(self):     #0-args
	#	print("Child-class Constructor");
	#	super().__init__();
	
obj = Cclass();


NOTE:-
= If Child-class does not have constructor then Parent-class constructor is executed
= Also from Child-class constructor, we can call Parent-class constructor using super()


========================================================
***Abstraction***
------------------------
def:- 
	Hiding unncecessary things in an object & exposing only necessary things outside the object 

= In python, abstraction is done in 2-ways,
	1) abstract-classes (with abstract-methods)
	2) interface (with abstract-methods)

1) Abstract-Methods in Python-Programming:-
(These methods are used inside a class)
= Method with a body or implementation is called as Complete or Concrete-Method
Ex:-
	def m1(self):	#complete-method
		....
		....
=** Methods without a body(pass) or implementation is called as Abstract-Methods
Ex:-
	def m2(self):	#in-complete-method
		pass;
= Abstract-Methods have only-declaration but no-definition or implementation or body
= Such methods are decorated with "@abstractmethod"
Ex:-
	@abstractmethod	--> it is decorator ("abc" module)
	def m2(self):
		pass;
(here pass means body W.O definition)

= @abstractmethod decorator is in "abc" module 
(import it)
(abstract base class)

Ex:-
from abc import *;
class Demo:
	@abstractmethod
	def m1(self):
		pass;
(here @abstractmethod decorator & pass for abstract-method are compulsory)	


==> Abstract-Classes:-
= Class which is not complete is called as Abstract-Class (In-concrete-class)
= Abstract-Classes are inherited from "ABC" class of abc-module

Def:-
	Abstract-Classes are classes with atleast-1 absract-method
(Abstract-Classes object cannot be created because they are in-complete-classes)
Ex:-
from abc import *;
class Demo(ABC):
	@absractmethod
	def m1(self):
		pass;
obj = Demo();	#error

(Abstract-Classes should be inherited from "ABC" & they should have atleast 1 abstract-method)
	


=** Final-NOTE:-
1)
If a class contains "atleast 1 abstract-method" and is "inherited from ABC" then only it is Abstract-Class (Which cannot be instantiated i.e, object cannot be created for abstract-class)


=>>** How to make use of Abstract-Classes??
***= To use Abstract-Class, we have go for child-class(Inheritance) 
= in child-class we have to re-define(method-overriding) all the abstract-methods of Parent-class
(then only child-class becomes complete-class & its object can be created)

***= Parent-class abstract-methods should be implemented or re-defined in Child-class o.w Child-class also becomes abstract-class & its object cannot be created

==Diagarm
	Incomplete-class(Abstract-Class) (obj-NOT-ok)
		|
		|
	<<inheritance>>
		|
		|
	Complete-Child-class (obj->ok)


=** Abstract-class(abc-module,ABC(pc),@absractmethod) & Complete-Child-class(Compulsory) -> redefine all abs-methods

Ex:-
"""
# //Program (AbstractClassEx1.py)
#Program (AbstractClassEx1.py)
#Program to work with abstract-classes & abstract-methods

from abc import *;
class A(ABC):
	@abstractmethod
	def m1(self):
		pass;
	def m2(self):
		print("m2() complete-method of abstract-class")
	
#child-class(inheritance)	
class B(A):		#complete-class
    #m1(),m2()
	def m1(self):   #redefine or overriding of m1()
		print("m1() Redefined in Child-class B");
	def m3(self):
		print("m3() own-method in Child-class B");

#child-class(inheritance)		
class C(A):		#complete-class
    #m1(),m2()
	def m1(self):   #redefine or overriding of m1()
		print("m1() Redefined in Child-class C");		
	def m4(self):
		print("m4() own-method in Child-class C");		


#abstract-class object
#obj = A();


#object of complete-child-class-B
obj1 = B();			#Complete-class
obj1.m1();
obj1.m2();
obj1.m3()


print()
#object of complete-child-class-C
obj2 = C();			#Complete-class
obj2.m1();
obj2.m2();
obj2.m4();

# NOTE:-
# = Abstract-Class may contain complete-methods but atleast 1-abstract-method

"""
=====================================================
3) Interfaces in Python:-(**)
= Complete-class contains all complete-methods (Obj can be created)
= Abstract-Class contains atleast-1 abstract-method (but Obj cannot be created)
= Interface(Pure-Abstract-Class) contains all methods as abstract-methods (Obj cannot be created)

def:-
	Inheritance is a abstract-class with all absract-methods in it compulsory

==** here also we use "ABC" and @abstractmethod decorator form abc-module
= Interfaces are used with child-classes same like abstract-classes
(in child-class re-define all abstract-methods & child-class becomes complete-class & finally its object can be created)
"""
# Ex:-
#Program (InterfaceEx1.py)
#Program (InterfaceEx1.py)

from abc import *;
class A(ABC):
	@abstractmethod
	def m1(self): 
		pass;
	@abstractmethod
	def m2(self): 
		pass;	

class B(A):
	def m1(self): 
		print("m1() Redefined in Child-class B");
	def m2(self): 
		print("m2() Redefined in Child-class B");
	def m3(self):
		print("m3() own-method in Child-class B");
	
class C(A):
	def m1(self): 
		print("m1() Redefined in Child-class C");
	def m2(self): 
		print("m2() Redefined in Child-class C");
	def m4(self):
		print("m4() own-method in Child-class C");
        

#interface-obj
#obj = A();     

#obj1 of complete child-class-B
obj1 = B();
obj1.m1();
obj1.m2();
obj1.m3();
print()
#obj2 of complete child-class-C
obj2 = C();
obj2.m1();
obj2.m2();
obj2.m4();

"""
=> Real-time Usage of Abstraction***
(Project-Design phase)
		Interfaces
			|
			|
		Abstract-Classes
			|
			|
			|
		Complete-class(child)
	(objs are created... and used in real-time)	



==> Interface v/s Abstract-Class v/s Complete-class:-
1) If we dont know anything about functions & its implementations then we go for Interfaces (Only Specs are Available)
2) If we require only Partial Implementation of functions in class then we go for Abstract-Classes
3) If we require complete-implementation of class with objects then we go for Complete-classes
"""
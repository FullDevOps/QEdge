# 27th day 27.24-08-22

"""
******(Access-Specifier in Python)**********
(Access-Modifiers)
(used inside a class for its members(vars+methods))
(Scope of access/level of access)
= they are 3-types,
	a) public  (a,m1())   	#no-underscore
	b) protected (_a,_m1())  #single-underscore(begin)
	c) private (__a,__m1())  #double-underscore(begin)

= Access-Specifier means where we can access class-members in python program
(class-members => data-prop(vars) & methods)

= For this, we have 4-levels-of-access,
i.e, Same-class-access
	 Sub-class-access
	 Other-class-access
	 Outside the class-access(main-prog)
	 ----------------------------
	 Outside the module-access(**)
==Diagram==



==> Public, Protected, Private Attributes:-
(these attributes are internally defined in python)
a) Public:-
= By default all attributes(data-prop or vars or methods) are Public in python-class
= Public attributes(data-prop or vars or methods) of python-class can be accessed from anywhere (inside or outside a class) i.e, Full-access
i.e, Same-class/Sub-class/Other-class/Outside the class
Ex:-
name="Sai";		#name-var and m1() are public by default
def m1(self):
	pass;

b) Protected:-
= Protected attributes(data-prop or vars or methods) of a class can be accessed inside Same-class (or Same-File) and only its Child-classes (Other classes of Same-File)
i.e, Same-class/Sub-class/Other-class/Outside the class
= It is prefixed with _ symbol
Ex:-
_name="Sai";
def _m1(self):
	pass;
(It is just notation but such protected-attributes does not exists in python class)

c) Private:-
= Private attributes(data-prop or vars or methods) of a python-class can be accessed only inside Same-class and not outside the class
i.e, Same-class access
= It is prefixed with two __ symbol (double-underscore)
Ex:-
__name="Sai";
def __m1(self):
	pass;

Ex:-
#Program (PubProPriEx1.py)
(Program to demo Public, Protected, Private Attributes)

NOTE:-
= Basically we have only 2-access-modifers (public/private)
(protected is just a notation)
"""
# //Program...
#Program to demo Public, Protected, Private Attributes)
#Program to demo Public, Protected, Private Attributes)
#Program (PubProPriEx1.py)

class Demo:
	a=10;		#public-var
	_b=20;		#protected-var
	__c=30;		#private-var
	def m1(self):	#Same-class all are accessible
		print("Inside Same-class");
		print(Demo.a);
		print(Demo._b);
		print(Demo.__c);


#same-class-access
obj = Demo();
obj.m1();
'''

'''
print()
#in sub-class-access
class Demo1(Demo):
	def m2(self):
		print("Inside Sub-class-access");
		print(Demo.a);
		print(Demo._b);
		#print(Demo.__c);
		
obj1 = Demo1();
obj1.m2();
'''

'''
print()
#in other-class (same as out-side class access)
class Demo2:
	def m3(self):
		print("Inside Other-class-access");
		print(Demo.a);
		print(Demo._b);
		#print(Demo.__c);

obj2 = Demo2();
obj2.m3();
'''

'''
print()
#out-side the class-access(main-program __main__())
print("Outside-class-acess in main-program");
print(Demo.a);
print(Demo._b);
#print(Demo.__c);	#private-mem


"""
==> Assignment::-
=**WAP to demo access-modifers(pub/pro/pri) of a class, accessing from other-modules(.py files)
(use import statement)
#PubProPriEx2.py
-------------------
from PubProPriEx1 import Demo;
#main-prog
print("Other-Module Access)
print(Demo.a);
print(Demo._b);
#print(Demo.__c);	#private-mem




(=**sp-case**)
==> How to access Private-Vars outside the class:-
= Private-Vars cannot be accessed directly outside of a class
= It is accessed indirectly as follows,

Syntax:-
---------
objrefvar._classname__privatevarname/privatemethodname()
"""
	
# Ex:-
#Program (PubProPriEx3.py)
#Program (PubProPriEx3.py)
#Program to demo private-member access outside the class


class Demo3:
	__c=11;
	def __init__(self):
		self.__x=10;
	def __m3(self):
		print("Private __m3() method");
		
		
obj3 = Demo3();
#print(obj3.__x);  #error

print("Private-member outside access");
print(obj3._Demo3__x);	
print(obj3._Demo3__c);
obj3._Demo3__m3();		
	

"""
==> Assignment::-
=**WAP to demo access-modifers(pri with sp-case) of a class, accessing from other-modules(.py files)
(use import statement)
#PubProPriEx4.py
-------------------
from PubProPriEx3 import Demo;
obj4 = Demo3()
print("Private-member outside module-access");
print(obj4._Demo3__x);	
print(obj4._Demo3__c);
obj4._Demo3__m3();


---------------------------------------------
==> __str__() sp-method of class:-
(pre-defined magic-method)
= Whenever we print any Obj.Ref, internally __str__() is called
Ex:-
	print(s1)
	print(obj1)
= It returns or gives string-value
Ex:
<__main__.classname object at 0x1234AB0> #it prints object address

= This string-value is little bit confusion
= For easy understanding format, we override this method in our class
(re-define the same method in our-class with own-definition)
"""
# Ex:-
#Program (StrMethod.py)
#Program (StrMethod.py)
#Program to demo __str__() method in our class


class Student:
	def __init__(self,rollno,name):
		self.rollno=rollno;
		self.name=name;
	def __str__(self):	#re-define in our class
		ss="Student-Data"+"\t"+str(self.rollno)+"\t"+self.name;
		return ss;
		
s1 = Student(1001,"Sai");
s2 = Student(1002,"Ram");
print(s1);
print(s2);
print(id(s1))
print(id(s2))


# NOTE:-
# = help(modulename/classname) gives complete description of that class or module




"""
===========================================================
***==> Exception-Handling in Python:-
(Introduction)
= This concept is related to OOP(real-life-situations)
def:-
	Exception means runtime-error
	(Error which occurs during execution of a program)

***Runtime-Errors occur when end-user is using our-app or s/w.
(they occur b'coz end-userby mistake gives wrong input)

Ex:-
	"division program"
case-1:-
	a=10,b=2 	#correct-input
	c=a/b;
	print(c)	##10/2-->5 (proper-output)
case-2:-
	a=10,b=0		#wrong-input by mistake
	c=a/b;			#10/0
	print(c)	##runtime-error (no-proper-output)
	
==** When Runtime-Errors occur, our program execution-stops there only(Abnormal-Termination of Prog)
	

=** Basically we have 2-types of Errors in python-program,
a) Syntax-Errors
b) Runtime-Errors

a) Syntax-Errors:- (devlopment-time errors))
= These errors occur due to Invalid-syntax or Wrong syntaxes in program
Ex1:-
x=10;
if x==10		#Syntax-Error : is missing
	print("Hello");

Ex2:-
print "Hello";	#Syntax-Error () Missing Parenthesis

NOTE:-
= Once program does not have any syntax-error(dev-time-errors) then program executes completely o.w program does not execute completely
= Generally, we get syntax errors during development-time


2) Runtime-Errors:-
= These errors occur while executing the program due to improper input given by user (or logics or memory-problems)
= Also called as Exceptions
Ex:-
print(10/0);	#ZeroDivisionError
print(10/"ten");	#TypeError (int/string)
a = int(input("Enter any Number : "));
#if input is "ten" then we get "ValueError"
("ten" cannot be converted to int)

NOTE:-
= Syntax-Errors can be fixed at development-time
only
= But Runtime-Errors(Exception) occurs & we get Abnormal-Termination of Program
(break-down of the program)
(program stops executing at that particular line & remaining lines of program are not executed)



=> About Exceptions:-
= It is any unexpected-error during execution time of program and leads to Abnormal-Termination of Prog
Ex: (Some Pre-defined Exceptions)
	= ZeroDivisionError
	= TypeError
	= ValueError
	= FileNotFoundError
	= EOFError
	= SleepingError
	= InsufficientFundsError (User-Defined)

NOTE:-	
= If we handle Runtime-Errors(Exceptions) then we get Proper & Complete Execution of Program
(Normal-Execution of Program)

=> DEFINITION:-
=** Exception-Handling is a mechanism of detecting runtime errors and providing with proper alternate solution
(Detect Runtime-Errors -------> Provide-Solution)

Ex:-
= Accessing Gmail from India-Server and if india-server is down then immediately Google will provide gmail-service from US-Backup-Server
(Always Online and NO-Breakdown)
"""
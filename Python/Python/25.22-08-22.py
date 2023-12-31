# 25th day 25.22-08-22

"""
25.22-08-22
==>> Polymorphism in Python:-
(it is principle/feature of OOP)
= Poly means Many (2 or more)
= Morphism means Forms (behavior ---> methods/functions)

**Definition:-
	= Existence of single-object in multiple-forms based on a condition is called Polymorphism

Ex1:	(H20)
==Diagram==
		"H2O"
	=> Liquid (water)
    => Solid  (ice)	
	=> Gaseous (Vapour/Stream) 
(based on temperature(degrees))

Ex2: + operator can be used in 2-ways
==Diagram== (Concatenation & Numeric-Add)
10+20 ===> 30
"Hello"+"World" ===> "HelloWorld"

Ex3: * operator can be used in 2-ways
==Diagram== (Multiplication & Repetition)
10*20 ===> 200
"Hello"*3 ===> "HelloHelloHello"

NOTE:-
**=> Polymorphism in Python can be done in 3-ways:-
1) Duck-Typing Philosophy
2) Overloading
	a) Operator Overloading
	b) Method Overloading
	c) Constructor Overloading
3) Overriding
	a) Method Overriding
	b) Constructor Overriding



1) Duck-Typing Philosophy:-
Def:-
	= deciding method input-parameter data-type at runtime is called duck-typing

= In Python variables, we cannot specify the datatype explicitly
Ex:-
	a=10;
	a=5.6;
	a="Hello"
= Based on provided value at Runtime, dtype is taken into consideration
= Hence Python is dynamically typed Prog.Lang
Ex:-
(variables in methods as paramters)
	def f1(obj):
		obj.display();
(here which ever class object is passed as paramter, its coressponding display() is executed)

**= Here data-type of "obj" in f1(obj) is decided at Runtime, when we pass any type of class-object. This is called Duck-Typing		
Ex:-
//Program (DuckTypingEx1.py)

NOTE:-
= Here we have a problem, if any object-Class does not contain talk() then we get "AttributeError"
Ex:-
//Program (DuckTypingEx1.py)
"""
##Program (DuckTypingEx1.py)
#Program to demo Duck-Typing

class Student:
	def display(self):
		print("Student-Details");
class Employee:
	def display(self):
		print("Employee-Details");
class Customer:
	def display(self):
		print("Customer-Details");

#single-func with diff-input-para(duck-typing)
def f1(obj):
	obj.display();		

s1 = Student();
e1 = Employee();
c1 = Customer();

f1(s1);
f1(e1);
f1(c1);




"""

2) Overloading in Polymorphism:-
= It is done with 3-cases
	a) Operator Overloading 
	b) Method Overloading
	c) Constructor Overloading
	
Ex1:- (+ Operator used in 2-ways)
print(10+20);			#Numeric-Addition
print("Sai"+"Ram");		#String-Concatenation

Ex2:- (* Operator used in 2-ways)
print(11*3);			#Numeric-Multiplication
print("Sai"*5);			#String-Repetition

Ex3:- (Bank deposit() )
deposit(cash);
deposit(cheque);
deposit(dd);

=> Overloading is done in 3-ways,
i) Operator-Overloading
ii) Method-Overloading
iii) Constructor-Overloading


i) Operator-Overloading:-
= We can use same operator for multiple-purposes
Ex1:- (+ Operator used in 2-ways)
print(10+20);			#Numeric-Addition
print("Sai"+"Ram");		#String-Concatenation

Ex2:- (* Operator used in 2-ways)
print(11*3);			#Numeric-Multiplication
print("Sai"*5);			#String-Repetition

Ex:-
##Program (OperatorOverloading1.py) #with objects

NOTE:-
=** Here we have to overload +operator to work with Book-objs (class-objs)
= For every operator, python directly supports "Magic-Methods"
(Magic-Methods can be used on class-objs Ex:- b1+b2 directly)
= For operator-overloading, we have to override(redefine) Magic-Methods in our class
= For +operator on class-objs, magic-method is __add__()

Ex:- (redefining __add__())
"""
# //Program (OperatorOverloading1.py)
#Program (OperatorOverloading1.py)

class Book:
	def __init__(self,pages):
		self.pages=pages;
	def display(self):
		print(self.pages);
		
b1 = Book(100);
b1.display();
b2 = Book(200);		
b2.display();
#print(b1+b2);	#TypeError
b3 = Book(b1.pages+b2.pages);
print(b3.pages);


#redefining __add__()
class Book:
	def __init__(self,pages):
		self.pages=pages;
	def display(self):
		print(self.pages);
	def __add__(self,other):
		return (self.pages+other.pages);
b1 = Book(100);
b1.display();
b2 = Book(200);
b2.display();
print(b1+b2);	#NO-error (adding b1,b2 objs & auto __add__() executed)

"""
NOTE:-
= Below are different Magic-Methods for corresponding operators
Ex:- (self is 1st-object & other is 2nd-object)
1) +	__add__(self,other);	
2) -	__sub__(self,other);
3) *	__mul__(self,other);
4) /	__div__(self,other);
5) %	__mod__(self,other);
6) //	__floordiv__(self,other);
7) **	__pow__(self,other);
-----------------------------------------------
8) +=		__iadd__(self,other);	Ex: a+=b; (a=a+b)
9) -=		__isub__(self,other);
10) *=		__imul__(self,other);
11) /=		__idiv__(self,other);
12) %=		__imod__(self,other);
13) //=		__ifloordiv__(self,other);
14) **=		__ipow__(self,other);
------------------------------------------------
15) <		__lt__(self,other);	
16) <=		__le__(self,other);
17) >		__gt__(self,other);
18) >=		__ge__(self,other);
19) ==		__eq__(self,other);
20) !=		__ne__(self,other);


Ex:- (Overloading > and <= for Student-class objs)
//Program (OperatorOverloading2.py)

Ex:- (Overloading Multiplication Operator on Student-objs)
//Program (OperatorOverloading2.py)
#Program (OperatorOverloading2.py)
#OO to demo magic-methods speciality
"""

class Student:
	def __init__(self,name,marks):
		self.name= name;
		self.marks=marks;
	def __gt__(self,other):
		return (self.marks > other.marks);
	def __le__(self,other):
		return (self.marks <= other.marks);


s1 = Student("Sai",96);
s2 = Student("Ram",86);
print(s1>s2);       ##> <=
print(s1<=s2);

print()
#magic-combinations are automatic
print(s1<s2);
print(s1>=s2);
print()
print(s1==s2);
print(s1!=s2);


# NOTE:-
# = These sp-methods are called magic-methods b'coz in prev.example, we have defined only >, <= and other combinations are taken auto. w.o defining


"Assignment"
#Program (OperatorOverloading3.py)
#Overloading Multiplication Operator on Employee-objs
class Employee:
	def __init__(self,name,sal):
		self.name=name;
		self.sal=sal;
	def __mul__(self,other):
		return (self.sal * other.days);
	
class TimeSheet:
	def __init__(self,name,days):
		self.name=name;
		self.days=days;

e1 = Employee("Sai",1000);
t1 = TimeSheet("Sai",26);
print(e1.name,"Month Salary : ",e1*t1);

"""

(b) Method-Overloading:-
def:
	= 2 or more methods in same-class/prog with same-name but atleast 1-difference in method-signature 
		=** No-of-args,
		=** Order-of-args,
		=** Dtype-of-args
Ex:-
	m1(int x):
	m1(float a):
	m1(int, float):
	m1(float,int):

NOTE:-(***)
**= But in Python, Method-Overloading is NOT-POSSIBLE
= Trying to declare multiple-methods with same-name & diff. in method-signature then Python-takes only last-method into considerations (Like variables)
Ex:-
a=10;	(int)
a=5.6;	(float)
a="Sai"; (str)
a=True;	(bool)	--> only a=True is considered
	
Ex:-
"""
# //Program (MethodOverloading1.py)
#Program (MethodOverloading1.py)
#Program to perform method-overloading indirectly


#general-case
class Demo:
	def m1(self):
		print("0-Args m1()");
	def m1(self,a):
		print("1-Args m1()");
	def m1(self,a,b):	#lastest m1() is considered
		print("2-Args m1()");
	
obj = Demo();
#obj.m1();		#0-args
#obj.m1(11);	#1-arg	
obj.m1(11,22);	#2-args
'''

'''
#case-1
#Method with Default-Args
class Demo:
	def sum(self,a=1,b=2,c=3):
			print("SUM(of 3 numbers) : ",(a+b+c));
		
obj = Demo();
obj.sum(1000,2000,3000);		#3-args is passed
obj.sum(100,200);				#2-args
obj.sum(10);					#1-arg	
obj.sum();  					#0-args	


#case-2
#Method with Variable-len(No)-of-Args
class Demo:
	def sum(self,*nums):	#here nums is tuple
		print("SUM : ",sum(nums));
		
obj = Demo();
obj.sum(100,200,300);		#3-args
obj.sum(10,20);				#2-args	
obj.sum(1);					#1-arg	
obj.sum();					#0-args	


"""
NOTE:-
=> How to handle Method-Overloading in Python?
= For this we use Method with Default-Args (or) Method with Variable Number of Args

=> Method with Default-Args:-
=** Default-Args means while declaring the method, we give default values to input-parameters/args
Ex:-
	def sum(a=10,b=20,c=30):
= whenever method is called with less no.of.para or no-para then default-values of args are taken into consideration

Ex:- (Method with Default-Args)
//Program (MethodOverloading1.py)

=> Var-len-Args to Method:-
(Variable-Length-Arguments)
= For any method we can pass last-para as variable-args
= It means for that last-para, we can pass 0 or more args/values to call such method
= It is done with *varName (it can accept 0 to more args/values as input)
= compulsory it should be last-para in method o.w error

Ex:- (Method with Variable-No-of-Args)
//Program (MethodOverloading1.py)



C) 
==> Constructor-Overloading:-
= It is not possible in Python
= Here also, if we define multiple-constructors with same-name and atleast 1-difference in constructor-signature
	(No-of-args,
	Order-of-args,
	Dtype-of-args)
Ex:-
	def __init__(self):		#0-args
	def __init__(self,a):	#1-arg
	def __init__(self,a,b):	#2-args

=> def:-
	multiple-constructors with same-name in same-class & atleast 1-diff in constructor-signature

= In such case, last constructor is taken into consideration like methods/variable
Ex:-
Ex:-
a=10;	(int)
a=5.6;	(float)
a="Sai"; (str)
a=True;	(bool)

Ex:-
"""
# //Program (ConstructorOverloading1.py)
#Program (ConstructorOverloading1.py)
#Program to demo Const-Over indirectly in 2-cases


#no Const-Over
class Demo:
	def __init__(self):
		print("0-Args Constructor");
	def __init__(self,x):
		print("1-Args Constructor");
	def __init__(self,x,y):	#only lastest-const is taken
		print("2-Args Constructor");

#obj1 = Demo();         #0-args-const
#obj2 = Demo(11);        #1-args-const
obj3 = Demo(111,222);  #2-args-const
'''


'''
#case-1
print()
#Constructor with Default-Args
class Demo:
	def __init__(self,a=1,b=2,c=3):
		print("sum :: ",a+b+c)

obj1 = Demo();		#0-args
obj2 = Demo(11);	#1-arg	
obj3 = Demo(111,222);	#2-args
obj4 = Demo(1111,2222,3333);	#3-args



#case-2
print()
#Constructor with Variable-No-of-Args
class Demo:
	def __init__(self,*nums):	#nums is tuple(dyc-size)
		print("Sum ::",sum(nums))
		
obj1 = Demo();			#0-args
obj2 = Demo(11);		#1-arg
obj3 = Demo(111,222);	#2-args
obj4 = Demo(1111,2222,3333);	#3-args



"""
NOTE:-
= However, we can make constructor-overloading possible using Constructor with Default-Args & Constructor with Variable-No-of-Args

=> Constructor with Default-Args:-
=** Default-Args means while declaring a constructor, we give default values to input-parameters/args
= when such constructor is called with less no.of.para or no-para then default-values of args are taken into consideration
Ex:-
def __init__(self,a=10,b=20,c=30):

Ex:- (Constructor with Default-Args)
//Program (ConstructorOverloading1.py)

=> Var-len-Args to Constructor:-
= For any constructor, we can pass last-para as variable-args
= It means for that last-para, we can pass 0 or more args/values to call such method
= It is done with *varName (it can accept 0 to more args/values as input)
= compulsory it should be last-para in constructor o.w error

Ex:- (Constructor with Variable-No-of-Args)
//Program (ConstructorOverloading1.py)

"""
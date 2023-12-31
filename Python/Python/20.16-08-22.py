# 20th day 20.16-08-22

"""
****Encapsuation***
-----------------------------
==> Classes & Object:- (in OOP)
-----------------------------
= This concept is related to Encapsulation 
(OOP-Principle)

**= In Python, everything is an object and to create an object we require a Class(model)

=> Def:-
	= A class is a Model, which represents properties(Vars) and behaviour(functions)
=** Properties ---> Variables
=** Behaviour means Functions/Methods

[Class = data-Variables + Functions/Methods]

=** Binding togather data-properties & functionalities into a single-unit
(class is collection of vars & methods(Funcs))

NOTE:-
= A class is a Model/Plan/Design/Arch/Blue-print before getting an actual Product (i.e, Object)
Ex:-
	House(Blue-print)	---> Class(model) [Civil-Engg]
	Constructed-House(Object/End-Product)
=** Object is End-Product used by End-User(Customer/Client/Humans)
=** For 1-class(model/blue-print) we can have multiple-objects(products)

=> How to define class?
= It is defined with "class" keyword
Syntax:-
	class Classname:
		'''Doc-String or Comments'''
		data-variables; 	(instance/static/local)
		methods;			(instance/static/class)
	
= Indentation is Compulsory for class-body o.w Error...	
(inside a class function is called as METHOD)

NOTE:-
'''Doc-String''' (Description/Comment of Class and it Optional)
= We can get it as follows,
Ex:-
help(Classname); #complete-desc/def of a class i.e, help()
print(Student.__doc__);


##Program (Student.py)
#(Prog to define Student-class)



help(Student);
print(Student.__doc__);

NOTE:-
= inside class, vars & methods are optional(not-compulsory)


===> Class with Vars & Methods:-
Ex:- (Student-class)
	sno/sname/height --->	(Variables)
	def display():	--->	(Methods/funcs)
	def show():

NOTE:-
= We define-vars(declare & initialize) using sp-method(Func)
Ex:-
	def __init__(self):
	
=** self means current object of class	
"""
##Program (Student1.py)
#Program to work with Student1-class with vars & methods(funcs)
##Program (Student1.py)
#Program to work with Student1-class with vars & methods(funcs)

class Student1:
	'''Student1-class def...'''
	def __init__(self):
		self.sno=1001		#(.dot operator)
		self.sname='Sai'
		self.height=6.2
	def display(self):
		print(self.sno)
		print(self.sname)
		print(self.height)
		
	
print(Student1.__doc__)
print()
help(Student1)
print()


# NOTE:-
# = Student1-class has (3-vars & 2-methods)
"""
**Working with object**
==> Object:-
	= Object is instance of a class, which represents state(Vars) and behavior(func) of a class
	
(instance ----> 1-individual-unit)

=> how to create object??	
Syntax:-
	objrefvar = Classname();
Ex:-
	s1 = Student1();
(when class-obj is created, __init__() is called auto.)
==Diagram==
(obj.ref.var--------->[sno/sname/height])

=> using object??
= to work or use any class object we use (Dot .) operator
Ex:-
	objref.Variables
	objref.methods()
Ex:-
	s1.sno
	s1.display()
"""
# [contd..]
##Program (Student1.py)
##Program (Student1.py)
#Program to work with Student1-class with vars & methods(funcs)

class Student1:
	'''Student1-class def...'''
	def __init__(self):
		self.sno=1001		#(.dot operator)
		self.sname='Sai'
		self.height=6.2
	def display(self):
		print("Roll-No =",self.sno)
		print("Name =",self.sname)
		print("Height =",self.height)
		
	

#case1
print(Student1.__doc__)
print()
help(Student1)
print()


#case2 (working with objs)
s1 = Student1();
print("s1-obj Student-details")
s1.display();

print()
s2 = Student1();
print("s2-obj Student-details")
s2.display();

# NOTE:-
# = Here s1 and s2 both objs have same-data(vars) b'coz in __init__() we have static-values


# [contd..]
##Program (Student1.py)
##Program (Student1.py)
#Program to work with Student1-class with vars & methods(funcs)

class Student1:
	'''Student1-class def...'''
	def __init__(self):
		self.sno=1001		#(.dot operator)
		self.sname='Sai'
		self.height=6.2
	def display(self):
		print("Roll-No =",self.sno)
		print("Name =",self.sname)
		print("Height =",self.height)
		
	

#case1
print(Student1.__doc__)
print()
help(Student1)
print()


#case2 (working with objs)
s1 = Student1();
print("s1-obj Student-details")
s1.display();

print()
s2 = Student1();
s2.sno=1002		#modify obj-data(Vars) outside class
s2.sname='Ram'
s2.height=5.9
print("s2-obj Student-details")
s2.display();

"""
NOTE:-
= Here we can modify s2(obj-data-vars) outside class
Ex:-
	s2.sno=1002
	s2.sname='Ram'
	s2.height=5.9
(this techique is not advisable)

***= However, we can modify object data using dynamic-values with input() inside __init__()
Ex:-
	self.rno = int(input("Enter Roll-No :: "))
"""
##Program (Student2.py)
#Program to work with Student2-class with vars & methods(funcs) with dynamic-values
##Program (Student2.py)
#Program to work with Student2-class with vars & methods(funcs) with dynamic-values


class Student2:
	'''Student2-class def...'''
	def __init__(self):
		self.sno=int(input("Enter Roll-No :: "))
		self.sname=input("Enter Name :: ")
		self.height=float(input("Enter Height :: "))
	def display(self):
		print("Roll-No =",self.sno)
		print("Name =",self.sname)
		print("Height =",self.height)
		
	
#working with objs
s1 = Student2();	#__init__() called auto for obj.create
print("s1-obj Student-details")
s1.display();

print()
s2 = Student2();
print("s2-obj Student-details")
s2.display();

# NOTE:-
# = Whenever we create obj of a class, __init__() is called auto with self-var(current-obj is passed auto)

# ***Other-Examples***
##Program (Employee.py)
##Program to work with Employee-class with vars & methods(funcs) with dynamic-values
##Program (Employee.py)
##Program to work with Employee-class with vars & methods(funcs) with dynamic-values

class Employee:
	'''Employee-class def...'''
	def __init__(self):
		self.empno=int(input("Enter Emp-No :: "))
		self.ename=input("Enter Emp-Name :: ")
		self.sal=float(input("Enter Salary :: "))
	def show(self):
		print("Emp-No =",self.empno)
		print("Name =",self.ename)
		print("Salary =",self.sal)
		
	
#working with Employee-class-objs
e1 = Employee();	#__init__() called auto for obj.create
print("e1-obj Employee-details")
e1.show();

print()
e2 = Employee();	#__init__() called auto for obj.create
print("e2-obj Employee-details")
e2.show();


# **"Assignment"**
##Program (Employee1.py)
##Program to work with Employee1-class with vars & methods(funcs) with dynamic-values
# (empno/ename/job/sal/comm) --> vars inside __init__()
# [cal. totalsal = e1.sal+e1.comm] --> inside main-prog
# [cal. annulsal = totalsal*12]


"Assignment"
##Program (Customer.py)
##WAP to work with Customer-class with vars & methods (dynamic-values)
# (cacno,cname,cbranch,cbal)



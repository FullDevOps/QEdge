# 18th day 18.13-08-22

"""
==> Modules in Python:-
(module means python .py file)
= A Module contains Classes, Functions, Variables etc saved in a single-file (.py as extension)
= Every Python .py file is a Module
Ex:- math.py, 
	random.py, 
	time.py 
	(pre-defined modules)

=> we have 2 types of modules,
	a) Pre-defined modules
	b) User-defined Modules (our own modules)

= Now, we create our own modules in python (user-defined modules)
##Program (SaiMath.py)
#Program to create our own user-defined module
Ex:-
"""
# (SaiMath.py)
a=100;
b=200;
def add(x,y):
	print(x+y);
def sub(x,y):
	print(x-y);
def prod(x,y):
	print(x*y);
def div(x,y):
	print(x/y);	
def mod(x,y):
	print(x%y);

##Program (SaiMath.py)
# (Program to demo a Module with Functions and Variables)

# NOTE:-
# = "SaiMath" is UD-Module, It contains 2-Vars and 5-Funcs

##Program (SaiMath.py)
#Program to create our own user-defined module

#2-vars
a=100;
b=200;

#5-funcs
def add(x,y):
	print(x+y);
def sub(x,y):
	print(x-y);
def prod(x,y):
	print(x*y);
def div(x,y):
	print(x/y);	
def mod(x,y):
	print(x%y);
"""
==> How to use Module in Python-prog??
= It is used with "import-keyword"
= To use such module in our prog, we have to import it using import-keyword
Ex:
	import <<ModuleName>>;
	import SaiMath;
	
(***)	
= After importing module in our program, we can access module vars,funcs,classes using ModuleName (.dot operator)
Ex:-
	SaiMath.variable (SaiMath.a)
	SaiMath.function() (SaiMath.add(11,3))

##**main-program**
##Program(Demo1.py)
##(Prog to use SaiMath module and its content)


NOTE:-
= Here just run main-program(Demo1.py) & NO need to run module-program
"""
# //Program...
##**main-program**
##Program(Demo1.py)
##(Prog to use SaiMath module and its content)


import SaiMath;
print("Using SaiMath.py module in main-program");

print(SaiMath.a);
print(SaiMath.b);

SaiMath.add(11,3);
SaiMath.sub(11,3);
SaiMath.prod(11,3);
SaiMath.div(11,3);
SaiMath.mod(11,3);
'''

'''
#Module Aliasing(alternate-name) with as keyword
import SaiMath as SM;	#use only alias-name o.w NameError
print(SM.a);
print(SM.b);
SM.add(11,3);
SM.sub(11,3);
SM.prod(11,3);
SM.div(11,3);
SM.mod(11,3);
#SaiMath.add(11,3)	#dont use org-name
'''

'''
#specific-content import
#from...import
from SaiMath import a,add,mod;
print(a);		#use directly mod-name not-req
add(11,3);
mod(11,3);
print(b)    #not defined
div(11,3); 	#NameError
'''

'''
#import all content at a time(*)
from SaiMath import *;	#* means import-all
print(a);		#no-need to use module-name
print(b);
add(11,3);
sub(11,3);
prod(11,3);
div(11,3); 	#NO-Error
mod(11,3);


#Member-Aliasing(content-alias) with as-keyword
from SaiMath import a as x, add as sum;
print(x);		#module-name not-req
sum(11,3);
#print(a);		#Error
#add(11,3);		#Error




"""
==> Module Renaming while usage:-
= It is like alias-name for module
Ex:-
import SaiMath as SM;
= SaiMath is Org-ModuleName
= SM is Alias-name

Ex:- (Demo1.py)
(Prog to use SaiMath module and its content with Alias-name)



==> from...import in Module:-
= We can import only particular members from a module as follows,
= Advantage is we can use them directly without ModuleName
Ex:-
from SaiMath import a,add,mod;
print(a);
add(11,3);
mod(11,3);
#div(11,3); 	#NameError

Ex:-
from SaiMath import *;		#Here * means all the members
print(a);
add(11,3);
mod(11,3);
div(11,3); 	#NO-Error

Ex:- (Demo1.py)

==> Possible ways for Module-import:-
1) import ModuleName;				#Single-Module
Ex:-
	import SaiMath;

2) import Module1,Module2,....;		#Multiple-Modules
Ex:-
	import SaiMath1, SaiMath2;
=** Here SaiMath1/SaiMath2 should be defined in our working-directory

3) import Module1 as M;				#Using Alias-name
Ex:-
	import SaiMath as SM;

4) import Module1 as M1,Module2 as M2,....;	
(#Multiple-Modules with alias-name)
Ex:-
	import SaiMath1 as SM1, SaiMath2 as SM2,.....;

5) from ModuleName import MemberName; #Only Members Import 
Ex:-
	from SaiMath import a;

6) from ModuleName import Member1, Member2,...;	
						#Multiple Members Import
Ex:-
	from SaiMath import a,add,sub;

7) from ModuleName import Member as M;	
						#Members Import with Alias
Ex:-
	from SaiMath import add as plus;
	print(plus(11,3));
						
8) from ModuleName import Member as M1, Member as m2,...;	
						#Multiple-Members Import with Alias
Ex:-
	from SaiMath import add as plus, sub as minus,...;
	print(plus(11,3));
	print(minus(11,3));
						
9) from ModuleName import *;
						# * indicates all members import directly
Ex:-
	from SaiMath import *;
	print(a);
	print(add(11,3));
						
NOTE:-
= from...import provides direct access to Members without ModuleName



==> Module-Members Aliasing:-
(for module-members we give alternate-name)
Ex:-
from SaiMath import a as x, add as sum;
print(x);
sum(11,3);

NOTE:-
= Once alias-name is given we have to use only that alias-name but not original names o.w NameError
Ex:-
from SaiMath import a as x, add as sum;
print(a);
add(11,3);


from SaiMath import a as x, add as sum;
print(x);
sum(11,3);

Ex:- (Demo1.py)

-------------------------------------------------------
==> Reloading a Module:-
= In main-prog, when a module is imported, it is loaded only once, even if we are import it multiple-times in a program
Ex:-
#Program(MyModule1.py)
print("Hello from MyModule1");

Ex:-(main-program)
"""
#Main-Program(Demo2.py)
import MyModule1;
import MyModule1;
import MyModule1;
print("End of the Program");
"""
# NOTE:-
(Refer-notes)
= MyModule1.py is loaded only once (for multiple-imports)
= After loading a module, and if it is updated from outside then updated new-changes is not available in our main-program

==> reload() function
= However, we can reload a module mulitple-times in our main-program using reload() function of "importlib"(new) module
Ex:- (Demo2.py)
"""
#Main-Program(Demo2.py)

import time;
import MyModule1;
import MyModule1;
import MyModule1;

print()
time.sleep(20)
import importlib;
importlib.reload(MyModule1)

print()
time.sleep(20)
from importlib import reload;
reload(MyModule1)

print("End of the main-Program");


# Ex:- (#MyModule1.py)
#Program(MyModule1.py)

print("Hello from MyModule1");

print("1st changes done in MyModule1"); 
#do changes in sleep-time

print("2nd changes done in MyModule1"); 

"""
------------------------------------------------------
NOTE:-
from importlib import reload;
= importlib is new-module and imp is old-module
= reload() reloads the module & its contents multiple-times




==> __name__ sp-variable::-
(refer-notes)
= __name__ is a sp-var in python-program
= it gives name of currently executing program
= It gives module-name for module-program
= It gives __main__ for main-program

Ex:-(Program)
##MyModule2.py (module-program)

print("Hello from MyModule2");
print(__name__)

--------------------------------------
##Demo3.py (main-program)

print("Hello from Demo3.py main-program")
print(__name__)

import MyModule2;

	


======================================================
***dir() and help()***
(Refer-notes)
==> Getting all members of Module using dir() function:-
= dir() lists all the members of a current-module 
(variables, functions, classes etc) [.......]
Ex:-
dir()	#lists all members of current-module(current-program or .py file)
dir(ModuleName)	#Lists all members of specified module

= help() gives complete desc of module including comments

Ex:- (Demo4.py)
a=100;
b=200;
def f1():
	print("Hello World");
print(dir());

Ex:-(with module-name)
import math;
print(dir(math));	#Pre-defined Module

import SaiMath;
print(dir(SaiMath));	#User-defined Module

help(math);		#Provides complete description of math-module
"""

# //Program...
#Demo4.py (listings all the members of module)

a=100;
b=200;
c=300
def f1():
	print("Hello World");
def f2():
	print("Welcome to Python");
print(dir());	#here it gives a list of all members of current-program
'''

'''
import math;
print(dir(math));
'''
'''
print();
import SaiMath;
print(dir(SaiMath));
'''

'''
import math;
help(math);




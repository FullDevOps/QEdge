# 19th day 19.15-08-22

"""
==> Packages in Python:-
= Package is a Folder/Directory 
(Coll.of Modules i.e, .py files)

***def:-
	= Packages is collection/grouping of related modules as single-unit

NOTE:-
= Python Package folder contains (__init__.py) empty-file. It indicated that special-folder is a Package-folder
= A package may have sub-packages also

Ex1:-
==Diagram==
D:\SAISIR\Python\Packages> (normal-regular-folder)
	=> Pack1 (pkg-folder)
		= __init__.py
		=> Pack11 (sub-pkg-folder)
			= __init__.py
			= Demo1.py 	(module)
			= Demo2.py	(module)
		
-------------------------------------------------------
=> Advantages:-
1) Naming conflicts can be removed
(we can have same-name .py file in multiple pkgs)
2) Project Components can be identified uniquely
(pkgname.filename)
Pack1.Demo
Pack2.Demo
3) Improves Modularity of Application
(it means grouping togather related .py files as single-pkg) 		


==> Creating packages & using them in program:-
##Program (Packages\Pack1 folder)
**(Module1.py)
def f1():
	print("Hello from Module1.py of Pack1 package");

##Program (Packages> folder) main-prog
**(Demo1.py)
import pack1.Module1;
Pack1.Module1.f1();
(or)
(Demo1.py)
from pack1.Module1 import f1;
f1();

NOTE:-
= to use pkgs we use import keyword only
Ex:-
	import PkgName.ModuleName;
	from PkgName.ModuleName import var,func;
"""


#Packages\pack1\Module1.py

def f1():
	print("Hello from Module1.py of Pack1 package");

# //Program...
#Packages\Demo1.py

import Pack1.Module1;
Pack1.Module1.f1();
'''

'''
#other-way
from Pack1.Module1 import f1;
f1();
'''

'''
#Package\Pack2 sub-pkg
from Pack2.Module1 import f1;
f1();
'''
'''
#sub-pkg(pack2\pack22 folder)
from Pack2.Pack22.Module2 import f2;
f2();


"""
=> Creating Sub-Pkgs & using them in our program:-
=** creating a folder(pkg) inside another folder is called sub-pkg

##Program (Packages\Pack1\Pack11 i.e Sub-Pkg/sub-folder)
(Module11.py)
def f11():
	print("Hello from Module11.py of Pack11 package");


##main-program in same	
(Demo1.py - Same add below-code)
==add-prog-code for sub-pkg access===


"Assignment" (Demo1.py main-prog only)
-----------------
1) WAP to work with Packages import with alias name
2) WAP to work with specific content import of a package with alias-name
(both cases use "as" keyword)
Ex:-
	import Pack1.Module1 as PM;
	PM.f1()
	(or)
	import Pack1.Pack11.Module11 as PPM;
	PPM.f11()
	(or)
	from Pack1.Module1 import f1 as hello;
	hello()
	(or)
	from Pack1.Pack11.Module11 import f11 as hi;
	hi()



##Program (Packages\Pack1 pkg-folder)
##(Module1.py)

def f1():
	print("Hello from Module1.py of Pack1 package");
"""
# -------------------------------------------------------	
##Program (Packages> folder) main-prog
##(Demo1.py)


import Pack1.Module1;
Pack1.Module1.f1();
'''

'''
#other-way
from Pack1.Module1 import f1;
f1();


#access sub-pkg (PkgName.SubPkgName.ModName)
import Pack1.Pack11.Module11;
Pack1.Pack11.Module11.f11()

#other-way(using from)
from Pack1.Pack11.Module11 import f11;
f11()

# --------------------------------------------------
##Program (Packages\Pack1\Pack11 i.e Sub-Pkg/sub-folder)
#(Module11.py)

def f11():
	print("Hello from Module11.py of Pack11 sub-package");
	

"""
============================================================================================================
"Advanced Python Concepts"
----------------------------------
I) OOP:-
(Object Oriented Programming)
= it is not new-programming
= it is not separate-progrmming
(it is available in C++,Java,.net,Python also)
(it is a concept or subject)
def:-
	it is a programming based on real-life situtaions(objects) as real-time computer programs
Ex:-
	Online shopping
	Online banking
	Online Tickets

==> OOPS principles:- (Based on real-life)
==Diagram==
	a) Abstraction
	b) Encapsulation
	c) Inheritance 
	d) Polymorphism
	
	
==> Abstraction::-
(Develop a Product in Company)
def:-
	= Hiding unnecessary things in a Product & exposing necessary things outside a product
	(desiging a product-model as dummy-product)
Ex:-
	Marker-Pen
		- Hidden (Ink,Refill)
		- Exposed (Body,Cap,Nib)

=** In python-program, we do abstraction in 2-ways,
	i) Abstract-classes
	ii) Interfaces
	
	
==> Encapsulation::-
= Encapsulation says that every product has 2-things,
	i) Data as Input
	ii) Functionality as Usage
Ex:-
	Marker-Pen
		- Input (Ink-color, Ink-Qty)
		- Use (Writing on Whiteboard)

=** In python-program, we do Encapsulation with,
	i) classes & objects


==> Inheritance::-
(G.Parents----->Parents----->Children----->G.Childrens)
def:-
	Getting properties & functionalities from existing-product to new-product
Ex:-
	iPhone11 (2G,3G,4G)
		|
		|
		|
	iPhone12 (2G,3G,4G + 5G**)
	
=** In python-program, we do Inheritance with
	i) Parent-class
	ii) Child-class
(Advantage of Inheritance is Re-usability)


==> Polymorphism::-
= Poly means Many (2 or more)
= Morphism means Forms (behaviour or functionality)
def:-
	Single Product in multiple-forms based on some condition
Ex:-
==Diagram==
	H2O(3-Forms) ----> (temp. is condition)
		= Solid(ICE)
		= Liquid(Water)
		= Gas(Vapour)

=** In python-program, we do Polymorphism as follows,
	i) Overloading
	ii) Overriding
	ii) Ducktyping



NOTE:-
= Python supports all principles of OOP. Hence it is called as OOP.Lang

"""
	
	











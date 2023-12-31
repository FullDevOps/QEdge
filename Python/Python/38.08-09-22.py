# -- 38th day 38.08-09-22

# ==>>> Decorator Functions:-
# = It is function, which takes another-function as argument and extend its functionality and returns/gives modified-function
# ==Diagram==
# Ex1:-
# I/P Function (wish()--->"@Decorator"---> new(add some functionality) using inner()
# Ex2:-
# I/P Function (wish()--->"Decorator-Function"---> Output-Function with Extended Functionality

# [our-func+@decorator/decorator-function ---> extra-func-our-func]

'''
=> Advantage,
= Decorator-Function extends the functionality of existing functions without modifying that function
Ex1:-
#Program (DecoratorEx1.py)

NOTE:-
=* Here wishes(), prints Same message for all user-names
= However to modify messages for different user-names, we can do this without touching wishes() & it is possible with @decorator/decorator-function



=> Using @decorator/decorator-function in program
Ex2:-
#Program (DecoratorEx1.py)
@decorator is passed or used before our function-def

NOTE:=
= Here for every wishes() function call, decor(func) is executed automatically
= For decorator-function, our function-ref is passed as input-para
= Inside decorator-function, inner() provides extra-functionality
= inner() takes same input-para as that of our function
= Finally, decorator-function returns inner() as return-value

==> How to call Same-Function with Decorator and without Decorator:-
(with @decor and W.O @decor)
Ex3:-
#Program (DecoratorEx1.py)

NOTE:-
= It is done with func-ref-var to decorator-function with input-para as org-function




==> Decorator Chaining:-
= We can define multiple-decorators for same-function and all these decorators will form Decorator-Chaining
Ex:-
@decor1
@decor
def num():
	....
=** Here for num(), we are applying 2 decorator functions
(1st inner-decorator works & then 2nd outer-decorator works)	
Ex6:-
#Program (DecoratorEx1.py)
'''


#Program (DecoratorEx1.py)
#Program to work with diff-decorators


#case-1
#same-msg w.o decorators
def wishes(name):
	print("Hello :",name,"Good Morning");
	
wishes("Sai");
wishes("Ram");
wishes("Ali");
'''


'''
#case-2
#diff-msgs using with decorator
def decor(func):	#wishes() is passed here	[func=wishes]
	def inner(name):	#inner() gives extra-func. to wishes()
		if name=="Ram":
			print("Hello :",name,"Good Afternoon");
		elif name=="Ali":
			print("Hello :",name,"Good Evening");
		else:
			func(name);
	return inner;
	
@decor
def wishes(name):
	print("Hello :",name,"Good Morning");
	
wishes("Sai");
wishes("Ram");
wishes("Ali");


#sp-case (using decorator-func but w.o @decorator (manually)
print();
decorfunction = decor(wishes); 
#func-ref-var to decor() with wishes()-i/p
decorfunction("Sai");	#decorator func is executed
decorfunction("Ram");
decorfunction("Ali");



#chaining of decorators
#Decorator-Chaining (using multiple-@decorators)
def decor1(func):
	def inner():
		x=func();
		return x*x*x;
	return inner;

def decor(func):
	def inner():
		x=func();
		return x*x;
	return inner;	

@decor1		#2nd-exec outer-dec
@decor		#1st-exec inner-dec
def num():
	return 5;
	
print(num());


'''
----------------------------------------------------------------
==>>> Generator Functions:-
= It is function responsible for generating sequence of values
Ex:-
	r1 = range(10)	----> 0 to 9 (pre-defined generator)
= We can write this function, just like regular-functions but here we use "yield-keyword" to return values
Ex:-
	yield 1;		#1st-value
	yield "Sai";	#2st-value
	yield 2;		#3rd-value
	etc....
==Diagram==
yield <---- "Generator-Function" ----> Sequence-of-values

Ex1:-
#Program (GeneratorEx1.py)
NOTE:-
= next(gen-var) is used to get/access values from generator-function


Ex2:-(Generator with Loops)
#Program (GeneratorEx1.py)

Ex3:-
#Program (GeneratorEx1.py)
NOTE:-
= We can convert generator into list as follows,
Ex:-
list1 = list(values);
print(list1);

=> Advantages:-
1) Compared to class-level iterators, generators are easy to use
2) Improves Memory Utilization and Performance
3) Best suitable for reading-data from Large No.of Files
4) Works best for web-scraping and crawling


#Program (GeneratorEx1.py)
#Program to work with generators
'''
#generator-func
def mygenf1():
	yield 'A';
	yield 'B';
	yield 'C';

g1 = mygenf1();
print(g1);
print(type(g1));
print()
#get values from gererator-func using next()
print(next(g1));
print(next(g1));
print(next(g1));
#print(next(g1));
'''


'''
#another-example with Loops
def countdown(num):
	print("Start Countdown...");
	while(num>0):
		yield num;
		num=num-1;
	
values=countdown(10);
#values=countdown(20);
print(values);
for x in values:
	print(x);



#with lists using list()
def firstnnums(num):
	i=1;
	while(i<=num):
		yield i;
		i=i+1;
	
values=firstnnums(10);
list1 = list(values);
print(list1);










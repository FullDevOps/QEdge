# 32nd day 32.01-09-22

"""
==>>> MultiThreading in Python:-
= Multi means many (2 or more)
= Threading means small-logics(functions)

Def:-
= Executing 2 or more small-logics parallelly in a same program is called Multi-Threading


NOTE:-
= Multi-Threading  are widely used here,
1) Multimedia Graphics
2) Animations
3) Video Games
4) Web-servers & Application-servers
etc



==> Single-Threaded App v/s Multi-Threaded App:-
= In Single-Threaded App, multiple-tasks are executed one-by-one linearly
==Diagram==
	main-function(.py file)	__main__()
	m1();
	m2();
	m3();
(m1,m2,m3 are executed linearly one-by-one)
	
= In Multi-Threaded App, multiple-tasks are executed parallelly 
==Diagram==
	main-function(.py file)	__main__()
	m1(); or m2(); or m3();
(m1,m2,m3 are executed parallelly)
(PVM executed multi-threads(small-logics/funcs) parallelly)

NOTE:-
= "threading" module in Python provides multi-threading in program
= thread means light-weight-process (doing some sp.task in same-prog)
= Every python-prog by default contains 1-thread known as "Main-Thread"
(__main__())

Ex:-
"""
#Program (ThreadEx1.py)
# (Printing name of current executing thread)
import threading;
print("Current-Executing-Thread : ",threading.current_thread().getName());
"""
NOTE:-
= current_thread() is in threading-module, it gives currently executing thread obj.ref
= On this obj.ref, we call getName(), which gives current executing thread-name

=** Hence Thread is also 1-object in python prog



==> Different ways to create a Thread in Python:-
(3-ways)
1) Creating a thread directly in main-prog
2) Creating a thread extending Thread-class (inheritance sub-class)
3) Creating a thread w.o extending Thread-class 
(our own-class)

(****)
1) Creating a thread directly in our Program:-
Step::-
i)
	= Write your own methodname/function
	Ex:-
		def display():
ii)
= create object of Thread-class from threading-module
Ex:-
	t1 = Thread(target=methodname/funcname);
	t1 = Thread(target=display);
	
iii)	
= use start() of Thread-class to run our method parallely
	t1.start();
	
Ex:-"""
#Program (ThreadEx2.py)
#Program (ThreadEx2.py)
#Creating a Thread directly in program

from threading import *;

#step-1
def display():
	for i in range(1,11):
		print("Child-Thread");
#step-2
t1 = Thread(target=display);
#step-3
t1.start();


#main-thread
for i in range(1,11):
	print("\t\tMain-Thread");


"""
NOTE:-
= Here we get output for Main-Thread & Child-Thread 10 times each with parallelly execution (Random-Execution)
= The pattern differs from Run to run and execution to execution
** Here PVM calls main-thread(program) & we call display() thread



NOTE::-
==> Using Thread-class(Inheritance):-
= It is a pre-defined class present in threading-module
= Using this class we can create our own threads
= To Thread-class constructor, we pass the "target=funcname" attribute
= Such function becomes small-logic of the thread for execution
= To start or executed the method(logic) of thread-obj, we use start() method

		
2) Creating a Thread by extending Thread-class:- (Inheritance)
=i) Create our Child-class inheriting from Thread-class
=ii) Override run() from Parent-class for multi-threading logic
(run() is available in Thread-class, here we perform overriding)
=iii) Create and object of our thread-class
=iv) When we call start(), automatically run() is called for parallel execution

4-steps::
-------
i)
	define our own-class inherited from Thread-class
ii)
	redefine run() method --> overriding
	(it is responsible for parallel-exec)
iii)
	create our own-class object
iv)
	call start() method on our class-object

Ex:-
"""
#Program (ThreadEx3.py)
#Program (ThreadEx3.py)
#Program to multi-threading inheriting from thread-class

from threading import *;

#step-1
class MyThread(Thread):
	def run(self):      #step-2
		for i in range(1,11):
			print("Child-Thread");

#step-3
t1 = MyThread();
#here target=run method automatically(no-need to pass as para)

#step-4
t1.start();


#main-thread-logic
for i in range(1,11):
	print("\t\tMain-Thread");



"""
3) Creating a Thread without extending Thread-class:-
4-Steps::-
i)
= Here also we create our own class with our own method for multi-threading logic (no run())
ii)
= Create an object of our thread class
iii)
= Create an object of Thread class and pass "target=obj.methodname" attribute as parameter to constructor
iv)
= Call start() for parallel execution of given method in our class (using Thread-class obj)

Ex:-
"""
#Program (ThreadEx4.py)
#Program (ThreadEx4.py)
#Program to demo Multi-thread w.o inheriting Thread-class

from threading import *;

#step-1
class Demo:
	def display(self):
		for i in range(1,11):
			print("Child-Thread with display()");

#step-2
obj=Demo();
#Step-3
t1 = Thread(target=obj.display);	
#step-4
t1.start();


#main-thread-logic
for i in range(1,11):
	print("\t\tMain-Thread");


"""
==> Working with Thread-Names:-
= We can give our own names to the threads
= It is done by below methods,
1)t1.getName() => gives name of a thread
2)t1.setName("newname") => sets name of a thread

=** Every thread-obj has implicit-var "name", which represents name of a thread
Ex:- t1.name

NOTE:-
= Default thread-names given to threads are Thread-1, Thread-2, ... so-on

Ex:-
"""
#Program (ThreadEx5.py)
#Program (ThreadEx5.py)
#(Program to work with thread-names)

from threading import *;


#case-1(main-thread)
print(current_thread().name);
#current_thread().name="Hello-Thread";
print(current_thread().name);




#case-2
def display():
	for i in range(1,11):
		#print(current_thread().getName());
		print(current_thread().name);
def show():
	for i in range(1,11):
		#print("\t\t",current_thread().getName());		
		print("\t\t",current_thread().name);		

t1 = Thread(target=display);
t2 = Thread(target=show);
#t1.setName("my-display-thread");
#t2.setName("your-show-thread");
t1.name="my-display-thread";
t2.name="your-show-thread";
t1.start();
t2.start();


"""
==> Thread Identification Number(ident):-
= "ident" is implicit-var to access unique thread identification number
= this identification-no is a unique no. given by PVM during execution
= It identifies each-thread uniquely in program
(int-number)
Ex:-
	t1.ident (from Thread-class)
	t2.ident
"""
# Ex:-
#Program (ThreadEx6.py)
#Program (ThreadEx6.py)
#Prog to demo ident implicit-var

from threading import *;

def test():
	print("Child-Thread");
	
t1 = Thread(target=test);
t2 = Thread(target=test);
t1.start();
t2.start();

print("Main-Thread ident :",current_thread().ident);
print("Child-Thread ident(t1) :",t1.ident);
print("Child-Thread ident(t2) :",t2.ident);



#(Working with thread-methods):-
# ==> active_count():-
# = It givens no.of active-thread currently running or active in python program

# Ex:-
#Program (ThreadEx7.py)
#Program (ThreadEx7.py)
#active_count()

from threading import *;
import time;

def display():	#it is our thread-run()
	print(current_thread().name,"...started");
	time.sleep(2);
	print(current_thread().name,"...ended");

print("No.of active-threads :",active_count());

t1=Thread(target=display,name="ChildThread1");
t2=Thread(target=display,name="ChildThread2");
t3=Thread(target=display,name="ChildThread3");
#t1.name="ChildThread1"

t1.start();
t2.start();
t3.start();
print("No.of active-threads :",active_count());

#main-thread
time.sleep(10);
print("No.of active-threads :",active_count());

print("End of the Main-Thread");

"""
NOTE:-
t1=Thread(target=display,name="ChildThread1");
= we can give names to the threads while creating object of thread-class using name="" parameter



==> enumerate():-
= It returns list[...] of all active-threads(obj.ref) currently running in program
Ex:-
"""
#Program (ThreadEx8.py)
#Program (ThreadEx8.py)
#enumerate()

from threading import *;
import time;

def display():	#it is our thread-run()
	print(current_thread().name,"...started");
	time.sleep(3);
	print(current_thread().name,"...ended");

t1=Thread(target=display,name="ChildThread1");
t2=Thread(target=display,name="ChildThread2");
t3=Thread(target=display,name="ChildThread3");
t1.start();
t2.start();
t3.start();

list1 = enumerate();
print(list1)
for tt in list1:
	print("Thread-Name :",tt.name);

print();	
time.sleep(15);	
list1 = enumerate();
for tt in list1:
	print("Thread-Name :",tt.name);



# ==> is_alive() Method:-
# = Checks whether particular thread is still executing or done its job (True/False)
# Ex:-
#Program (ThreadEx9.py)
#Program (ThreadEx9.py)
#is_alive()

from threading import *;
import time;

def display():	#it is our run()
	print(current_thread().name,"...started");
	time.sleep(2);
	print(current_thread().name,"...ended");
	
t1=Thread(target=display,name="ChildThread1");
t2=Thread(target=display,name="ChildThread2");
t3=Thread(target=display,name="ChildThread3");
t1.start();
t2.start();
t3.start();

#main-thread
print(t1.name,"is Alive :",t1.is_alive());
print(t2.name,"is Alive :",t2.is_alive());
print(t3.name,"is Alive :",t3.is_alive());

print();
time.sleep(15);
print(t1.name,"is Alive :",t1.is_alive());
print(t2.name,"is Alive :",t2.is_alive());
print(t3.name,"is Alive :",t3.is_alive());

print("End of the Main-Thread");


# NOTE:-
# = isAlive() is deprecated(outdated/old)
# = Use is_alive() instead of that










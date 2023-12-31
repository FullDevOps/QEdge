# 33rd day 33.02-09-22

"""
***Other-Methods in Thread-class***
------------------------------------------
==> join():-
= if a thread wants to wait for other-threads to complete their job then we have to use join()
(once all the remaining threads completes their jobs then all thread go for dead-state/go for other-jobs)
Ex:-
#Program (ThreadEx10.py)

NOTE:-
= We can also use join() with time also
Ex:-
	t1.join(5);
= In this case, main-thread waits for 5-seconds	
	t1.join()
"""
#Program (ThreadEx10.py)
#join() method

from threading import *;
import time;

def display():	#it is our run()
	for i in range(10):
		print("Hello-Thread");
		time.sleep(1);
	
def show():		#it is also our run()
	for i in range(20):
		print("\t\tWelcome-Thread");
		time.sleep(1);
        
t1 = Thread(target=display);
t2 = Thread(target=show);
t1.start();
t1.join(5);
#t1.join();
t2.start();
#t2.join();


#main-thread
for i in range(10):
	print("\t\t\t\tMain-Thread");
	time.sleep(1);


"""
==> Daemon Thread:-
(least priority threads)
= Threads which are running in the background are called Daemon-Thread
= They provide support for other non-daemon-threads (main-thread)
Ex:- Garbage-Collector
(When main-thread runs out-of-memory, PVM runs GC thread for to destroy useless objects and provide free-memory, hence main-thread can continue its execution without any memory-problems)

= t1.isDaemon() checks whether a thread is daemon-thread or not
(they are low priority-threads)
= t1.daemon property(variable) checks for same-above

= t1.setDaemon(boolean-value), changes its property 
(used before starting a thread o.w RuntimeException)
Ex:-
#Program (ThreadEx11.py)

==> Daemon Thread:-
(least priority threads)
= less chance for execution in group of threads
=> methods,
= t1.isDaemon()		#True/False
= t1.daemon variable	#True/False
= t1.setDaemon(boolean)
(use before start())
"""
# Ex:-
#Program (ThreadEx11.py)
#Program (ThreadEx11.py)

from threading import *;


#case-1(main-thread)
#current_thread().setDaemon(True);
print(current_thread().isDaemon());
print(current_thread().daemon);


#case-2
def display():	#it is our run()
	while True:
		print("Child-Thread");
	
t1 = Thread(target=display);
print(t1.daemon);
t1.daemon=True;
t1.start();

#main-thread
while True:
	print("\t\tMain-thread");


"""
NOTE:-
= Main-Thread is always non-daemon-thread, its Nature can't be changed because it is already started at beginning only by PVM


==> Synchronization in Multi-Threading:-
(automatic ITC -> Inter-thread-communication)
= If multiple-threads are executing parallelly and accessing same common-sharable-data then there are chances of Data-Inconsistency (Wrong-data updates)
Ex:-
==Diagram==
(Online-Ticket Booking)
(multiple-users)---->website/app---->select-cinema---->theater----->date----->show-time---->seats--->booking/billing/checkout

NOTE:-
= To avoid this, we perform "synchronization"(auto-ITC)
(Proper communication b/w multiple-threads accessing common-sharable-data to avoid Data-Inconsistency/Wrong-data/Wrong-Tranx)
(Critical-Resource)
Ex:-
"""
#Program (ThreadEx12.py)
# (Without Synchronization)
#Program (ThreadEx12.py)
#(Without Synchronization)

from threading import *;
import time;

#common-transaction/func
def wishes(name):		#name is common-sharable-data
	for i in range(10):
		print("Good Morning :",end='');
		time.sleep(1);
		print(name);
		
t1 = Thread(target=wishes,args=("Sai",));
t2 = Thread(target=wishes,args=("Ram",));	
t1.start();
t2.start();


"""
=** Here, we get Irregular-Output, coz both t1 and t2 are execute same common sharable method(wishes()) and output is In-consistent(Wrong)
= To overcome this we perform "Synchronization"
= Here PVM allow only 1-thread to perform operation common-sharable-data or functions and avoids Data-Inconsistency(wrong)
(one-by-one execution)


NOTE:-
= In python, synchronization (auto.ITC) is done in 3-ways,
	1) Lock mechanism
	2) RLock mechanism
	3) Semaphore mechanism

1) Synchronization using Lock concept:-
= Lock is fundamental synchronization mechanism in threading module
= It is created as follow,
Ex:-
	ll = Lock();	#Lock-class-obj
= Lock-obj can be hold by only 1-thread at a time 
(if other thread requires same lock then it will wait till before thread release lock)
Ex:-
Common Telephone Booth, Common Washrooms
= Thread gets lock as follows,
Ex:-
	ll.acquire();
= Thread releases lock as follows,
Ex:-
	ll.release();
(for releasing lock, that thread should be owner of lock o.w we get RuntimeError)

=** Above Both methods are called inside multi-threading logics
(run() or user-defined run() method)

Ex:-
#Program (ThreadEx13.py)
(Lock Mechanism)

NOTE:-
=** Here which ever thread 1st goes to wishes() executes it without and Data-Inconsistency followed by other thread one-by-one
(Hence Synchronization is achieved by Lock()/acquire()/release())
=** Always create and keep Lock-obj ready at begin of Main-Thread
=** use acquire() at beginning of MT-logic
=** use release() at end of MT-logic



NOTE:- (Simple-Lock problem in Lock() mechanism)
= If any thread tries to acquire same lock then it is blocked even though same-thread tries to lock again
(same thread mulitple locks)
Ex:-
#Program (ThreadEx13.py)
(Simple-Lock Problem)

NOTE:-
= To kill Blocked-Thread, use Ctrl+PauseBreak (Ctrl+C)
= Threads calling Recursive-functions or Nested-Access or using Loops then it may acquire same-lock again and gets blocked for itself
(Hence it is not suitable for all-situations)
= To overcome such problem, we go for "RLock"



2)
==> Reentrant Lock:- (RLock())
= It means a thread can hold same-lock again and again
= But if lock is held by other threads then only it is blocked
= this chance is given only for owner-thread
Ex:-
#Program (ThreadEx13.py)
(RLock Problem)

NOTE:-
= For every acquire() of RLock make-sure to release() it
EX:-
rl = Rlock();
rl.acquire();
rl.acquire();
rl.release();
rl.release();
= After 2-release only RLock is released(o.w not)
NOTE:-
= Only same-owner can have RLock multiple-times
= No of acquire() and release() should be matched



==>(RLock Synchronization):-
Ex:-
#Program (ThreadEx13.py)
(RLock Synchronization)
NOTE:-
= Instead of RLock(), if we use Lock() then thread will be blocked for itself

==> Difference b/w Lock() and RLock():-
i) 
= Lock() can be acquired by only 1 thread at a time including owner thread
= RLock() can be acquired by only 1 thread at a time but owner thread can acquire multiple-times
ii)
= Not suitable for Recursive or Looping logics
= suitable for Recursive or Looping logics
iii)
= Lock obj takes care of only Locked or Unlocked information
= RLock obj takes cares of Locked, Unlocked and also owner information, no.of times lock acquire and release
"""

#Program (ThreadEx13.py)
#Synchronization-Lock Mechanism using Lock()

#using Lock()
from threading import *;
import time;



#Lock-class-obj mechanism
#step-1
ll=Lock();
def wishes(name):	#wishes() is run() method
	ll.acquire();
	for i in range(10):
		print("Good Morning :",end='');
		time.sleep(1);
		print(name);
	ll.release();

t1 = Thread(target=wishes,args=("Sai",));
t2 = Thread(target=wishes,args=("Ram",));
t3 = Thread(target=wishes,args=("Ali",));	
t1.start();
t2.start();
t3.start();
'''

'''
#Simple-Lock mechanism small-Problem
from threading import *;
ll=Lock();
print("Main-Thread acquiring Lock");
ll.acquire();
print("Main-Thread again acquiring same-lock");
ll.acquire();
'''


'''
#RLock() mechanism with multiple-locks
from threading import *;
import time;
#step-1
rl=RLock();
print("Main-Thread acquiring RLock");
rl.acquire();
print("Main-Thread again acquiring same-Rlock");
rl.acquire();
time.sleep(3)
print("Main-Thread is not Blocked");
print("End of the Program");




#Semaphore-Mechanism
from threading import *;
import time;
sp=Semaphore(2);
def wishes(name):
	sp.acquire();
	for i in range(10):
		print("Good Morning :",end='');
		time.sleep(1);
		print(name);
	sp.release();
	
t1 = Thread(target=wishes,args=("Sai",));
t2 = Thread(target=wishes,args=("Ram",));
t3 = Thread(target=wishes,args=("Ali",));	
t4 = Thread(target=wishes,args=("Tom",));
t1.start();
t2.start();
t3.start();
t4.start();


"""
3) Synchronization using Semaphore:-
= Here it allows to access common-sharable-data or resource by multiple-threads at a time
= It allows limited no.of sharings of data or resource b/w multiple-threads
= It is advanced Synchronization Mechanism
= Its object is created as follows,
Ex:-
sp = Semaphore(counter);
= counter is max.no.of threads for parallel access of data
= default is 1

= When thread acquires a lock then counter is decremented by 1
= When thread releases a lock then counter is incremented by 1

Case1:-
sp1 = Semaphore();
= Here it allows only 1-thread at a time to lock the data/resource
(same as Lock())

Case2:-
sp2 = Semaphore(5);
= Here it allows 5-threads at a time to lock the data/resource
(remaining threads wait)

Ex:-
#Program (ThreadEx14.py)
(Semaphore-Mechanism)
NOTE:-
= Here only 2-threads are allowed to access wishes() and remaining will be waiting



(2-types of Semaphore)
==> Regular & Bounded Semaphore:-
= Regular Semaphore is unlimited wrt to release() method, to increment counter
= Sometimes counter may exceed no.of acquire() also
Ex:-
#Program (ThreadEx13.py)
(Regular Semaphore)
sp = Semaphore(2);

= However, in Bounded-semaphore, no.of release() should not exceed no.of acquire() calls o.w we get "ValueError"
Ex:-
#Program (ThreadEx13.py)
(Bounded-Semaphore)
sp = BoundedSemaphore(2);

NOTE:-
= Recommended to use BoundedSemaphore() than Semaphore()

==> Difference b/w Lock() and Semaphore():-
1)
= Lock-obj can be obtained by only 1-thread
= Semaphore-obj can be obtained by multiple fixed no of threads using a counter parallelly

NOTE:-
= Advantage is Synchronization is to avoid Data-Inconsistency problems
= Dis-Advantage is increases waiting-time and performance issues
"""





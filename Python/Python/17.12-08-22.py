# 17th day 17.12-08-22

"""
==>> Lambda Functions::-
= they are anonymous funcs (func w.o names)
= they are defined with lambda keyword
= they take input-values(args/para) & directly return a value
=*** def, return keywords are not required
=* they are specially used for instantly used funcs
(use then & there only)
Ex:-
==Diagram==
regular-func v/s lambda-func
=** Advantage is,
	= func code-lines is reduced
NOTE:-
= in python, everything is object, even func is also one-object with func.ref.var(f1,f2,sqr,ss)
"""	

##Program...(FunctionEx5.py)
#Program for Lambda-functions(Anonymous-Funcs)


#Prog for square of num using Lamda-Func
ss = lambda n: n*n;
print("Square of 5 :",ss(5));
print("Square of 9 :",ss(9));
'''

'''
#Prog for sum of 2 nums using Lamda-Func
ss = lambda a,b : a+b;
print("Sum of 10,20 :",ss(10,20));
print("Sum of 11,22 :",ss(11,22));
'''

'''
#Prog for bigger of 2 nums using Lamda-Func
ss = lambda a,b : a if a>b else b;
print("Bigger of 10,20 :",ss(10,20));
print("Bigger of 11,22 :",ss(111,99));
'''

#sp-cases of lambda-func
'''
#Prog to filter only even-nums from List using filter()
#filters the coll.of.data Ex:- filter(func,coll)->T(accept)/F(reject)
#With Lambda-Func
list1 = [11,22,33,44,55,66];
list2 = list(filter(lambda x : x%2==0,list1));
print(list2);
list2 = list(filter(lambda x : x%2!=0,list1));
print(list2);
'''

'''
#Prog to generate sqr-nums from List using map()
#map(func,coll)
#With Lambda-Func
list1 = [1,2,3,4,5];
list2 = list(map(lambda x : x*x,list1));	
print(list2);

#map() with multiple-lists
list1=[1,2,3,4,10];
list2=[1,2,3,4,10];
list3 = list(map(lambda x,y:x*y,list1,list2));
print(list3);
'''

'''
#reduce(func,coll) ---> functools.py module(import it)
from functools import *;
list1 = [11,22,33,44,55];
result = reduce(lambda x,y:x+y, list1);
print(result);
result = reduce(lambda x,y:x*y, list1);
print(result);



#Sum of N-Nums
from functools import *;
result = reduce(lambda x,y:x+y, range(1,101));
print(result);


filter() #---> we get less no.of.values
map() #---> we get equal no.of.values
reduce() #---> we get single values
# (all takes lambda-func)


"""
==> Lamda functions are commonly used with filter(), map() and reduce() functions:-
= These funcs take function as argument/para
(here we pass lamda function as input-para to given functions)

1) filter():-
= It is used to filter-values from given-sequence of values based on some condition
Syn:-
	filter(function,sequence)
= function as arg, performs conditional-check
= sequence is List/Tuple/String/Rangeofvalues

//Program (FunctionEx5.py)
(Prog to filter only even-nums from List using filter())


2) Map():-
= For every-element in given sequence, apply some functionality and generate new-element (with some modifications)
Ex:-
= For every-element in (1 to 10), generate squares
	map(function,sequence)
	
//Program (FunctionEx5.py)
(Prog to generate sqr-nums from List using map())
 	
NOTE:-
= map() can be applied on multiple-lists also but both should have same-length
Ex:-
list1=[1,2,3,4];
list2=[1,2,3,4];
list3 = list(map(lambda x,y:x*y,list1,list2));
print(list3);

=** x is taken from list1 and y is taken from list2

3) reduce():-
= It reduces sequence of elements into single-element by applying given function as arg
= Syn:
	reduce(function,sequence)
	
= This function is in "functools" module, hence import it.
Ex:-
from functools import *;
list1 = [11,22,33,44,55,66];
result = reduce(lambda x,y:x+y, list1);
print(result);

//Program (FunctionEx5.py)
	
Ex:-
result = reduce(lambda x,y:x*y, list1);
print(result);

Ex:-
from functools import *;
result = reduce(lambda x,y:x+y, range(1,101));
print(result);

NOTE:-
= In import *, * indicates all-functions


===> Function Aliasing(Referencing)::-
==> Function as Object:-
= In python, everything is an object
= Even functions are also objects
= Every function-name has unique reference/address

Ex:-
def f1():
	print("Hello World");
print(f1);
print(id(f1));

//Program (FunctionEx6.py)
(Every function is an object)


=> Function Aliasing:-
= For existing function, we can give another name (alias)
= alias means alternate-name or another-name
Ex:-
def f1(name):
	print("Hello :",name);
	
f2=f1;
f1("Sai");
f2("Ali")
print(f1);
print(f2);
print(id(f1));
print(id(f2));

=** Here we have only 1-function, it can be called with f1 or f2 names
= If we delete 1-name still we can access that func with alias name

Ex:- (Function Ref-deletion)
def f1(name):
	print("Hello :",name);
	
f2=f1;
f1("Sai");
f2("Ali")
del f1;
f1("Sai");
f2("Ali")



==> Nested Functions:-
= Defining one-func inside another func is called Nested-Functions
Ex:-
"""
def f1():
	print("f1() is Outer-Func");
	def f2():
		print("f2() is Inner");
	print("f1 is calling f2-Func");
	f2();
f1();
#f2(); #NameError, f2 is not-defined
		
##Program (FunctionEx6.py)
# (Nested-Functions)


##Program (FunctionEx6.py)
##Program to work with functions


#Every-function is an object
def f1():
	print("Hello World");
f1();
print(f1);
print(id(f1));
'''
'''
#function-aliasing(another-name)
#same-fun-def and diff-names
def f1(uname):
	print("Hello :",uname);

f1("Sai");
f2=f1;		#f1----->(def.....)<-------f2
f2("Ali")
print(f1);
print(f2);
print(id(f1));
print(id(f2));
'''

'''
#sp-case
#function-ref.var-deletion
def f1(uname):
	print("Hello :",uname);
	
f2=f1;		#f1----->[def....]<-----f2
f1("Sai");
f2("Ali")
del f1;		#      [def....]<-----f2
#f1("Sai");
f2("Ali")


#Nested-Functions (func with-in func) local-func(local-access)
def f1():
	print("f1() is Outer-Func");
	def f2():
		print("f2() is Inner-Func");
	print("f1 is calling f2");
	f2();

f1();
#f2(); #NameError



"""
========================================================================================================================
==> Date & Time in Python:-
= Python provides different ways to handle Date and Time
= Python provides "time" and "calendar" and "datetime" modules (.py files)
(we have to use this modules and work with date&time)
Ex:-
	import time;
	import calendar;
	import datetime;

(BASICS)
=> What is Tick?
(representing date&time in seconds/ticks)
= Date and Time are taken as float numbers (in seconds)
= Particular Date & Time is taken in seconds since "Jan 1st, 1970 00:00:00 AM"

==> Current System Date & Time?
= time module with time() gives current system date&time (in Ticks)
Ex:-
import time;
sysdatetime = time.time();
print(sysdatetime);

##Program (DateTimeEx1.py)
#Program to work with Date & Time


==> Getting Current-Time:-
= time-module
= For this we use localtime()
Ex:-
import time;
currenttime = time.localtime(time.time());
print(currenttime);

=** for localtime(), pass Tick-time as parameter
= Tick-time seconds is converted to TimeTuple(9 values) Ex:-struct-time()

=> Getting Formatted-Time:-
(Proper data & time in understandable format)
= asctime() gives Date and Time in simple format
Ex:-
import time;
formattedtime = time.asctime(time.localtime(time.time()));
print(formattedtime);

NOTE:-
= 3 methods to work with date & time
time()--->localtime()---->asctime()



=> Getting Calendar of Month:-
= "calendar" module gives monthly and yearly calendars
"month()"
Ex:-
import calendar;
cal = calendar.month(2023,03);
print(cal);

=* 1st parameter is Year
=* 2nd parameter is Month(1-12)



==> time module:-
= time module provides different functions and attributes(variables) to work with time-representations

1) time.altzone:-
= It is attribute, which gives Local DST timezone (offset) in seconds
Ex:-
import time;
print(time.altzone);

2) time.asctime():-
= This method gives date&time as "Thu Nov 14 20:00:09 2019" format
= It converts TimeTuple or struct_time to Local-Time
Ex:-
import time;
datetime = time.localtime();
print(time.asctime(datetime));

3) time.clock():- (NA)
= It gives seconds elapsed since 1st time call of function
Ex:-
import time;
print(time.clock());
time.sleep(5.5);	#sleeps for 5.5 seconds
print(time.clock());

4) time.ctime():- 
= It gives Local-Time by converting seconds elapsed from Jan 1,1970 00:00:00
Ex:-
import time;
datetime = time.ctime();
print(datetime);
=** no-need to use time(), localtime(), asctime()

5) time.gmtime(sec) (not-req)
= It gives struct_time values for given seconds
= If no para is given then current sysdatetime is taken
Ex:-
import time;
print(time.gmtime());
print(time.gmtime(300));

6) time.localtime(sec)
= It gives TimeTuple values for given seconds
= If no para is given then current sysdatetime is taken
Ex:-
import time;
print(time.localtime());
print(time.gmtime(300));


(Other-Methods)
7) time.mktime()
= It gives seconds elapsed since Jan 1st, 1970 00:00:00 for given localtime or TimeTuple
Ex:-
"""
import time;
timetup = (2009, 2, 17, 17, 3, 38, 1, 48, 0);
secs = time.mktime(timetup );
print(secs);
print(time.asctime(time.localtime(secs)))
"""
8) time.sleep(sec)
= It makes the program execution sleep for given no.of seconds(int/float)
Ex:-
import time;
print(time.ctime());
time.sleep(5);
print(time.ctime());

9) strftime()	-> (NReq)
= Provides date&time in required formatted string (using format-specifiers %char)

10) strptime() -> (NReq)
= Takes formatted-string date&time using format-specifiers and gives struct_time

11) time.time()
= Gives date&time as seconds elapsed from Jan 1st, 1970 00:00:00
Ex:-
import time;
print(time.time())
print(time.asctime(time.localtime(time.time())));
-----------------------------------------------------
12) time.timezone 	(time zone offset in seconds)
13) time.tzname		(local time zone name)


==> calendar module:-
= calendar module provides different functions to work with calendars
= By default it takes Monday as 1st day of week (Mon-Sun as 0-6)

Ex:-
calendar(YEAR,width b/w date,lines b/w weeks,charspaces b/w cal)
Ex:-
"""
import calendar 
print(calendar.calendar(2021,2,1,6))

print(calendar.firstweekday()); #Mon-0
print(calendar.isleap(2020));	#True or False

print(calendar.leapdays(2020,2030)); #Leap days b/w 2 years

# print(calendar.calendar(Year,Month,))#width b/w dates,lines b/w weeks)
print(calendar.month(2020,11,2,1));

# print(calendar.monthcalendar(Year,Month));
print(calendar.monthcalendar(2020,11)); #Nested Lists with weeks

print(calendar.monthrange(2020,11)); #1st date weekday & No.ofdays

calendar.prcal(2020,2,1,6);	#Prints Year Calendar
calendar.prmonth(2020,11,2,1);	#Prints Year Calendar
calendar.setfirstweekday(6);	#Mon-Sun(0-6)

print(calendar.weekday(2020,11,14)); #gives weekday-code(0-6 mon-sun)


"""
==>#datetime module
= In this module, we have datetime-class
= In that class, we have now() method/function
= now() method gives current system date&time
Ex:-
import datetime;
date1 = datetime.datetime.now();
print(date1);
"""


##Program (DateTimeEx1.py)
#Program to work with Date & Time


#time()-->time-module
import time;
sysdatetime = time.time();
print(sysdatetime);
'''

'''
#localtime()
import time;
currenttime = time.localtime(time.time());
print(currenttime);
#it gives struct_time as time-tuple with 9-values
'''

'''
#asctime()
import time;
formattedtime = time.asctime(time.localtime(time.time()));
print(formattedtime);
'''

'''
#ctime()
import time;
formattedtime = time.ctime()
print(formattedtime);
'''

'''
#time module (altzone-var)
import time;
print(time.altzone);
'''

'''
#sleep() with ctime()
import time;
print(time.ctime());
time.sleep(5);	#sleeps for 5 seconds
print(time.ctime());
'''

'''
#digital-clock
import time;
while True:
	ct = time.localtime(time.time())
	print(ct[3],":",ct[4],":",ct[5],end="\t\r")
	time.sleep(1)
'''

'''
#time-module(vars)
import time;
print(time.timezone);
print(time.tzname);


#calendar module
import calendar;
#print(calendar.calendar(2022,2,1,6));
#print(calendar.calendar(2022,2,0,6));
#print(calendar.firstweekday());
#print(calendar.isleap(2020));
#print(calendar.isleap(2022));
#print(calendar.leapdays(2020,2032)); 
#print(calendar.month(2022,8,2,1));
#print(calendar.monthcalendar(2022,12));
#print(calendar.monthrange(2022,8));
#print(calendar.monthrange(2022,9));
#calendar.prcal(2022,2,1,6);
#calendar.prmonth(2022,8,2,1);
#calendar.setfirstweekday(6);
##calendar.prmonth(2022,8,2,1);
#print(calendar.weekday(2022,8,12)); 
#gives weekday-code(0-6 mon-sun)


#datetime module (classes & objects)
import datetime;
date1 = datetime.datetime.now();
print(date1);




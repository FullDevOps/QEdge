# 28th day 28.26-08-22

"""
***How to Handle Exceptions??***
==> How to do Exception-Handling in Program?
= Every exception is an object in Python with some corresponding class
= Exception-obj is created automatically by PVM when it occurs
= PVM searches for Exception-Handling code in prog and if not there then Interpreter terminated prog-exec-abnormally
= PVM also prints corresponding Exception-Info also
= Finally, rest of program is Not-Executed (Abnormal-Termination)

Ex:-
//program..."""
#(ExceptionEx1.py)
#Program to generate exception (ExceptionEx1.py)
#Abnormal-Termination of Program

print("Division Program in Python");
a = int(input("Enter A : "));
b = int(input("Enter B : "));
c = a/b;
print(c);
print("End of Program");
"""
NOTE:-
= In python, Every exception is an object, it has 3-properties,
a) Exception-Type (Exception-Classname)
b) Exception-Message (division by zero)
c) Exception-State (line-no,prog-name,module-name)
(Except-object is automatically created by PVM***)


(Pre-defined Exception-classes)
==> Inbuilt-Exception classes in Python:- 
(Hierarchy --> B.C & its S.C)
==Diagram==(refer-notes)

=> BaseException
	= Exception
		- AttributeError
			* ZeroDivisionError
			* FloatingPointError
			* OverFlowError
		- ArithmeticError
		- EOFError
		- NameError
		- LookupError
			* IndexError
			* KeyError
		- OSError
			* FileNotFoundError
			* InterruptedError
			* PermissionError
			* TimeOutError
		- TypeError
		- ValueError
	= SystemExit
	= GeneratorExit
	= KeyboardInterrupt
NOTE:-
= Every exception is a class
= "BaseException" is top-level Parent-class (Root) and remaining all are Child-classes
= "Exception" class and it child-class are important for Exception-Handling mechanism



==> Steps for Exception-Handling:-
=> How to Handle Exception in Program?
= It is done with try-except (indented block-of-code)

Step-1) 
	= Monitor or Detect the exception in prog
	= It is done with try-block(header & suite)
Syntax:- 
	try:
		......
		.code.
		......
	
Step2)
	= When exception-occurs, raise it (alert or warning)
	= it is done with raise-stmt
Syntax:-
	try:
		...
		c=a/b;  #raise ZeroDivisionError();
		....
*** All pre-defined exceptions are automatically created(obj) & raised by PVM

Step3:-
	= Now accept the exception occured in try-block
	= it is done with except-block(header & Suite)
Syntax:-
	try:
		...
		c=a/b;  #raise ZeroDivisionError();
		....
	except ZeroDivisionError:
		........
		..body..
		........

**= for except-block, pass Exception-Classname(type)
(use except-Block immediately after try-block)

Step4:-
	= Provide proper-solution in body of except-Block


NOTE:-
= Hence Exception-Handling mechanism is done successfully & NO Abnormal-Termination of Prog(normal-execution)

"""
# Ex:-
#Program (ExceptionEx2.py)
# (Program to generate exception & handle exception)
#Program to generate exception & handle exception
#ExceptionEx2.py

print("Division Program in Python");
a = int(input("Enter A : "));
b = int(input("Enter B : "));

try:
	c = a/b;
	print(c);	
except ZeroDivisionError:
	print("Division by 0 NOT OK");
print("End of Program");

"""
NOTE:-
1) Where there is no-exception in try-block then except-block is not executed and remaining stmts after except-block are executed for normal-execution
2) Where there is exception in try-block then except-block is executed and remaining stmts after except-block are executed for normal-execution
3) When exception occurs in try-block, it skips remaining stmts in try-block and control goes to immediate except-block
4) When exception-occurs in try-block and there is no matching except-block then it leads to Abnormal-Termination of Prog
5) If exception-occurs in except-block or remaining stmts after except-block then it is abnormal-termination of prog


==> Printing Pre-defined Exception Information:-
= It means exception-object 3-properties
(exception-type/msg/state)

Ex:-"""
#Program (ExceptionEx3.py)
# (Program to display exception-info)
#Program to display exception-info
#Program (ExceptionEx3.py)

print("Division Program in Python");
a = int(input("Enter A : "));
b = int(input("Enter B : "));
try:
	c = a/b;
	print(c);
except ZeroDivisionError as msg:
	print("Division by 0 NOT OK");
	print("Exception-Message :",msg);

print("End of Program");


"""
==> try with multiple-except blocks:-
= For single try-block, we can  have multiple except-blocks
= Depending on exception-type in try-block, corresponding except-block is executed
Ex:-
try:
	...
	...
	...
except Type1:
	...
except Type2:	
	...
except Type3:
	...
............
............
"""
#Program (ExceptionEx4.py)
# (Program to demo multiple-except-blocks)
#Program to demo multiple-except-blocks

print("Division Program in Python");
try:
	a = int(input("Enter A : "));
	b = int(input("Enter B : "));
	c = a/b;
	print(c);
except ZeroDivisionError:
	print("Division by 0 NOT OK");
except ValueError:
	print("Provide Proper int-value");	
print("End of Program");

"""
NOTE:-
= In multiple-except-blocks, 1st exception raised from try-block is executed by corresponding except-block
= And also only 1 exception is processed at a time (i.e, 1st raised exception) [1st come, 1st server]
= If in multiple-except-blocks matching except-block is not present then it leads to Abnormal-Termination of Prog


==> Single except-block handling multiple-exceptions:-
= Single except-block can handle multiple-exceptions as follows,
Ex:-
except(Exception1,Exception2,...):
(or)
except(Exception1,Exception2,...) as msg:

=* parenthesis() are mandatory
= group of exceptions are taken as tuple
"""
# Ex:-
#Program (ExceptionEx5.py)
# (Program to demo single-except-block with multi-exceptions)
#Program to demo single-except-block with multi-exceptions
#ExceptionEx5.py

print("Division Program in Python");
try:
	a = int(input("Enter A : "));
	b = int(input("Enter B : "));
	c = a/b;
	print(c);
except (ZeroDivisionError, ValueError) as msg:
	print("Exception : ",msg);	
print("End of Program");

"""

==> Default except-Block:-
= It is used to handle any type of exception
= Mainly used when we dont know type of exception in try-block and displaying general-exception-msgs

Syntax:-
except:		#do not give any Classname
	stmts;
=** Use it at the end of all the except-blocks (o.w syntax-error)

Ex:-"""
#Program (ExceptionEx6.py)
# (Program to demo default-except-block)
#Program to demo default-except-block

print("Division Program in Python");
try:
	a = int(input("Enter A : "));
	b = int(input("Enter B : "));
	c = a/b;
	print(c);
#except:
	#print("Default-Except-Block : Unknown Exception occurred");
except ZeroDivisionError:
	print("Division by 0 NOT-OK");
except:
	print("Default-Except-Block : Unknown Exception occurred");
print("End of Program");

"""
NOTE:-
= Possible except-blocks definitions,
1) except ZeroDivisionError:
2) except ZeroDivisionError as msg:
3) except (ZeroDivisionError,ValueError):
4) except (ZeroDivisionError,ValueError) as msg:
5) except:



==>finally block:-
= finally-block is used at the end of all the except-blocks
= This block is executed whether exception is raised or not in try-block
**= Its main purpose is cleaning up resources in program at the end of all the except-blocks
(Resource Deallocating or Releasing Codes)
Syntax:-
try:
	....
except:
	....
except:
	....
...
...
finally:
	....
=* It is executed whether exception occurs or not (OR) exception is handled or not

Ex:-"""
#Program (ExceptionEx7.py)
# (Program to demo finally-block)
#Program to demo finally-block

print("Division Program in Python");
try:
	a = int(input("Enter A : "));
	b = int(input("Enter B : "));
	c = a/b;
	print(c);
#except ZeroDivisionError:
except NameError:
	print("Division by 0 NOT OK");
except ValueError:
	print("Provide Proper int-value");	
finally:
	print("Finally Block is executed");
	
print("End of Program");

"""
NOTE:-
=** it is executed if exception is handled or not(abnormal-termination also)

NOTE:-(Sp.case of finally-block)
= Only 1 situation where finally block is not-executed
i.e, os._exit(0) function  
(0 is normal-termination of Py-Prog)
(1 is abnormal-termination of Py-Prog)
= This function shuts down PVM by OS
(_exit(0) is in os-module)
"""
# Ex:-
#Program (ExceptionEx8.py)
#Program (ExceptionEx8.py)
#Program to demo finally-block not executed sp-case

import os;
try:
	print("try-block");
	os._exit(0);
except ValueError:
	print("ValueError");	
except:
	print("Unknown-Exception");
finally:
	print("Finally-block executed");
	
print("End of the Program");




# 29th day 29.27-08-22

"""
==> Nested try-except-finally block:-
(Nested-Exceptions)
(Nested try-blocks)
= We can have try-except-finally inside any other try/except/finally blocks
Ex:-
try:
	...
	try-except-finally
	...
except:
	...
	try-except-finally
	...
finally:
	...
	try-except-finally
	...

NOTE:-
***Advantage is,
	= Inner try-block exceptions are handled by inner-except-Block o.w they can be handled by outer-except-Block also
"""
	
# Ex:-
#Program (ExceptionEx9.py)
# (Program to demo nested try-blocks)
#Program to demo nested try-blocks
#Program (ExceptionEx9.py)

print("Division Program in Python");
try:
	print("Outer try-block");
	a = int(input("Enter A : "));
	b = int(input("Enter B : "));
	try:
		print("Inner try-block");
		c = a/b;
		print(c);
	except NameError:
		print("Inner except-block");
		print("NameError occurred");
	finally:
		print("Inner finally-block");	
except ZeroDivisionError:
	print("Outer except-block");
	print("Division by 0 NOT OK");
except ValueError:
	print("Outer except-block");
	print("Provide Proper int-value");	
finally:
	print("Outer Finally Block is executed");

print("End of Program");
"""


NOTE:-
= If control enter try-block (inner/outer) its corresponding finally-block is executed (whether exception is raised or not)

NOTE:-
= Exception occurred in finally-block is Abnormal-Termination of Program



==> else Block with try-except-finally blocks:-
(else block with exceptions)
= We can use else block with try-except-finally blocks
= It is executed only if there is NO-exception inside try-block
Ex:-
try:
	...
except:
	... (executed if exception occurs in try-block)
else:
	... (executed if no-exception occurs in try-block)
finally:
	... (executed if exception is there or not in try-block or handled or not in except-block)

=**else-block is used before finally-block
"""

# Ex:-
#Program (ExceptionEx10.py)
#Program (ExceptionEx10.py)
#Program to demo else-block in exceptions
try:
	print("try-block");
	a = int(input("Enter A : "));
	b = int(input("Enter B : "));
	c = a/b;
	print(c);
except:
	print("Div by 0 NOT-OK or Any other Exception");	
else:
	print("Else-Block executed for NO-Exception");
finally:
	print("Finally-Block");


"""

(Our-own Exceptions)
==> Types of Exception:-
= There are 2-types of exceptions,
1) Pre-defined Exceptions
2) User-defined Exceptions(**)

1) Pre-defined Exceptions:-
= Also called Inbuilt-Exceptions
= They are automatically raised by PVM when occurs in prog
Ex1:-
= When 10/0 is performed in prog then ZeroDivisionError is automatically raised by PVM
Ex2:-
= When int("ten") is done in prog then ValueError is automatically raised by PVM

2) User-Defined Exceptions:-
= Also called Customized Exceptions or Programatic Exceptions
= These exceptions are defined & raised by programmer as per requirement in program/coding
= "raise" keyword is used in try-block to raise UD-Exceptions
Ex:-
raise InsufficientFundsException
raise InvalidPinException
etc

==> How to define and work with UD-Exceptions?
Step1:-
= Inherit our UD-Exception class from pre-defined Exception base-class
(Child-class is a kind of Parent-class)

Syntax:-
class UDExceptionClassname(Predefined-Exception-Class):
	def __init__(self,arg):
		self.msg=arg;
Ex:-
class InsufficientFundsException(Exception):
	def __init__(self,arg):
		self.msg=arg;	
		#here self.msg becomes our UD-Exception Message
(Now our class can participate in Exception-Handling-Mechanism)

Step2:-
(use raise-stmt to raise an exception, when it occurs)
=** When UD exception occurs, raise it as follows,
Ex:-
	raise InsufficientFundsException("any-message");

=**here our exception-class-obj is created & its constructor is exec.automatically(__init__()) 


Step3:-
=** accept your exception in except-Block & give proper-solution
"""



# Ex:-
#Program (ExceptionEx11.py)
#Program to demo UD Exception

import time;

class InsufficientFundsException(Exception):
	def __init__(self,msg):
		self.msg=msg;	#this is our UD-Exception Message

#main-prog
print("ATM Transaction");
print("********************************");
acbal = 5000;
print("Initial-Balance ::",acbal);
wamt=int(input("Enter Withdraw Amount : "));		#6000
time.sleep(5)
try:
	if wamt > acbal:
		raise InsufficientFundsException("Less Funds in Account...");
	else:
		acbal = acbal - wamt;
	print("Balance after Successuful-Transaction : ",acbal);
except InsufficientFundsException as msg:
	print(msg)
	print("Transaction NOT possible!!!");


time.sleep(5)
print("********************************");
print("Account Balance : ",acbal);
print("End of the ATM Transaction");

"""

NOTE:-
= For UD-Exceptions also, objects created in raise stmt
= For this object also we have 3-properties
(Exception-class-type/Message/Type)
"""


"Assignment"
##WAP to perform ATM transaction using "InvalidPinException"
#Program (ExceptionEx12.py)

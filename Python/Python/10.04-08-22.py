# 10th day 10.04-08-22

"""
==>> Numbers in Python:-
= Numbers mean numeric-values
= Python supports 3-types of numeric-values,
	a) int-type (10)
	b) float-type (10.5)
	c) complex-type (5+6j)
	
= For number dtypes, we have conversion funcs,
a) int()
b) float()
c) complex(a)	---> a+0j
d) complex(a,b) ---> a+bj

NOTE:-
= Python provides diff.funcs, using which we can perform mathematical-oper


==> Mathematical Functions in Py-Numbers:-
= Python provides "math.py", pre-defined module(lib-file)
= Here we hae diff. mathematical-funcs
Ex:-
	square-root
	logarithm
	trignometric
	factorial
	etc...
	
"""	
##Program (MathFuncs.py)
##(Program to demo different Mathematical-Functions)
"""
NOTE:-
(using a module)
step1:-
	import math; module in program
step2:-
	use respective funcs or vars (.dot operator)
	math.sqrt(100)
	math.pi


1) abs(x):-
= It gives absolute (positive) value of given number "x"(Numeric-Expr)

2) ceil(x):-
= It gives least-integer-value which is greater-than or equals to given value
Ex:- 10--10.5--11(11 is ceil of 10.5)
= It is in math module (import it)
Ex:-
from math import ceil;
import math;

3) factorial()
= it gives factorial of given number
	math.factorial(5)

4) exp(x):-
= It gives exponential of x (e power of x)
= It is in math module

5) fabs(x):-
= It gives absolute value(+ve) of x
= it is mainly used on float-value(also works on int-values)
= It is in math-module

6) floor(x):-
= It gives next/greatest-integer-value which is greater-than or equals to given-value
= It is in math module (import it)

7) log(x):-
= It give natural logarithm value of x (log to the base-e)
= and x>0 (compulsory)
= It is in math-module

8) log10(x):-
= It give logarithm value of x (base-10)
= and x>0 (compulsory)
= It is in math-module

9) max(x,y,z,...):-
= It gives maximum value from given args

10) min(x,y,z,...):-
= It gives minimum value from given args

11) modf(x):- (it works on float-values)
= It gives fractional-part and integer-part of given value
= It is given as tuple-value
= It is in math-module
(both values are given as decimal-point values)

12) 
pow(x,y):-
= Gives x to the power of y
pow(x,y,z):- (Not-Working)
= Gives pow(x,y)%z
= It is in math-module

13) round(x,n):-
= it gives rounded value of to n-digits after decimal-point
= If next-digit is >=5 then it rounds to next-digit
= If n is -ve then it rounds n-digits before decimal-point
(Here it is done based on 1's, 10's, 100's, 1000's places)
= If n value is not given then it is rounded to decimal-point itself

14) sqrt(x):-
= It gives square-root of given number (x>0)
= it is in math-module
"""


##Program MathFuncs.py
##(Program to demo different Mathematical-Functions)

import math;

#abs() function
print(abs(-9));
print(abs(9));
print(abs(0));
print(abs(-0));
print(abs(-9.5));
print(abs(9.5));
print(abs(0.0));
print(abs(-0.0));
'''

'''
#ceil() function (upper/next int-value)
from math import ceil;  #.dot is not-req
print(ceil(9.8));
print(ceil(9.2));
print(ceil(9.0));
print(ceil(9));
print(ceil(-9));
'''

'''
import math;
print(math.ceil(-9.8));
print(math.ceil(-9.2));
print(math.ceil(-9.0));
print(math.pi);
print(math.ceil(math.pi));
'''

'''
#exp() function (e--->Euler's number)
import math;
print(math.exp(3));
print(math.exp(-3));
print(math.exp(3.5));
print(math.exp(-3.5));
print(math.exp(0));
print(math.exp(1));		
#We get exact e-value(2.718281828459045)
'''

'''
#fabs() function
import math;
print(math.fabs(3));
print(math.fabs(-3));
print(math.fabs(3.5));
print(math.fabs(-3.5));
print(math.fabs(0));
print(math.fabs(-0));
'''

'''
#floor() function (lower/prev int-value)
from math import floor;
print(floor(9.8));
print(floor(9.2));
print(floor(9.0));
print(floor(9));
print(floor(-9));
'''
'''
import math;
print(math.floor(-9.8));
print(math.floor(-9.2));
print(math.floor(-9.0));
print(math.pi);
print(math.floor(math.pi));
'''

'''
#log() function (base-e)
import math;
print(math.exp(1));		#We get exact e-value
print(math.log(math.exp(1)));	#e power 0 is 1
print(math.log(10));
#print(math.log(-10));	#Error
print(math.log(10.5));
'''

'''
#log10() function (log value to base-10)
import math;
print(math.log10(10));
#print(math.log10(-10));	#ValueError
print(math.log10(10.5));
print(math.log10(1));
'''

'''
#max() function
print(max(10,20,30));
print(max(-10,-20,-30));
print(max(10.5,20.5,30.5));
print(max(-10.5,-20.5,-30.5));
'''

'''
#min() function
print(min(10,20,30));
print(min(-10,-20,-30));
print(min(10.5,20.5,30.5));
print(min(-10.5,-20.5,-30.5));
'''

'''
#modf() function(tuple())
import math;
print(math.modf(10.56));
print(math.modf(-10.56));
print(math.modf(10));
print(math.modf(-10));
print(math.modf(0));
print(math.modf(0.0));
'''

'''
#pow() function
import math;
print(math.pow(10,3));
print(math.pow(10,-3));
print(math.pow(100,0.5));	#it is 10 power 0.5(1/2) i.e. sqrt(100)
'''

'''
#round() function
print(round(10.12345,3));
print(round(10.12345,4));
print(round(12345.12345,-3));
print(round(12345.12345,-2));	
print(round(12345.12345,-1));
print(round(12545.12345,-3));
print(round(10.123));
print(round(10.789));
'''

'''
#sqrt() function
import math;
print(math.sqrt(100));
print(math.sqrt(10.56));
print(math.sqrt(-10));		#ValueError


#factorial() function
import math
print(math.factorial(5))
print(math.factorial(6))



"""
==> Trigonometric Functions:-
= they are available in math-module (import math)
Ex:-
	sine, cosine, tangent etc (angles & radians)

"""
##Program (TrigonometricFuncs.py)
#Program to demo Trigonometric-Functions)

"""
1) sin(x):-
= Give sine of x (x in radians)
= here x radians should be converted to angles
= Angle => x*pi/180
= It is in math-module


2) cos(x):-
= Give cosine of x (x in radians)
= Angle => pi/180
= It is in math-module

3) tan(x):-
= Give tangent of x (x in radians)
= Angle => pi/180
= It is in math-module

 
4) hypot(x,y):-
= Gives Hypothesis value of Rt.angled triangle
i.e sqrt(x*x + y*y)
= It is in math-module

5) degrees(x):-
= Converts x radians to degrees
= It is in math-module

6) radians(x):-
= Converts x degrees to radians
= It is in math-module

==> Mathematical Constants:-
1) pi
2) e
= Both are in math-module
Ex:-
print(math.pi);
print(math.e);
"""

##Program (TrigonometricFuncs.py)
##(Program to demo Trigonometric-Functions)

##Program TrigonometricFuncs.py
#Program to demo Trigonometric-Functions)


#sin()
import math;
print(math.sin(30*math.pi/180));
print(math.sin(0*math.pi/180));
print(math.sin(90*math.pi/180));
'''

'''
#cos()
import math;
print(math.cos(60*math.pi/180));
print(math.cos(0*math.pi/180));
print(math.cos(180*math.pi/180));
'''


'''
##tan()
import math;
print(math.tan(0*math.pi/180));
print(math.tan(90*math.pi/180));
print(math.tan(45*math.pi/180));
'''

'''
#hypot()
import math;
print(math.hypot(2,2));
print(math.hypot(2,3));
'''

'''
#degrees()
import math;
print(math.degrees(0));
print(math.degrees(math.pi));
print(math.degrees(math.pi/2));
print(math.degrees(math.pi/4));
'''

'''
##radians()
import math;
print(math.radians(0));
print(math.radians(180));
print(math.radians(90));
print(math.radians(45));


#math-variables
import math;
print(math.pi);
print(math.e);
print(math.inf)



"""
-------------------------------------------------
==> Random Number Functions:-
= they are available in random-module (import random)
= they are used to generate Random-Numbers


##Program (RandomFuncs.py)
(Program to work with Random-Functions)


1) choice(sequence):-
= It gives random number/item from list,tuple,string
= It is in random-module
(import random;)


2) randrange(start,stop,step):-
= It gives random value for given range of values
= It is in random-module
= Here stop value is not-included in range
= step-value generates range of values

3) random():-
= It generates a random float number b/w 0 to 1
= It is in random-module

4) seed(x):-
= It sets the starting integer value before generating any random number using random() function

5) shuffle(list):-
= It will shuffle the values in a list
= it is in random-module
= It shuffles the values randomly

6) uniform(x,y):-
= It gives a random float-value b/w x and y
= It is in random-module
= last value is not-included(y)
"""
##Program RandomFuncs.py
#Program to work with Random-Functions


#choice() (works only on index-coll)
import random;
list1 = [11,22,33,44,55];
print(random.choice(list1));
s1 = "SaiRamKumar";
print(random.choice(s1));
tup1 = (10,20,30,40,50);
print(random.choice(tup1));
#set1 = {1,2,3,4,5};
#print(random.choice(set1));	#set does not have indexes
'''

'''
##randrange(start,end,step)
import random;
print(random.randrange(10,100,2));
print(random.randrange(3,100,3));
print(random.randrange(-20,-1));
#print(random.randrange(-1,-100));  #Empty-range
'''

'''
#random() #0 to 1(not-included)
import random;
print(random.random());
print(random.random());
'''

'''
#shuffle()
import random;
list1 = [10, 20, 30, 40,50];
random.shuffle(list1)
print(list1);
random.shuffle(list1)
print(list1);



#uniform()
import random
print(random.uniform(1,5));
print(random.uniform(11,15));




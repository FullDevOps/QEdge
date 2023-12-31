#8th day 8.02-08-22
"""
===>>> Control Structures or Flow Controls in Python:-
= Control means <<Condition>>:	Ex:- (a<b)
= Structure means indented-block-of-code
Def:-
	Executing an indented-block-of-code, based on <<condition>> is known as Control-Structure
==Diagram==	
Ex:-
	<<condition>>:	(T/F)
		stmt1;
		stmt2;
		stmt3;
		.....

	
= In Python, we dont have blocks with {}
= Here we have indented-block-of-code
(single/multiple stmts with equal spaces from left)

***= Flow-control means the order in which statements are executed in program

=> CS(Flow-Controls) in python are classified into 3-types,
==Diagram==
	A) Conditional stmts (Branching-Stmts)
	(Executes stmts 0 or 1 time only)
		= if
		= multiple-if
		= if-else
		= nested-if
		= if-elif-else
	B) Iterative stmts	(Looping-Stmts/Loops)
	(Executes stmts 0 or more time only)
		= for
		= while
		= nested-loops
	C) Transfer stmts	(Jumps-Stmts)
		= break
		= continue
		= pass



***A) Conditional stmts:-
= They are also called as Branching stmts
= They execute indented-block-of-code 0 or 1 time only 

i) if statement:-
Syntax:-
	if (condition):		#colon: is mandatory but not ()
		stmt1;
		stmt2;	
		stmt3;
	.....
	
= Here if condition is True then "statements" are executed o.w not-executed for False (and comes to next-line)

"""
##Program (IfStmt1.py)
#Program to demo if-stmt


#if-stmt with single-stmt
name = input("Enter any name : ");
if name=="Sai":
	print("Hello :",name,"Good Morning");
print("Take care n Bye!!");




#with multiple-stmts
name = input("Enter any name : ");
if name=="Sai":
	print("Hello :",name,"Good Morning");
	print("Have a great day!!");
print("Take care n Bye!!");


#sp-case
#Header & Suite in single-line
#single-suite-stmts (CS/FS in single-line)
a = int(input("Enter any +ve integer :: "));
if (a>0): print("Given Number is +ve Number");
print("Take care n Bye!!");


"""
ii) Multiple-if Statements::-
= Here we use, multiple-if Statements one after the another
Ex:-
	if <<condition1>>:
		stmts;
		stmts;
	if <<condition2>>:
		stmts;
		stmts;
	if <<condition3>>:
		stmts;
		stmts;	
	next-stmt;
	......
	......	
= Here, whichever condition is True, its indented-statements are executed & comes to next-stmt o.w smts not-executed for False		

"""
#Program (MultipleifStmt1.py)
#Program to demo Multiple-if stmts with +ve,-ve,0


num = int(input("Enter any integer-value :: "));
if num>0:
    print("Given Num is +ve");
if (num<0):
    print("Given Num is -ve");
if (num==0):
    print("Given Num is ZERO");

print("End of the Program");

"""
"Assignments"
#Program (MultipleifStmt2.py)
#(Program to demo Multiple-if stmts with Even,Odd,Neither of them)
Hint:-
	Even (num%2==0)
	Odd (num%2!==0)
	Neither Even Nor Odd (num==0)




iii) if-else statement:-
(Here we have 2nd option also)
Syntax:-
if condition:
	True-Stmts;
	.....
else:					#here : is mandatory
	False-Stmts;
	.....
.....
next-stmt
.....
	
=*** Here if condition is true then True-Stmts are executed,
if condition is False then False-Stmts are executed
(and comes to next-stmt)
"""

##Program (IfElseStmt1.py)
#Program to demo if-else stmt


#single-stmt
name = input("Enter any name : ");
if name=="Sai":
	print("Hello :",name);
else:
	print("Hello : New User!!");
	
print("End of Program!!");
'''

'''
#multi-stmts
name = input("Enter any name : ");
if name=="Sai":
	print("Hello :",name);
	print("Have a nice day!!");
else:
	print("Hello : New User!!");
	print("Register your Name...");

print("Take care n Bye!!");


#sp-case
#single-suite-stmt (Header & Suite in single-line)
num = int(input("Enter any Integer-Number : "));
if num==0: print("Given Number is 0");
else: print("Given Number is NON-Zero(+ve/-ve)");



# "Assignment"
#WAP to accept age of a person as input & display "Eligible for Voting or not"
##Program(IfElseStmt2.py)
#Program to demo if-else stmt (IfElseStmt1.py)


age = int(input("Enter your Age : "));
if (age>=18):
	print("Your are Eligible for Voting");
else:
	print("You are NOT-Eligible for Voting");
	
print("End of Program..!!");


"""
"Assignment"
#WAP to check for for eligibility for marraige
(maleage>=21 and femaleage>=21) [T and T  ---> T]
#WAP to accept age of candidate & print eligibility for employement
(personage >= 15 and personage <= 65) [T and T  ---> T]



iv)
=> Special-Case:-
==> Nested if's:-
= We can use "if-stmt" inside another if-stmt or another else-stmt as follows,
Ex:-
if condition:(T)
	stmts;
	if condition:(T)
		stmts;
		.....
else:
	stmts;
	if condition:
		stmts;
		.....
		
=** here if both conditions are True then its idented stmts are executed o.w else with if-stmts are executed

"""	
##Program (NestedIf1.py)
#Program to check biggest of 3 numbers using nested-if)

print("Enter 3-diff values :");
a=int(input("Enter A value :: "));
b=int(input("Enter B value :: "));
c=int(input("Enter C value :: "));

if (a>b):
    if (a>c):
        print("A is Biggest");
    else:
        print("C is Biggest");
else:
    if (b>c):
        print("B is Biggest");
    else:
        print("C is Biggest");


print("End of the Program");



"Assignments"
#WAP to print smallest of 3-diff-numbers using nested-if stmts


"Assignment"
##Program (NestedIfs2.py)
#Program to demo Nested-If statements to check given number is +ve,-ve or 0

num = int(input("Enter any int-value : "));

if (num==0):
	print("Given Number is Zero");
else:
	if (num>0):
		print("Given Number is +VE");
	else:
		print("Given Number is -VE");
print("End of the Program");


#"Assignment"(nested-if)
##Program (NestedIfs3.py)
#WAP to display given number is even, odd or neither using nested-if

"""
**V) if-elif-else:-
Syntax:-
if condition1:
	stmts;
elif condtion2:
	stmts;
elif condtion3:
	stmts;
....
....
else:
	stmts;
next-stmt;(comes-out-of-CS)
......
= Here linearly one after the other conditions are checked
= Whichever condition is true, corresponding stmts are executed and remaining conditions are skipped till end
= If no-condition is true then last else part is executed
"""
##Program (IfElifElse.py)
#Program to accept 5 subject marks of a student and print the grade Distinction,1st-class,2nd-class,3rd-class or Fail
#Program to demo If-elif-else

print("Enter 5 Subject Marks :");
s1 = int(input("Sub1 : "));
s2 = int(input("Sub2 : "));
s3 = int(input("Sub3 : "));
s4 = int(input("Sub4 : "));
s5 = int(input("Sub5 : "));

total=s1+s2+s3+s4+s5;
avg = (total)/5;

print("Total-Marks : ",total);
print("Average-Marks : ",avg);

if (avg>=75):
	print("Distinction");
elif (avg>=65):
	print("1st-Class");
elif (avg>=50):
	print("2nd-Class");
elif (avg>=35):
	print("3rd-Class");
else:
	print("Failed");
	
print("End of Program");


#"Assignment"(if-elif-else)
#WAP to accept age of person and print following msgs
# (Baby, Kid, Teenage, Adult, Oldage)
"""
if personage >=65
elif personage>=18
elif personage>=12
elif personage>=5
else "Baby"
"""
#Assignment (if-elif-else)
#WAP to display given num is +ve, -ve, 0 (if-elif-else)
#WAP to display given num is even, odd, neither(if-elif-else)

"""
NOTE:-
= if-elif-else stmt is very efficient & fast when compared to multiple-if-stmts (or) nested-if-stmts becasuse here other-conditions are not-checked un-necessarily
"""
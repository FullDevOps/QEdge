# 9th day 9.03-08-22

"""
***B) Iterative Statements:- (Looping-stmts)
= They are used to execute group-of-statements(indented block-of-code) 0 or more times based on condition/values
= We have 2-types of Iterative-Stmts,
	i) for loop
	ii) while loop
(do-while or foreach-loop are not in python)


i) for loop:-
= This loop is based on collection-of-values
Ex:-
Strings, List, Tuple, Set, Dictionary, Arrays, Range etc

Syntax:-
for x in collection-of-values:  [11,22,33]
	stmts;
	.....
	
= Here group-of-stmts are executed for each-value in collection
(each time coll-value is assigned to loop-var(x))
"""
##Program ForLoopEx1.py)
# (Program to deme Python For Loop)
##Program (ForLoopEx1.py)
#Program to demo for-loop


#using str
s1 = "Hello";		#coll.of.chars
for x in s1:
	print(x);
print("End of For Loop")
'''

'''
#using str with indexes
s1 = "Hello";       #Hello(0,1,2,3,4)
i=0;
for x in s1:
	print("index",i,"char is",x);
	i=i+1;
print("End of For Loop")
'''

'''
#range()
for x in range(10):     #0 to 9
	print("Sai");
    
print()
for x in range(10):     #0 to 9
	print(x+1);
'''

'''
#sum of N-natural no's	
sum=0;
for x in range(1,11):   #1 to 10    
	sum=sum+x;
print("Sum :",sum);	
'''

'''
#for loop single suite stmt (header & suite in single-line)
for x in range(1,11): print(x*x);
print()
for x in range(1,11): print(x*x*x);


#using list-coll
for x in [11,22,33,44,55]:
    print(x)

"""
NOTE:-
= For is purely based on coll.of.values


**Sp-case**
==>> for-loop with else-block:-
= In python, we can have else-block with for-loop
= else-block stmt is executed when for-loop values are finished (only 1-time in last)
Ex:-
	for x in coll:
		....
	else:
		....
"""
##Program (ForLoopElseEx1.py)
#Program to demo for-loop with else-block

vals = [11,22,33,44,55];
for x in vals:
	print(x);
else:				#else is executed only 1-time
	print("End of the Vals");

print("End of For Loop");


"""
**ii) while loop:-
= This loop-stmts is executed based on a condition (till it is false)
(here we use loop-var initial-value, condition-check, incre/decre)
Syntax:-
	inital-value;
	while condition(T/F):
		stmts;
		stmts;
		.....
		incre/decre;
"""

##Program (WhileLoopEx1.py)	
#Program to print N-Natural numbers using while-loop

i=1;
while i<=10:
	print(i);
	i=i+1;
print("End of While Loop");
'''

'''
#Printing SUM of N-Natural Numbers
sum=0;
n = int(input("Enter any num : "));
i=1;
while i<=n:
	sum=sum+i;
	i=i+1;
print("Sum : ",sum);
print("Sum of :",n,"Natural numbers is :",sum);


#while loop single suite stmt
n = int(input("Enter N-value :: "))
i=1;
while i<=n: print(i*i); i+=1;
print()
i=1;
while i<=n: print(i*i*i); i+=1;


"""
**Sp-case**
**==> Infinite While-Loop:-
= A loop which is always true is called Infinite Loop
Ex:-
	while True:
		...
		...
		...
"""
##Program (InfiniteLoop.py)
#(Program to demo Infinite-Loop while)

i=1
while True:
    print(i)
    i=i+1;
    
print("End of While Loop"); 
'''	
NOTE:-
= (Ctrl+c) is used to come out of infinite loop
(ctrl+Pause-break-key)


**sp-case**
==> else-block with while-loop:-
= In python, we can have else-block with while-loop 
= else stmt is executed when condition in while-loop is False
(only 1-time in last)
Ex:-
	while <<cond>>:
		...
	else:
		...
'''
##Program (WhileLoopElseEx1.py)
#Program to demo while-loop with else-block

i=1;
while i<=10:
	print(i);
	i=i+1;
else:		#here else-block is executed only once
	print("End of Natural-Nums");

print("\nEnd of While Loop")


# **sp-case**
# ==> Nested Loops:-
# = Using a particular loop inside another loop is called Nested-Loop
# (loop with-in loop)
# Ex:-
for i in range(3):		#outerloop(i=0,1,2) ---> rows
	for j in range(3):	#innerlloop(j=0,1,2) ---> cols
		print(i,",",j,end="\t");
	print();
	

"""
NOTE:-
= Nested-Loops are mainly used to represent data in the form of rows and columns, table-data, matrices data etc
=** Here outer-loop represents no.of rows and inner-loop represents no.of columns
"""
##Program (NestedLoopEx1.py)
#Program to demo Nested-Loops

for i in range(3):			#outer-loop(0,1,2) => rows(i)
	for j in range(3):		#inner-loop(0,1,2) => cols(j)
		print(i,",",j,sep="",end="\t");
	print();
	
print("End of Program")


"""
***C) (Transfer Stmts) in Control Statements:- 
(Jump Stmts)
(jumping from one-line of program to another-line)
a) break
b) continue
c) pass


A) break:- 
(mainly used in loops(for/while))
= It is used to come out of looping-stmts using some condition
(Termination/Exit of Loop)

Syntax:-
loop:
	if cond:
		break;

=** it skips remaining stmts & also remaining iterations(cycle)
"""
##Program (BreakStmt.py)
##Program to demo break-stmt in Loops)


#using while loop
i=1
while i<=100:
    if i>=50:
        break;
    print(i)        #odd-nums
    i=i+2;
'''

'''    
#using infinite while loop
i=2
while True:
    if i==102:
        break;
    print(i)        #even-nums
    i=i+2;


#using for-loop
for x in range(0,1001,3):
    if x>500:
        break;
    print(x)

"""
NOTE:-
= The best-way to come out of Infinite-Loop is with break-stmt(using cond..)


b) continue stmt:- 
(mainly used in loops(for/while))
= It is used to skip current-iteration-stmts and continue with next-iteration(cycle)
Ex:-
	loop:
		...
		if cond:
			continue;
		....
"""
##Program (ContinueStmt.py)
##Program to demo continue-stmt in Loops

''
#using while-loop
i=1
while(i<=100):
    if i%2==0:  #even
        print(i)
    else:
        i=i+1;
        continue;
    i=i+1


#using for loop
for x in range(1,101,1):
    if x%2!=0:  #odd
        print(x)
    else:
        continue;

"""
c) pass statement:-
= It is used in program when some indented-block-of-code is not required for header-stmt
= pass takes control of execution to next-stmt in program
=** pass is like empty-stmts

Ex:-
	if (True): 
		pass;
Ex:-
	def m1(): 
		pass; 
	class A: 
		pass;
"""
##Program PassStmt.py
#Program to demo pass-stmt in program with Loops

#inside loops
for x in range(1,101):
    if x%3!=0:
        pass;
    else:
        print(x)

print()
i=1;
while i<=100:
    if i%5!=0:
        pass;
    else:
        print(i)
    i=i+1








# 16th day 16.11-08-22

"""
==> Parameters to Function:-
(Function with Paramters)
(Function with Paramters)
= Parameters means input-values given to a function
= Such input-values are passed to function while calling a function

Ex:- (FunctionEx1.py)
(Program to define a function with params and call it)
def f2(uname):
	print("Hello User :",uname+", Welcome to Python...");
f2("Sai");
f2("Ram");
f2("Ali");
"""	
# //Program (FunctionEx1.py)
# (Program to define a function with param as number and print is square)
def f3(num):
	print("Square of given :",num," is :",num*num);

f3(4);
f3(5);
f3(6);

#Program (FunctionEx1.py)
#(Program to define a function and call it)


#func with no-args(input) & no-return-value
def f1():
	# ''''''f1() def''''''
	print("Hello User");
	print("Welcome to Python");
	print("All the best");

#use or call the function (any no.of.times) re-usability  
f1();  
print()
f1();
print()
f1()
print()
for i in range(10):
    f1();
'''

'''
#func with input-para(args)
def f2(uname):		#uname='Sai'....
	# ''''''f2() func def.''''''
	print("Hello User :",uname);
	print("Welcome to Python...");
	
f2("Sai");		#based on input-value output also changes
f2("Ram");
f2("Ali");


#func with input-para
def f3(num):	#num=4,5,6
	#'''f2() func def'''
	print("Square of given :",num," is :",num*num);
	
f3(4);	#input-values can be used inside func-body
f3(5);
f3(6);

"""
-------------------------------------------------------
==> return statement in Functions:-
(Func with return-stmt)
= Function takes input-values, executes-the-logic and can provide return value/statement
Ex:-
	return sum;

##Program (FunctionEx2.py)
##(Program to define a function with return value)
= Accept 2 nums and return its sum-value

NOTE:-
= To call a function, we can pass values or variables
= We can call function in another function as parameter (return value of 1-function is input-para to another function)

Ex:- (without return stmt)
def f1():
	print("Hello User");
f1();
print(f1());

=** Here since f1() does not have return-value, it prints "None" in 2nd case	
	

//Program (FunctionEx2.py)
(Program to check given num is Even or Odd)


==> return multiple-values:-
= This is special-feature(added) in Python-Functions, not available in C,C++,Java,.net languages

//Program (FunctionEx2.py)
(Program to return multiple-values in func)

//Program (FunctionEx2.py)
(Program to return multiple-values in func using arithmetic-oper)
"""
##Program (FunctionEx2.py)
#Program to define a function with return value
##Program (FunctionEx2.py)
##(Program to define a function with return value)


#Accept 2 nums as input and return its sum-value
def sum(a,b):	#a=11,b=22
	# ''''''sum() func def''''''
	c=a+b
	return c;

#case1	
x=11;
y=22;	
result = sum(x,y); ##c=33
print("SUM1 :",result);
result = sum(111,222);
print("SUM2 :",result);
print("SUM3 :",sum(1111,2222));	#sp-case
#using or calling a func inside print() as para
'''

'''
#Without return-stmt
#func by default returns None
def f1():				#no-input-para
	print("Hello User");
	#no-return-value
f1();
print()
print(f1());	#prints None
print("End of Program");


#sp-case
#func with multiple-return-values(tuple)
#Multiple-return values(Arithmetic-Opertions)
def calci(a,b):
	sum=a+b;
	sub=a-b;
	prod=a*b;
	div=a/b;
	mod=a%b;
	return (sum,sub,prod,div,mod);
tup1 = calci(11,3);
print(tup1)
print(type(tup1))
#use loop
print("Result :");
for x in tup1:
	print(x);

"""
---------------------------------------------------------------------------------------------------------------------------------------------------------
==> Types of Function-Arguments:- (paramters) i/p-values
Ex:-
def f1(a,b):	#a,b -> Formal-Args/Para/input-values
	...
	stmts;
	...
f1(x,y);	#x,y -> Actual-Args/Para/input-values

= Here x,y are Actual-Args and a,b are Formal-Args

= Pythons supports 4-types of Actual-Args, they are:-
1) Positional Args
2) Keyword Args
3) Default Args
4) Variable-Length Args


1) Positional Args:-
= Arguments passed to a function in proper-order or particular-order is called as Positional-Args
Ex:-
def sub(a,b):
	print(a-b);
x=11;
y=22;	
sub(x,y);
sub(y,x);

= Here order/position/number of args will give appropriate result

##Program (FunctionEx3.py)
(Program to demo Types of Func-Args)

2) Keyword-Arguments:-
= We can pass args using keyword i.e, paramter name (formal-args)
Ex:-
def f1(uname,msg):
	print("Hello :",uname,msg);
f1(uname="Sai",msg="Thank You!!");
f1(msg="All the Best",uname="Ram");

=** Here we pass actual-args using formal-args name & value in any order separated with ,(comma)

//Program (FunctionEx3.py)
(Program to demo Types of Func-Args)

Ex:- (both positional and keyword args)
= Here 1st positional-args and then followed by keyword-args is mandatory
def f1(uname,msg):
	print("Hello :",uname,msg);
f1("Sai","Thank You!!");		#Valid
f1("Ram",msg="Thank You!!");	#Valid
f1(name="Ram","All the Best");	#InValid (SyntaxError)



3) Default-Arguments:-
= We can have default values to formal-args
= Such values are used when we do not pass actual-args
= It is used for positional-args
Ex:-
def sum(a=11,b=3):
	print("SUM :",(a+b));
sum(10,20);
sum();

//Program (FunctionEx3.py)
(Program to demo Types of Func-Args)

NOTE:-
= After default-args, we should not take non-default args in func-definition
Ex:-
def sum(a=11,b=3):	#Valid
def sum(a=11,b):	#In-Valid (SyntaxError)
def sum(a,b=3):		#Valid



4) Variable-Length Arguments:-
= We can pass any no.of args to call a function
i.e, 0 or 1 or more actual-args to call a function
**= Such functions formal-args are declared using * symbol
Ex:-
def f1(*num):
	total=0;
	for x in num:
		total=total+x;
	print("SUM :",total);
f1();
f1(11);
f1(11,22);
f1(11,22,33);
= Such values are represented as Tuple internally

//Program (FunctionEx3.py)
(Program to demo Types of Func-Args)


**NOTE:-
= We can declare Keyword Variable-Length-Args as follows,
= For this we use ** symbol
Ex:-
def f1(**nums):
= To call such function, we pass any no.of keyword-args
= Internally it is treated as Dictionary (K,V)
Ex:-
def f1(**nums):
	for k,v in nums.items():
		print(k,"=",v);
f1(a=10,b=20,c=30);
f1(rollno=1001,name="Sai",course="CSE");
"""

##Program (FunctionEx3.py)
#Program to demo Types of Func-Args
##Program (FunctionEx3.py)
#(Program to demo Types of Func-Args)


#Positional Args (position of input-values)
def sub(a,b):
	print(a-b);
x=11;
y=22;	
sub(x,y);	#-11
sub(y,x);	#11	#based on postion of args output also changes 
sub(x,x);	#0
sub(y,y);	#0
'''

'''
#Keyword-Arguments (input-para-names is used to pass args)
#here input-para-names are keyword-names
def f1(uname,msg):
	print("Hello :",uname,msg);
f1(uname="Sai",msg="Thank You!!");
f1(msg="All the Best",uname="Ram");
#here we can change order of input-para-names(keyword-names)
'''

'''
#Default-Arguments
#default-values to input-para
def sum(a=1,b=2,c=3):	#here a,b,c have default values
	print("SUM :",(a+b+c));
	
sum(10,20,30);
sum(10,20); 	#c(3rd-para) is missing
sum(10)		#b,c(2nd,3rd-para) is missing
sum();		#a,b,c(1st,2nd,3rd all are missing)
'''

'''
#Variable-Length Arguments
#sp-arg given with *varname(tuple)
def f1(*num):	#here *num(tuple) can accept 0/1/more values
	print(num,type(num))
	print("SUM :",sum(num));	
	
f1(11,22,33);	#3-values(or more)
f1(11,22);
f1(11);
f1();
#list1 = [11,22,33,44,55];	#TypeError
#f1(list1);


#sp-case for var-len-args
#Keywords with Variable-Length-Args (**varname) dict{}
def f1(**nums):
	print(nums)
	print(type(nums))
	print();
	
f1(a=10,b=20,c=30,d=40); #keyword-args(our-own)
f1(rollno=1001,name="Sai",course="CSE");

"""
---------------------------------------------------------------
**==> Functions Types of Variables:-
= Python supports 2 types of variables wrt functions
1) Global variables
2) Local variables

1) Global variables:-
= Variables declared outside a function
= They are accessible in all functions of that Module(.py file)
Ex:-
a=10;
def f1():
	print(a);
def f2():
	print(a);

f1();
f2();
"""
##Program (FunctionEx4.py)
##(Program to work with Function Variables)
#Program to work with Function Variables


#Global-Variables (def directly in prog outside func)
a=10;	#global-var-a
def f1():
	print(a);	#using inside f1()
def f2():
	print(a);	#using inside f2()
f1();
f2();
'''

'''
#Local-Variables (Def. inside particluar func
def f1():
	a=11;		#local-var-a (local-access)
	print(a);
	#print(b)
def f2():
	b=22		#local-var-b (local-access)
	print(b);
	print(a)
	

f1();
f2();	
#print(a,b)		#NameError
'''


'''
#Both Global & Local-vars with same name
a=100;	#global-var-a(100)
def f1():
	a=11;	#local-var-a(11) 1st preference to local-var
	print(a);
def f2():
	print(a); #It takes Global-Var reference

f1();
f2();
'''

'''
#global-Keyword (Local-var and Global-Var with same-name)
#global-Keyword inside a func for modifications
a=100;
def f1():
	global a;
	a=1000;		#It takes Global-Var reference
	print(a);
def f2():
	print(a); 	#It takes Global-Var reference

#case1
#f1();
#f2();

#case2
f2();
f1();
f2()



#globals() -> gives all global-vars as dict{}
#Global-Var & Local-var with same-name and access both at a time
a=100;	#global-vars
b=200
c=300
def f1():
	a=10;	#local-vars with same-name as global-vars
	b=20	
	c=30
	print(a,b,c);
	dict1 = globals()
	print(dict1["a"],dict1["b"],dict1["c"]);
	
f1();


"""
2) Local-Variables:-
= They are declared inside the body of a function
(indented block-of-code)
= They are accessible only inside that function-body itself but not outside the function
Ex:-
def f1():
	a=11;
	print(a);
#def f2():
#	print(a);

f1();
#f2();

# //Program (FunctionEx4.py)
# (Program to work with Function Variables)

# Ex:- (Both Global & Local-vars with same name)
a=100;
def f1():
	a=11;
	print(a);
def f2():
	print(a); 	#It takes Global-Var reference

f1();
f2();


==> Global-Keyword:-
= It is used in 2-ways
1) To declare global-var inside a function
2) To make global-var available to a function for modification 
(provided local-var also have same-name)

Ex:- (Local-var and Global-Var with same-name)
a=100;
def f1():
	a=11;
	print(a);
def f2():
	print(a); 	#It takes Global-Var reference

f1();
f2();

//Program (FunctionEx4.py)
(Program to work with Function Variables)

Ex:- (with global-keyword & modifications)
"""
a=100;
def f1():
	a=11;
	print(a);
	# global a;
	a=1000;		#It takes Global-Var reference
def f2():
	print(a); 	#It takes Global-Var reference

f1();
f2();

# Ex:- (global-Keyword inside func for global-var-declaration)
def f1():
	global a;
	a=100;		#It takes Global-Var reference
	print(a);
def f2():
	print(a); 	#It takes Global-Var reference

f1();
f2();


# Ex:- (Global-Var & Local-var with same-name and access both at a time)
a=100;
def f1():
	a=10;		
	print(a);
	print(globals()['a']);
f1();

# =** globals() is used here to access global-var inside a function with same name along with local-var


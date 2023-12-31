# 15th day 15.10-08-22


"""
===> Dictionary Collectioion (or) Data-Structure in Python:-
= List, Tuple, Set, FrozenSet collections have single-single values
= However, in Dict-coll, we have group of (Key,Value) pairs
Ex:-
	"rollno":1001		Key:Value
	"name":"Sai"
	"height":6.0
	etc...
	"addr":"Hyd"
	"phno":9988776655
	
=> Dict-Imp-Points:-
(Refer-notes)
	= Keys are unique, cannot be duplicate (Unique)
	= Values can be duplicated
	= Allows Homo/Heterogeneous (Keys,Values) objs (same-data or diff-data)
	= Order is not Preserved
	= Dictionary is Mutable-coll (Org-data is Modifiable)
	= NO-Indexes and Slicing is Not applicable


##Program (DictionaryEx1.py)
(Program to work with Dictionary DS)

==> How to create Dictionary?
= To represent dictionary DS we use {} curly-brackets
Ex:-	{Key1:Value1, Key2:Value2, Key3:Value3,.......}

Ex:- (Empty-Dictionary)
dict1={};
dict2=dict();

Ex:- (Adding Entries)
Syntax:-
	dict1[Key]=Value;
	
dict1[1001]="Sai";
dict1[1002]="Ram";
dict1[1003]="Ali";
print(dict1);

//Program (DictionaryEx1.py)
(Program to work with Dictionary DS)

Ex:- (Dictionary with K,V pairs)
Syn:-
	dict1 = {K:V, K:V, K:V,....};
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};

Ex:- (Accessing-Data)
Syn:-
	dict1[key] ---> we get corresponding value
dict1[1001]	
dict1[1002]
dict1[1003]	
#print(dict1[1004]);		#KeyError

= If specified Key is not-found then we get "KeyError"

Ex:- (has_key())
= It checks whether Key is there or not in Dictionary
= It gives 1(Found) o.w 0(Not-Found)
= It is in Python-2 but not in Python-3
= Alternate is "in" operator
if 1004 in dict1:
	print(dict[1004]);
else
	print("Key Not Found");
"""

##Program (DictionaryEx1.py)
#Program to work with Dictionary DS & its Operations


#Empty-Dictionary
dict1={};       #Empty {} curly brackets
print(dict1);
print(type(dict1));
dict2=dict();   #Empty dict() func
print(dict2);
print(type(dict2));
'''

'''
#Adding Entries	dict1[key]=value; (use [] key-oper)
dict1 = {}
dict1[1001]="Sai";
dict1[1002]="Ram";
dict1[1003]="Ali";
print(dict1);
print()
dict2 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict2);
'''

'''
#Accessing-Dict-Data(using [] key-oper)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1[1001]);
print(dict1[1002]);
print(dict1[1003]);
#print(dict1[1004]);		#KeyError


#dict with membership-oper(in, not in)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
#if 1004 in dict1:
if 1002 in dict1:
	print(dict1[1002]);
else:
	print("Key(1004) Not Found");

#dict with loops
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali",1004:"John"};
for key in dict1:     #assigns only keys
    print(dict1[key])
    
"""
NOTE:-
= The best-way to access dict-data is with loops is the best-way
Ex:-
for var in dict1:	--->each-key is assigned to loop-var
	dict1[var]---->value
##Program (DictionaryEx1.py)    
    


"Assignment"
#WAP to enter student-name(key) and Percentage-Marks(value) & insert in dict1
//Program (DictionaryEx2.py)
(Program to Enter Student-Name and Percentage-Marks for Display)

#Program to Enter Student-Name and Percentage-Marks for Display in Dict-obj
'''
records = {};	#empty-dict
n = int(input("Enter No.of Students : "));
i=1;
while i<=n:
	name=input("Enter Student Name : ");
	percentage=input("Enter Marks % : ");
	records[name]=percentage;
	i=i+1;

print("Student-Name","\t\t","% of Marks");
for x in records:	#here dict-key is assigned to x
	print("\t",x,"\t\t",records[x]);
	
print(records);
'''




"Operations on dict-coll"
==> Dictionary Updates:-
(Updating data in a dictionary)

##Program (DictionaryEx3.py)
(Program to work with Dictionary DS)

Ex:-
	dict1[Key]=Value or new-value;
= If Key is not-available then New-Entry is Added
= If Key is available then Old-Value is replaced by New-Value
Ex:-
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
dict1[1004]="Tom";		#add-new K:V
print(dict1);
dict1[1001]="Baba";		#replace
print(dict1);

//Program (DictionaryEx3.py)
(Program to work with Dictionary DS)

=> Deleting Elements:-
= del keyword is used here

1)del dict1[Key]
= It deletes corresponding (K,V) pair o.w "KeyError"(Not-Found)
Ex:-
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
del dict1[1003];
print(dict1);
del dict1[1003];

2)dict1.clear()
= Removes all entries from dictionary
Ex:-
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
dict1.clear();
print(dict1);
dict1.clear();	#No-Error

3)del dict1
= deletes total dictionary object including its reference
Ex:-
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
del dict1;
print(dict1);	#NameError
"""

##Program (DictionaryEx3.py)
##Program (DictionaryEx3.py)
#Program to work with Dictionary DS operations


#dict-Updates (updating existing value)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
#key[] oper
dict1[1004]="Tom";	#add new K:V if not-there
print(dict1);
dict1[1001]="Baba";	#updated/replaced "Sai" with "Baba"
print(dict1);
'''
    
'''
#Deletes (single-entry)
#del stmt (with []key-oper)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
del dict1[1003];
print(dict1);
#del dict1[1003];	#KeyError if not-there
'''

'''
#clear()
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
dict1.clear();
print(dict1);       #empty-dict
dict1.clear();	    #No-Error
'''

'''
#delete complete dict (del stmt)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
del dict1;
#print(dict1);	#NameError(dict-obj-ref is deleted from memory)
'''

'''
#Dictionary-Functions
#dict() conversion-func
dict1 = dict();
print(dict1);
dict2 = dict({1001:"Sai",1002:"Ram",1003:"Ali"});
print(dict2);
dict3 = dict([(1001,"Sai"),(1002,"Ram"),(1003,"Ali")]);	#list(k,v)->dict (list of tuples(k,v)) [(k,v),(k,v),(k,v)]
print(dict3);
'''

'''
#len()
dict1 = dict();
dict2 = dict({1001:"Sai",1002:"Ram"});
dict3 = dict([(1001,"Sai"),(1002,"Ram"),(1003,"Ali")]);
print(len(dict1));
print(len(dict2));
print(len(dict3));
'''


'''
#using get() we get values w.o KeyError
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1.get(1001));
print(dict1.get(1002));
print(dict1.get(1003));
print(dict1.get(1004));	#None but no-error
print(dict1.get(1004,"NOT-THERE"));
'''
'''
#using [] subscript-operator
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1[1001]);		
print(dict1[1002]);		
print(dict1[1004]);		#KeyError
'''

'''
#pop() -> deletes given key-value pair
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
print(dict1.pop(1001));
print(dict1.pop(1003));
print(dict1);
print(dict1.pop(1001));		#KeyError
'''

'''
#popitem() -> dels random key-value pair
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
print(dict1.popitem());
print(dict1);
print(dict1.popitem());
print(dict1);
print(dict1.popitem());
print(dict1);
print(dict1.popitem());		#KeyError (Empty-Dictionary)
'''

'''
#keys() -> we get list of keys[]
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1.keys());
for k in dict1.keys():
	print(k);
'''

'''
#values() -> we get list of values[]
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1.values());
for v in dict1.values():
	print(v);
'''

'''
#(***)
#items() -> we get list-of-key,value pairs as ()tuples
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1.items());
#**for loop with 2-vars(k,v)
for k,v in dict1.items():
	print(k,"--->",v);
'''

'''
#copy() cloning(dup-dict-coll, sep-coll with sep-addr)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
dict2 = dict1.copy();
print(dict1,id(dict1));
print(dict2,id(dict2));
'''

'''
#setdefault()->adds new (k,v) o.w gives existing value
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
print(dict1.setdefault(1004,"Tom"));	#adds to dict
print(dict1);
print(dict1.setdefault(1004,"Tommy"));	#gives the value
print(dict1);


#update() #if entry is not-there then it will add o.w update
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
dict1.update({1004:"Tom"}); #not-there it adds
print(dict1);
dict1.update({1004:"Tommy",1005:"Sai"}); #1004(updated)
print(dict1);       #1005 is newly-added




"""
==> Functions in Dictionary DS:-
1) dict()
= It creates a Empty-Dictionary/Dictionary with Values also
Ex:-
dict1 = dict();		#Creates Empty-Dictionary
dict2 = dict({1001:"Sai",1002:"Ram",1003:"Ali"});
				#Creates Dictionary with Specified-Elements
dict3 = dict([(1001,"Sai"),(1002,"Ram"),(1003,"Ali")]);					
		#Creates Dictionary with Specified-Tuple-Values

2) len():-
= Gives length of dictionary
Ex:-
len(dict1);

3) clear():-
= Removes all elements in dictionary (empty)
Ex:-
dict1.clear();

4) get(key):-
= Gives value for particular key o.w None(Not-Found)
Ex:-
dict1.get(1001);

=>get(key,defaultValue):-
= Gives value for particular key o.w defaultValue(Not-Found)
Ex:-
dict1.get(1004,"NOT-THERE");

Ex:- (Other)
print(dict1[1001]);
#print(dict1[1004]);		#KeyError
print(dict1.get(1001));
print(dict1.get(1004));		#None
print(dict1.get(1001,"NOT-THERE"));
print(dict1.get(1004,"NOT-THERE"));		


5) pop():-
Ex:-
dict1.pop(Key);
= It removes corresponding (K,V) pair and returns its value o.w "KeyError"

dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1.pop(1001));
print(dict1);
print(dict1.pop(1001));

6) popitem():-
= Removes any random (K,V) pair from dictionary and returns it
Ex:-
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1.popitem());
print(dict1);
print(dict1.popitem());
print(dict1);
print(dict1.popitem());
print(dict1);
print(dict1.popitem());		#KeyError (Empty-Dictionary)


==> Other functions:-
7) keys():-
= Returns all keys at a time
Ex:-
dict1.keys()

8) values():-
= Returns all values at a time
Ex:-
dict1.values()

9) items():-
= It returns list-of-tuples representing (K,V) pairs
Ex:-	[(k,v), (k,v), (k,v)]
print(dict1.items());

10) copy()
= Creates a duplicate copy(cloned copy)
Ex:-
dict2 = dict1.copy();

11) setdefault()
Ex:-
	dict1.setdefault(k,v);
= If key is already there then it returns corresponding value
= If key is not there then new (K,V) entry is added to dictionary
print(dict1.setdefault(1004,"Tom"));

12) update():- 
Ex:-
dict1.update(x);	#x is {k:v,k:v,....}
= x will be updated in dictionary o.w new-entry is added
"""

"Assignment"
##Program (DictionaryEx4.py)
#Program to accept Dictionary vals(nums) and print its SUM
# Input: {"sub1":100,"sub2":92,"sub3":65,"sub4":75,"sub5":68}

##Program to accept Dictionary values(K:V) and print its SUM

dict1 = eval(input("Enter Dictionary :"));
sum1 = sum(dict1.values());
print("SUM :",sum1);


'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
==> Functions in Python:-
= A Function is indented-block-of-code, which is used to perform specific-task in a program (task/work)
= Advantage is write-once & call or use any no.of times (Code-Reusability)


= Basically, Functions are divided into 2-types,
	a) Built-in Functions
	b) User-defined Functions
	==Diagram==

1) Built-in Functions:-
= They are available in Python-Library-Modules
(Modules means .py python-files only)
Ex:-
	id()
	type()
	input()
	eval()
	etc...

2) User-defined Functions:-
= These functions are developed by programmer/developer as per user-requirements in program

Syntax:-(***)	[def is the keyword]
-----------------------------------------------
	def function_name(parameters,....): #input-values/args
		"""doc-string/comment"""
		....
		stmts;	#(Body/Indented-block-of-code)
		....
		return value;
------------------------------------------------
(5-things in function::)
function_name/parameters/comments/body/return-value
-------------------------------------------------

NOTE:-
= def, return are 2-keywords used in function definition
= function-body is intended-block-of-stmts in multiple-lines till return value
'''
# Ex:- 
#Program (FunctionEx1.py)
#(Program to define a function and call it)

#func with no-args(input) & no-return-value
def f1():
	"""f1() def"""
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


# NOTE:-
# = After def. function, use or call the function
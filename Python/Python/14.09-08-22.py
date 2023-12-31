# 14thday 14.09-08-22

"""
==>> Tuple Collection (or) Data-Structure in Python:-
= Tuple is exactly same as List DS but it is Immutable
= Once Tuple is created we cannot perform any changes or modifications(insert/update/del) to its values

=> Tuple-Tech-Points:-
	= Tuple is coll of objects (....)
	= Tuple is Read-only version of List
	= Here Order is Preserved
	= It allows Duplicate Objects
	= It allows same-type/different-type of Objects
	= Indexes are provided to access the objects
	= It supports both +ve (F->L) [0to(n-1)] and -ve (L->F) index [-1 to -n] (both Farward/Backward)
	= Its values are represented in () with , (commas) 
	= () are not compulsory (optional) but it is recommended

Ex:- (Creating Tuple)
tup1 = 11,22,33,44,55;		#w.o ()
tup1 = (11,22,33,44,55);	#with ()
print(tup1);
print(type(tup1));

##Program (TupleEx1.py)
(Program to work with Tuple DS)

Ex:- (Empty-Tuple)
tup1=();
print(type(tup1));

Ex:- (Single-Value-Tuple taken as int)
tup1=(10);		#Single-Value Tuple taken as int(respective-dtype)
print(tup1);
print(type(tup1));

Ex:- (Single-Value Tuple with , comma)
tup1=(10,);		#Single-Value Tuple with , comma #10,
print(tup1);
print(type(tup1));

=> Other Tuple Examples:-
(different ways of creating a tuple)
Ex:-
tup1=();
print(tup1);
print(type(tup1));

tup1=11,22,33;
print(tup1);
print(type(tup1));

tup1=10;	#int type
print(tup1);
print(type(tup1));

tup1=10,;	
print(tup1);
print(type(tup1));

tup1=(10);	#int type
print(tup1);
print(type(tup1));

tup1=(10,);
print(tup1);
print(type(tup1));

tup1=(10,20,30);
print(tup1);
print(type(tup1));

NOTE:-
= Tuple-Creations,
1) tup1=();	#Empty-Tuple
2) tup1=(11,);	#Tuple-with Single-Value
3) tup1=11,;	
4) tup1=(10,20,30); #Tuple-with Multiple-Value
5) tup1=10,20,30; #Tuple-with Multiple-Value


=> Creating Tuple with tuple():-
= here tuple() is a conversion function
= it converts other coll.of.values into tuple-type values
Ex:-
list1 = [11,22,33];
tup1 = tuple(list1);
print(tup1);

tup1 = tuple(range(0,20,2));
print(tup1);


==> Accessing Elements of a Tuple:-
= It is done with indexes or slice-operator

1) By using index:-
+ve indexes (0 to n-1) First->Last (Forward)
-ve indexes (-1 to -n) Last->First (Backward)
Ex:-
tup1 = (11,22,33,44,55);
print(tup1[0]);
print(tup1[1]);
print(tup1[2]);
print(tup1[3]);
print(tup1[4]);
print(tup1[-1]);
print(tup1[-2]);
print(tup1[-3]);
print(tup1[-4]);
print(tup1[-5]);
#print(tup1[100]);	#IndexError
#print(tup1[-100]);

2) Using slice-operator:-
= it gives sub-tuple values based on indexes and stepvalue
Syn:-
	tup1[startindex:endindex:stepvalue]
= startindex/endindex/stepvalue can be +ve or -ve
Ex:-
tup1 = (11,22,33,44,55);
print(tup1[0]);
print(tup1[1:5]);
print(tup1[0::2]);
print(tup1[0:100:2]);
print(tup1[-1:-5:2]);



==> Tuple and Immutability:-
= Immutable means org-data cannot be modified
= Once tuple is created it's values cannot be changed (Immutable)
Ex:-
tup1 = (11,22,33,44,55);
print(tup1);
tup1[0]=111;


==> Mathematical Operations on Tuple:-
= Here we can apply + and * operators

1) Concatenation Operator (+):-
Ex:-
tup1 = (11,22,33);
tup2 = (44,55,66);
tup3 = tup1+tup2;
print(tup3);

2) Repetition Operator (*):-
Ex:-
tup1 = (11,22,33);
tup2 = tup1*3;
print(tup2);


==> Commonly used Functions in Tuple:-
1) len():-
= Gives No.of Elements in a Tuple
Ex:-
tup1 = (11,22,33);
print(len(tup1));

2) count():-
= Gives a particular element is repeated how many times
Ex:-
tup1 = (11,22,33,44,55,11,22,11);
print(count(11));
print(count(22));
print(count(55));

3) index():-
= Gives index-position of given element (1st occurance)
= If not there then we get "ValueError"
Ex:-
tup1 = (11,22,33,44,55,11,22,11);
print(tup1.index(11));
print(tup1.index(22));
print(tup1.index(222));	#ValueError

4) sorted()
= Sorts or Orders the element of tuple (default is ASC)
Ex:-
tup1 = (11,22,33,44,55,11,22,11);
tup2 = sorted(tup1)	#default ASC order
print(tup1);
print(tuple(tup2));
=** After sorting, tuple is converted to list
(becuase tuple is immutable)

Ex:- (DESC)
tup1 = (11,22,33,44,55,11,22,11);
tup2 = sorted(tup1,reverse=True);
print(tup1);
print(tup2);
=** After sorting, tuple is converted to list

5) min() and max():-
= It gives minimum and maximum values of a list
Ex:-
tup1 = (11,22,33,44,55,11,22,11);
print(min(tup1));
print(max(tup1));

6) cmp() #outdated from py-3
= Compares elements of both tuples and gives
0 (Equal)
-1 (1st tup < 2nd tup)
+1 (1st tup > 2nd tup)
Ex:-
tup1 = (11,22,33);
tup2 = (44,55,66);
tup3 = (11,22,33);
print(cmp(t1,t2));
print(cmp(t1,t3));
print(cmp(t2,t3));

=** cmp() is in Python2 but not from Python3


==> Tuple Packing and UnPacking:-
= Tuple is created by packing group of variables
= Packing means creating a tuple with 2 or more variables
= UnPacking means getting tuple-values into 2 or more variables
Ex:-
a=11;
b=22;
c=33;
d=44;
e=55;
tup1 = a,b,c,d,e;
print(tup1);

= Tuple unpacking is reverse of packing,
(UnPacking and assign its values to different variables)
Ex:-
tup1=(11,22,33,44,55);
a,b,c,d,e=tup1;
print(a);
print(b);
print(c);
print(d);
print(e);

=** While unpacking, no.of vars and values in tuple should be same o.w we get "ValueError"
Ex:-
tup1=(11,22,33,44,55);
a,b,c=tup1;	#ValueError
"""

###Program... (TupleEx1.py)
#Program to work with Tuple DS


#creating a tuple(with & w.o ()brackets)
#tup1 = 11,22,33,44,55;		#() are not-complusory(optional)
tup1 = (111,222,333,444,555);
print(tup1);
print(type(tup1));
'''

'''
#empty-tuple
tup1=();
print(tup1);
print(type(tup1));
'''

'''
#tuple with single-value(give , compulsory)
tup1=(10);	#Single-Value Tuple taken as int-value data-type
print(tup1);
print(type(tup1));
#sp-case
tup1=10,;			#(10,);	#Single-Value Tuple with , comma
print(tup1);
print(type(tup1));
'''

#Other Tuple Examples
'''
tup1=();    #empty-tuple
print(tup1);
print(type(tup1));
'''

'''
tup1=11,22,33; #tuple w.o ()
print(tup1);
print(type(tup1));
'''

'''
tup1=10;        #single-value(respective-dtype)
print(tup1);
print(type(tup1));
print()
tup1=10,;  #give ,(compulsory)
print(tup1);
print(type(tup1));
'''
'''
#single-value
tup1=(10);
print(tup1);
print(type(tup1));
print()
tup1=(10,);
print(tup1);
print(type(tup1));
'''
'''
tup1=(10,20,30);
print(tup1);
print(type(tup1));
'''

'''
#Creating Tuple with tuple()
list1 = [11,22,33];
tup1 = tuple(list1);	#converts list to tuple
print(tup1);
tup1 = tuple(range(0,20,2));	#converts range-values to tuple
print(tup1);
tup1 = tuple("hello") #str to tuple
print(tup1)
'''

'''
#Access Elements with indexes
tup1 = (11,22,33,44,55);
print(tup1[0]);
print(tup1[1]);
print(tup1[2]);
print(tup1[3]);
print(tup1[4]);
print(tup1[-1]);
print(tup1[-2]);
print(tup1[-3]);
print(tup1[-4]);
print(tup1[-5]);
# print(tup1[100]);	#IndexError (out-of-index-range)
# print(tup1[-100]);
'''

'''
#Using slice-operator [startindex:endindex:stepvalue]
tup1 = (11,22,33,44,55);
print(tup1[0]);
print(tup1[1:5]);
print(tup1[0::2]);
print(tup1[0:100:2]);
print(tup1[-1:-5:-2]);
'''

'''
#Tuple is Immutability
tup1 = (11,22,33,44,55);
print(tup1);
# tup1[0]=111;	#TypeError
print(tup1)
'''

'''
#Concatenation (using +)
tup1 = (11,22,33);
tup2 = (44,55,66);
tup3 = tup1+tup2;
print(tup3);
#Repetition (using *)
tup1 = (11,22,33);
tup2 = tup1*3;	#3*tup1
print(tup2);
'''

#Tuple-Functions
'''
#len()
#tup1 = (11,22,33);
tup1 = tuple("Welcome")
print(len(tup1));
'''

'''
#count()
tup1 = (11,22,33,44,55,11,22,11);
print(tup1.count(11));
print(tup1.count(22));
print(tup1.count(55));
print(tup1.count(99));
'''

'''

#index()
tup1 = (11,22,33,44,55,11,22,11);
print(tup1.index(11));
print(tup1.index(22));
# print(tup1.index(222));	#ValueError
'''

'''
#sorting (sorted())
tup1 = (11,22,33,44,55,11,22,11);
tup2 = sorted(tup1) #after sorting we get list
print(tup1);
print(tup2);	#Here we get list
print(tuple(tup2));	#list to tuple()
'''

'''
#sorted(tup1, revserve=True/Fase)
tup1 = (11,22,33,44,55,11,22,11);
tup2 = sorted(tup1,reverse=True);	#True means DESC-order (False(ASC))
print(tup1);
print(tuple(tup2));	#Here we get list #use tuple() to coverted it
'''

'''
#min() & max()
tup1 = (11,22,33,44,55,11,22,11);
print(min(tup1));
print(max(tup1));
'''

'''
#Tuple-packing (creating a tuple)
a=11;
b=22;
c=33;
d=44;
e=55;
tup1 = a,b,c,d,e;
print(tup1);
'''

'''
#Tuple-unpacking
tup1=(11,22,33,44,55);
a,b,c,d,e=tup1;
print(a);
print(b);
print(c);
print(d);
print(e);
'''

'''
tup1=(11,22,33,44,55);
# a,b,c=tup1;	#ValueError (5-values cannot be un-packed to 3-variables)



"""
==> Difference between List and Tuple:-
1)
= List values are Mutable	(modified)
= Tuple values are Immutable (no-modified)

2)
= List values are given in [] (compulsory)
= Tuple values are given in () (Optional)

3) 
= Go for List if group of values are need to be changed
= Go for tuple if group of values are fixed need not be changed

----------------------------------------------------------
===>>> Set Collection or Data-Structure in Python:-
=> Tech-Points??
(Refer-notes)
	= It is coll.of Unique-values as single-unit
	= Duplicates are not allowed
	= Insertion Order is not preserved(**)
	= Sorting is possible (ASC/DESC)
	= Allows Homo/Heterogeneous Values (coll.of diff.data-type values)
	= Its values are Mutable (can be modified)
	= Represented in {......} with commas(,)
	= On Set, we can apply Union, Intersection, Difference etc mathematical operations
	= Set does not have indexes (slicing not-possible)

##Program (SetEx1.py)
(Program to work with Set DS)

=> Creating a Set:-
Ex:-
set1 = {11,22,33,44,55}; 
print(set1);
print(type(set1));

"""
# //Program (SetEx1.py)
# (Program to work with Set DS)

# Ex:- (Using set())
list1 = [11,22,33,44,55];
set1 = set(list1);
print(set1);
print(type(set1));

# Ex:- (Using range())
set1 = set(range(10));
print(set1);
print(type(set1));

set1 = set(range(10,20));
print(set1);
print(type(set1));

set1 = set(range(20,100,5));
print(set1);
print(type(set1));

"""
Ex:- (Empty-Set)
= It is created compulsory with set() function only but not with {}
set1 = {};
print(set1);
print(type(set1));
=** It becomes Dictionary type

set1 = set();
print(set1);
print(type(set1));
=* Now it is treated as Empty-Set


==> Commonly used Set functions:-
1) add(x):-
= Adds x to set
Ex:-
set1 = {11,22,33}
set1.add(55);
print(set1);

2) update(x,y,z):-
= Adds multiple items to set (from another-coll.of.data)
= x,y,z are not single-items but Iterable/Group of values like List,Range etc
Ex:-
set1 = {11,22,33}
list1 = [10,20,30];
set1.update(list1);
print(set1);

NOTE:-
= add() adds single-items to set
= update() adds multiple-items to set

= add() takes only 1-arg
= update() takes only multiple-arg

Ex:-
set1.add(10);		#Valid
set1.add(10,20,30);	#TypeError
set1.update(10);	#TypeError
set1.update(list1,range(1,10));	#Valid


3) copy():-
= It returns a duplicate-copy of the Set
= It is cloned object of Set
Ex:-
set1 = {11,22,33};
set2 = set1.copy();
print(set2);



4) pop():-
= It removes and returns any random element from Set
(Generally it remove from begin)
set1 = {11,22,33,44};
print(set1);
print(set1.pop());
print(set1);

5) remove(x):-
= It removes specified element from Set
(o.w we get "KeyError") 
Ex:-
set1 = {11,22,33,44,55};
set1.remove(33);
print(set1);
set1.remove(33);

6) discard(x):-
= It removes specified element from Set
(o.w we get NO-Error) 
Ex:-
set1 = {11,22,33,44,55};
set1.discard(33);
print(set1);
set1.discard(33);
print(set1);


7) clear():-
= Removes all elements in a Set
Ex:-
set1 = {11,22,33,44,55};
print(set1);
set1.clear();
print(set1);



==> Mathematical Operations on Set:-
(union/intersection/difference/symmetric_difference)
1) union():-
= set1.union(set2)
(or)
= set1 | set2
= It gives all the elements of set1 and set2 without duplicates
Ex:-
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.union(set2));
print(set1|set2);

2) intersection():-
= It gives only common values from given sets without duplicates
= set1.intersection(set2)
(or)
= set1 & set2
Ex:-
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.intersection(set2));
print(set1&set2);


3) difference():-
= It gives only 1st-set values which are not in 2nd-set
Ex:-
= set1.difference(set2)
(or)
= set1-set2
Ex:-
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.difference(set2));
print(set1-set2);

4) symmetric_difference():-
= It gives elements from both the sets without common-elements
Syntax:-
= set1.symmetric_difference(set2)
(or)
= set1^set2
Ex:-
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.symmetric_difference(set2));
print(set1^set2);


==> Membership Operators on Sets:- 
(in, not in)
= in checks for data in set 
= not in does not check for data in set
(True/False)
Ex:-
set1 = set("Hello Welcome");
print(set1);
print("H" in set1);
print("Z" in set1);
print("Z" not in set1);
"""


##Program.... (SetEx1.py)
#Program to work with Set-DS & its Operation


#creating a set using {}
set1 = {11,22,33,44,55,11,22,33}; 
print(set1);
print(type(set1));
'''


'''
#Using set() conversion-function
list1 = [11,22,33,44,55,11,22,33];
print(list1);
set1 = set(list1);
print(set1);
print(type(set1));
'''

'''
#set() with range()
set1 = set(range(10));
print(set1);
print(type(set1));
print()
set1 = set(range(10,20));
print(set1);
print(type(set1));
print()
set1 = set(range(20,100,5));
print(set1);
print(type(set1));
'''

'''
#Empty-Set (Sp-case)
set1 = {};	#takes as dict-obj
print(set1);
print(type(set1));
'''
'''
#sp-case
set1 = set();	#use empty-set() function
print(set1);
print(type(set1));
'''

'''
#Set-Functions
#add()
set1 = {11,22,33}
print(set1);
set1.add(55);
print(set1);
'''

'''
#update()->modify with another collection
set1 = {11,22,33}
list1 = [10,20,30];
set1.update(list1);
print(set1);
'''

'''
#update() multi-colls
set1 = {11,22,33}
list1 = [10,20,30];
set1.update(list1,range(100,110,2));
print(set1);
'''

'''
#copy() -> dup-set(cloning) sep-obj & sep-addr
set1 = {11,22,33};
set2 = set1.copy();
print(set1,id(set1))
print(set2,id(set2));	#Order is Not Preserved
set2.add(44)
print(set1)
print(set2)
'''

'''
#pop() -> del's random/first element
set1 = {11,22,33,44,55};
print(set1);
print(set1.pop());
print(set1.pop());
print(set1);
'''

'''
#remove(x) -> based on given value removed
set1 = {11,22,33,44,55};
print(set1);
set1.remove(33);
set1.remove(22);
print(set1);
#set1.remove(99);	#Error is value is not-found
'''

'''
#discard(x) -> removes given value but No-Error
set1 = {11,22,33,44,55};
print(set1);
set1.discard(22);
print(set1);
set1.discard(22);	#No-Error
print(set1);
'''

'''
#clear()
set1 = {11,22,33,44,55};
print(set1);
set1.clear();
print(set1);	#empty-set
'''

'''
#set-mathematical-operations
#Union on Sets (union(),|)
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1)
print(set2)
print(set1.union(set2));
print(set1|set2);
'''

'''
#Intersection on Sets (common-elements W.O dup)
#intersection() or & operator
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.intersection(set2));
print(set1&set2);
'''

'''
#Difference on Sets
#difference() or - operator
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.difference(set2));
print(set2.difference(set1));
print(set1-set2);
print(set2-set1);
'''

'''
#Symmetric-Difference on Sets (un-common elements)
#symmetric_difference() or ^ operator
set1 = {11,22,33,44};
set2 = {33,44,55,66};
print(set1.symmetric_difference(set2));
print(set1^set2);


#Membership operators (in, not in)
set1 = set("Hello Welcome");
print(set1);
print("H" in set1);
print("Z" in set1);
print("Z" not in set1);
print(" " in set1);


"""
---------------------------------------------------------
==> Frozenset Collection (or) Data-Structure(datatype):-
(Refer notes)
= It is same as that of set but it is Immutable
(Original-data cannot be modified)
= Here, we cannot use add() or remove() or pop() functions
**= Here we use frozenset() conversion-function to create a Frozen-Set

Ex:-
set1 = {10,20,30,40,50,"Sai",6.0,True};
fset1 = frozenset(set1);
print(fset1);
print(type(fset1));

##Program (FrozensetEx1.py)
(#Program to work with datatypes)

=> We can use loop to access display frozenset values
Ex:-
for x in fset1 : print(x);

=> Size is non-dynamic(FIXED) & Immutable (Org.data CANNOT be modified)
Ex:-
fset1.add(60);		#Error	
fset1.remove(44);	#Error
"""


##Program (FrozensetEx1.py)
#Program to work with FrozenSet Data-Structure(datatype)

#create FrozenSet using frozenset()
set1 = {10,20,30,40,50,"Sai",6.0,True,10,20};
fset1 = frozenset(set1);
print(fset1);
print(type(fset1));

#fset1.add(80);		#it is immutable (Error)
#fset1.remove(40);
#fset1.pop();


fset1 = frozenset({11,22,33,44,55,11});
print(fset1);
print(type(fset1))
#loops
for x in fset1: 
	print(x);


"Assignment"
##Program (FrozensetEx2.py)
##WAP to perform all operations of set same on frozenset
# Hint:-
# use SetEx1.py (replace set() with frozenset())
# (set1 replace fset1 var)

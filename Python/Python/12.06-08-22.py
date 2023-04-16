# 12th day 12.06-08-22

"""
==> Removing spaces from string:-
= We can remove or del or truncate extra-spaces from a string from left/right/both sides
= For this we have 3 functions,
a) rstrip() :- removes extra spaces from right-side
b) lstrip() :- removes extra spaces from left-side
c) strip() :- removes extra spaces from both-sides
"""
##Program (StringEx5.py)
##Prog to perform with string-stripping
##Program (StringEx5.py)
#Prog to perform with string-stripping/deleting/truncate extra spaces

ss = input("Enter your city-name : ");
#sscity = ss.strip();
#sscity = ss.lstrip();
sscity = ss.rstrip();
print(sscity,"is your city!!!");

"""
(***)
==> Finding Sub-strings:-
= To find any sub-string in main-string is done with 4-methods,
a) find()	//both forward-direction
b) index()
------------------
c) rfind()	//both backward-direction 
d) rindex()
(in all cases index is given from beginging 0 to n-1)
"""
##Program (StringEx6.py)
##Program to work with string-functions or methods

"""
==> Counting all sub-strings in main-string:-
= It is done with count() method/function
= it gives count of sub-string in org-string
Ex:-
ss.count(subss);	//from begin(0) to last(len)
ss.count(subss,beginIndex,endIndex);


==> Replacing a String with another string:-
= It is done with below method,
Syn:-
	ss.replace(oldstr, newstr);
= it replaces oldstr with newstr in org-str but we get new-string
	
NOTE:-
= String value(object) are immutable 
(org-str cannot be modified but can be re-assigned)
= Any changes done to org-str, new str-obj is created
= Hence in replace(), we got new-str after replace
"""

##Program (StringEx6.py)
##Program to work with string-functions or methods

#find() & rfind()
ss = "Hello Students, Welcome to Python Session, Hello by Sai sir";
#print(ss.find("Hello"));    #gives only 1st occurance
#print(ss.find("Java"));		#-1 on un-successful search
#print(ss.rfind("Hello"));
#print(ss.rfind("Java"));
##find(), rfind() we get -1 for un-successful search


#find(string,beg-ind,end-ind) & rfind(string,beg-ind,end-ind)
ss = "Hello Students, Welcome to Python, Hello all";
print(ss.find("Hello",6));	#From 6th-index to last-index
print(ss.find("Hello",6,20));
print(ss.rfind("Hello",0,30));
print(ss.rfind("Hello",6,len(ss)));
#print(ss.rfind("Hello",-1,-10));	#Here indexes cant be -ve
'''

'''
#index() and rindex() #here we get ValueError for un-successful search
ss = input("Enter Main String : ");
subss = input("Enter Sub String : ");
#print(ss.index(subss));
#print(ss.index(subss,9,len(ss)));
#print(ss.rindex(subss));		#0(begin) & len(end)
print(ss.rindex(subss,0,17));
'''

'''
#count()
#Counting all sub-strings in main-string
ss = "Hello Welcome to Python Hello users";
#print(ss.count("Hello"));
#print(ss.count("Hello",6));
#print(ss.count("Hello",6,len(ss)));
#print(ss.count("Welcome",6));
#print(ss.count("Welcome",8));
'''

'''
#replace()
#Replacing old-str with new-str
ss = "Hello, Welcome to Python, Hello users";
#newss = ss.replace('e','*');
print(ss)
print(id(ss))
newss = ss.replace('Hello','Hi');
print(ss);
print(id(ss))
print(newss);


#Immutable str-obj
ss = "Hello Welcome";
newss = ss.replace('e','*');
print(ss,"===>",id(ss));
print(newss,"===>",id(newss));

"""

(***)
===> Splitting of Strings:-
= We can split given string into sub-strings 
(we get list of sub-string values i.e, ['','','','',''])
= splitting is done based on separator
= Default separator is space
Ex:-
	sublist  = ss.split('separator');
= Return-type is List dtype(list of string-values)
"""
##Program (StringEx7.py)
##(Program to work with string functions)

"""
==> Joining of Strings:-
= it is used to join coll.of.strs to single string using a seperator
Ex:-
	newss = separator.join(group of string);
Ex:-
	newss = " ".join(list1);
		"-"
		":"	
		";"			
		","
"""
##Program (StringEx7.py)
# (Program to work with string functions)

"""
==> Changing case of a string:-
= Using below methods, we can change string-cases
a) upper() 		#converts to upper-case
b) lower() 		#converts to lower-case
c) swapcase() 	#converts to upper to lower & lower to upper
d) title() 		#converts each word 1st letter to Upper-case
e) capitalize()	#only 1st-char will be converted to upper-case
"""
##Program (StringEx7.py)
#(Program to work with string functions)

"""
==> Checking Starting and Ending part of a string:-
= These methods returns True or False
Ex:-
	ss.startswith(str);
	ss.endswith(str);
"""
##Program (StringEx7.py)
##Program (StringEx7.py)
#Program to work with string functions(operations)


#split()
ss = "Hello Students, Welcome to, Python Session";
#listss = ss.split(' ');
#listss = ss.split();
listss = ss.split(",");
print(listss);
'''

'''
#join()
listss = ['Hello', 'Students', 'Welcome', 'to', 'Python', 'Session'];
#Joining of strings
ss = " ".join(listss);
print(ss);
ss = "-".join(listss);
print(ss);
ss = "".join(listss);       #empty-string
print(ss);
ss = "-".join(["Sai","Ram","Ali"]);
print(ss);
listss = ["Hyd","Mum","Che","Delhi"];
ss = ":".join(listss);
print(ss);
'''

'''
##Changing-cases in string
ss = "Hello welcome to Python session";
print(ss.upper());
print(ss.lower());
print(ss.swapcase());
print(ss.title());
print(ss.capitalize());


#Starting & Ending strings
ss = "Hello Students, Welcome to Python Session";
print(ss.startswith("Hello"));
print(ss.endswith("Session"));
print(ss.startswith("Hi"));
print(ss.endswith("Bye"));


"""
==>> Checking Type-of-Characters in string:-
= For this we use following methods,
a) isalnum()	#checks for alphabets or digits (a-z,A-Z,0-9)
b) isalpha()	#checks for alphabets only (a-z,A-Z)
c) isdigit()	#checks for digits only (0-9)
d) islower()	#checks for lower-case alphabets only (a-z)
e) isupper()	#checks for upper-case alphabets only (A-Z)
f) istitle()	#checks for title-case string
g) isspace()	#checks for ONLY space chars only

=** All functions returns True or False
"""
##Program (StringEx8.py)
#(Program to work with string functions)

##Program (StringEx8.py)
#Program to work with string functions (Type of Characters)

ss="SaiRam123";
print(ss.isalnum());
print(ss.isalpha());

print()
ss="SaiRam";
print(ss.isalpha());
print(ss.isdigit());

print()
ss="123123";
print(ss.isdigit());

print()
ss="sairam";
print(ss.islower());
print(ss.isupper());

print()
ss="sairam123";
print(ss.islower());	#**sp-case(T)
print()
ss="SAI123";
print(ss.isupper());    ##**

print()
ss="Hello Students Welcome To Python";
print(ss.istitle());

print()
ss="Hello students Welcome to Python";
print(ss.istitle());

print()
ss=" ";
print(ss.isspace());
ss="\t";
print(ss.isspace());
ss="\n";
print(ss.isspace());
ss="\b";		#**sp-case
print(ss.isspace());
ss="\r";
print(ss.isspace());

"""
==>> Formatting the string using print():-
({} replacement-operator and format() func)
= In print(), while printing string-data(quotes), we can use replacement-operator and format() func
Ex:-
	print("Sum of {} and {} == {}".format(a,b,sum))
	= here a,b,sum are replaced inside string at {} replacement-operator
	
##Program (StringEx9.py)
(Program to work with string formats for print() )

NOTE:-
= We can use {} replacement-operator in 3-cases
	a) without indexes
	b) with indexes
	c) with vars (order can be changed in format())
"""
##Program (StringEx9.py)
#Program to work with string formats with print() using {} & format()


#case-1
rno=1001;
name="Sai";
height=6.0;
print("RollNo : {}\nName: {}\nHeight: {}".format(rno,name,height));


#case-2
print();
rno=1001;
name="Sai";
height=6.0;
#using-indexes
print("RollNo : {0}\nHeight: {2}\nName:{1}".format(rno,name,height));

#case-3
#using-vars (we can change the order)
rno=1001;
name="Sai";
height=6.0;
print("Name: {y}\nHeight: {z}RollNo : {x}\n".format(x=rno,y=name,z=height));
print("Name: {y}\nRollNo : {x}\nHeight: {z}".format(y=name,z=height,x=rno));





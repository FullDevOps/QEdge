# -- 37th day 37.07-09-22
'''
==>> Type of chars in Regex::-
= Characters are of 5-types
==Diagram==
(a-z, A-Z, 0-9, spaces, sp-chars)


***(General-topic)***
==> How to make Regex-Pattern-string???
(Every RegEx pattern is a string)
= We can make pattern-string in 3-ways
i) Character-classes
ii) Meta-Chars(Esc-Seq-chars)
iii) Quantifiers


Ist-one)
==> Character class:- "[...]" (pattern-string)
= Character classes can be used to search group of characters
1) [abc]	-> either a OR b OR c
2) [^abc]	-> Except a and b and c
3) [a-z]	-> Any lower-case alphabet (either of any char)
4) [A-Z]	-> Any upper-case alphabet (either of any char)
5) [a-zA-Z]	-> Any lower/upper-case alphabet (either of any char)
6) [0-9]	-> Any digit from 0 to 9 (either of any digit)
7) [a-zA-Z0-9]	-> Any Alpha-Numeric char (either of them)
8) [^a-zA-Z0-9]	-> Except Alpha-Numeric chars (none of them)
= Here ^ means "not"
'''
# Ex:-
#Program (RegEx2.py)
#using character classes
#Program (RegEx2.py)

#using character classes [....]
import re;
x="[abc]";
x="[^abc]";
x="[a-z]";
x="[0-9]";
x="[a-zA-Z0-9]";
x="[^a-zA-Z0-9]";

matcher=re.finditer(x,"a7bc@k9z p1");
for mm in matcher:
	print(mm.start(),"\t",mm.group());

'''
----------------------------------------------------------------
**(Meta-Chars) for pattern-string::-
==> Predefined Character classes with ESC.SEQ.CHAR:-
(\ back-slash) Ex::- "\s"
1) \s -> Space-char
2) \S -> Except Space any other char is matched
3) \d -> Any digit from 0 to 9
4) \D -> Any char except digit
5) \w -> Any word char [a-zA-Z0-9] including digits
6) \W -> Any Sp.char except word char (Sp.chars or Spaces-char)
7) . -> Any char including Sp.chars/Spaces
'''
# Ex:-
#Program (RegEx3.py)
#using pre-defined character classes
#Program (RegEx3.py)
#using pre-defined character classes

import re;
x="\s";
x="\S";
x="\d";
x="\D";
x="\w";
x="\W";
x=".";
matcher=re.finditer(x,"a7b k@9z");
for mm in matcher:
	print(mm.start(),"\t",mm.group());



'''
---------------------------------------------------------------------
==> Quantifiers in RegEx:- "qty" (pattern-string)
= Quantifiers gives no.of occurrences to given match
1) a -> Exactly one single 'a' is matched
2) a+ -> Atleast one 'a' (1 or more) Ex:- a,aa,aaa,...
3) a* -> Any no.of a's including Zero 'a' (0 or more)
4) a? -> Atmost one 'a' (0 or 1 only)
5) a{m} -> Exactly m-no.of a's
6) a{m,n} -> Min m-no.of a's & Max n-no.of a's
'''
# Ex:-
#Program (RegEx4.py)
#using quantifiers
#Program (RegEx4.py)

#using quantifiers(no.of.times)
import re;
x="a";
x="a+";
x="a*";
x="a?";
x="a{1}";
x="a{2}";
x="a{3}";
x="a{2,3}";

matcher=re.finditer(x,"abaabaaab");
for mm in matcher:
	print(mm.start(),"\t",mm.group());

'''
NOTE:-
1) ^x -> checks whether target string starts with x or not
2) x$ -> checks whether target string ends with x or not
(x is 1 or more chars of above cases)


--------------------------------------------------------------------
==> Functions in "re" module:-
1) match()
2) fullmatch()
3) search()
4) findall()
5) finditer()
6) sub()
7) subn()
8) split()
9) compile()

#Program (RegEx5.py)

1) match()
= Checks given pattern at beginning of original-string
= If it matches then we get Match-object(start(),end(),group) o.w None
Ex:-
#Program (RegEx5.py)
#using match()

2) fullmatch():-
= Here complete pattern is matched in Original-String
= If it matches then we get Match-object(start(),end(),group) o.w None
Ex:-
#Program (RegEx5.py)
#using fullmatch()


3) search():-
= It searches for 1st occurence of pattern in original-string
= If it matches then we get Match-object o.w None
Ex:-
#Program (RegEx5.py)
#using search()

4) findall():-
= Finds all occurrences of pattern-string in original-string
= It returns list-object with all occurrences
Ex:-
#Program (RegEx5.py)
#using findall()


5) finditer():-
= Gives iterator(loop) like Match-object for each successful match
= On Match-object, we can use start(),end(),group() functions
Ex:-
#Program (RegEx5.py)
#using finditer()


6) sub():-
= It means substitution or replacement
= re.sub(regex,replacement,targetstring)
= In target-string,every matching-pattern(regex) is replaced with replacement-string
Ex:-
#Program (RegEx5.py)
#using sub()


7) subn():-
= It is same as sub() but it also returns no.of replacements
= It returns/gives tuple
i.e, (newstring,no.of replacements)
Ex:-
#Program (RegEx5.py)
#using subn()


8) split():-
= Splits the original-string using given pattern-string
= It returns list of all tokens
Ex:-
#Program(RegEx5.py)
#using split()


9) ^ symbol with search():-
= It checks whether our original-string starts with our pattern-string or not
Ex:-
	result = re.search("^Welcome",org-string);
= If org-string starts with 'Welcome' then it returns Match-object o.w None
Ex:-
#Program(RegEx5.py)
#using ^ symbol


10) $ symbol with search():-
= It checks whether our original-string ends-with our pattern-string or not
Ex:-
	result = re.search("Python$",org-string);
= If org-string ends-with 'Python' then it returns Match-object o.w None
Ex:-
#Program(RegEx5.py)
#using $ symbol

NOTE:-
= If we wish to ignore the case then pass "re.IGNORECASE" as 3rd-arg to search()
Ex:-
result = re.search(pss,ss,re.IGNORECASE);
'''


#Program (RegEx5.py)
#re module functions


#using match()
import re;
ss =input("Enter Pattern-string to Check : ");
mm=re.match(ss,"abcabdefg");
if mm!=None:
	print("Matching is done at the beginning...");
	print("Start-Index :",mm.start(),"\tEnd-Index",mm.end()-1);
else:
	print("Match is NOT-available at the beginning...");
'''


'''
#using fullmatch()
import re;
ss =input("Enter Pattern to Check : ");
#mm=re.fullmatch(ss,"ababab");
mm=re.fullmatch(ss,"Welcome to Python Session")
if mm!=None:
	print("Full-Matching is done...");
	print("Start-Index :",mm.start(),"\tEnd-Index",mm.end()-1);
else:
	print("Full-Match is NOT-available...");
'''

'''
#using search()
import re;
ss =input("Enter search-Pattern to Check : ");
mm=re.search(ss,"ababab");
#mm=re.search(ss,"Welcome to Python Session");
if mm!=None:
	print("Search-Matching is done...");
	print("Start-Index :",mm.start(),"\tEnd-Index",mm.end()-1);
else:
	print("Search-Matching is NOT-available...");
'''


'''
#using findall()
import re;
ss=input("Enter finding-Pattern to Check : ");	#[0-9],[a-e],\s
list1=re.findall(ss,"ababab");
#list1=re.findall(ss,"Welcome to Python Session");
print(list1);
'''


'''
#using finditer()
import re;
ss=input("Enter finding-Pattern : ");
iter=re.finditer(ss,"Welcome to Python Session");
for mm in iter:
	print(mm.start(),"\t",mm.end()-1,"\t",mm.group());
'''


'''
#using sub()
import re;
ss=input("Enter Matching-Pattern : ");
ress=input("Enter Replacing-String : ");
newss=re.sub(ss,ress,"Welcome to Python Session");
print(newss);
'''


'''
#using subn()
import re;
ss=input("Enter Matching-Pattern : ");
ress=input("Enter Replacing-String : ");
tup1=re.subn(ss,ress,"Welcome to Python Session");
print(tup1);
print("New-String :",tup1[0]);
print("No.of Relacements :",tup1[1]);
'''


'''
#using split()
import re;
ss=input("Enter Original-string : ");
pss=input("Enter pattern-String : ");
list1=re.split(pss,ss);
print(list1);
for ll in list1:
	print(ll);
'''


'''
#using ^ symbol
import re;
ss=input("Enter Original-string : ");
pss=input("Enter ^ pattern-String : ");
result = re.search(pss,ss);
if result!=None:
	print("Original-String starts with Pattern-String");
else:
	print("Original-String does not starts with Pattern-String");




#using $ symbol
import re;
ss=input("Enter Original-string : ");
pss=input("Enter $ pattern-String : ");
result = re.search(pss,ss);
#result = re.search(pss,ss,re.IGNORECASE);
if result!=None:
	print("Original-String ends-with Pattern-String");
else:
	print("Original-String does not end-with Pattern-String");

'''''
---------------------------------------------------------------------

==> Regex-Case-Studies:- (Real-time Examples)

#Program (RegEx6.py)	
---------------------------------------------
1) WAP for RegEx to represent all 10-digits Mobile Number
Rules:
a) Mobile-No should be exactly 10-digit
b) 1st-digit should be 7 or 8 or 9
Ex:-
[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
(or)
[6-9][0-9]{9}
(or)
[6-9]\d{9}


NOTE:-
= We can use (91-), (0091) for group of chars in RegEx-Patterns
= (91|0091|[+]91|[+]91-) in regex grouping, we can use | for either of the selection inside group

NOTE:-
= (0091|91|[+]91) indicated either 0091 or 91 or +91
Here () means grouping of pattern/chars
= | indicates or
= [+] indicates 1-char is + before 91 o.w + (atleast one time)


2) WAP for email-id validation
3) WAP Vehicle reg-no validation

'''
#Program (RegEx6.py)
#Regex real-time-case-studies


#Valid 10-digit Mobile-No (1st-digit[6-9]& remaining 9-dig[0-9])
import re;
num=input("Enter Mobile-No : ");
mm = re.fullmatch("[6-9]\d{9}",num);
if mm!=None:
	print(num,"is a Valid-Mobile-No");
else:
	print(num,"is NOT a Valid-Mobile-No");
'''


'''
#Check whether given Mobile-No is Valid or NOT in India-code(+91)
import re;
ss = input("Enter Mobile-No : ");
mm = re.fullmatch("(0091|91|[+]91|[+]91-)?[6-9][0-9]{9}",ss);
if mm!=None:
	print("Valid Mobile-No");
else:
	print("Invalid Mobile-No");
'''


'''
#Check whether given Email-Id is Valid or NOT
import re;
ss = input("Enter Email-ID : ");
mm = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",ss);
if mm!=None:
	print("Valid Email-Id");
else:
	print("Invalid Email-Id");



#Check whether given Vehicle Reg-No is Valid or NOT in TS
import re;
ss = input("Enter Vehicle Reg-No : ");
mm = re.fullmatch("(TS|AP)[0123][0-9][A-Z]{1,2}\d{4}",ss);
if mm!=None:
	print("Valid Registration-No");
else:
	print("Invalid Registration-No");




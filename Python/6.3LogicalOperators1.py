##Program (LogicalOperators1.py)
#Program to work with Logical Operators


a=10;
b=20;
#logical-and
print(a>5 and b>5)	#T and T (True)
print(a>5 and b<5)	#T and F (False)
print(a<5 and b>5)	#F and T (False)
print(a<5 and b<5)	#F and F (False)

print()
###
#logical-or
print(a>5 or b==20);	#T or T (True)
print(a>5 or b!=20);	#T or F (True)
print(a<5 or b==20);	#F or T (True)
print(a<5 or b!=20);	#F or F (False)

print()
###
#logical-not
print(not (a==b));	#not F(True)
print(not (a!=b));	#not T(False)


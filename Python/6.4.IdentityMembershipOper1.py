##Program (IdentityMembershipOper1.py)
##Program to work with Identity-Operator & Membership-Operator

'''
#is, is not
a=10;
b=10;
print(a is b);
###
a=10;
b=20;
print(a is not b);
###
a=True;
b=False;
print(a is b);
print(a is not b);
###
a="Sai";
b="Sai";
print(id(a));
print(id(b));
print(a is b);
print(a is not b);
'''


#in, not in
#using strings
ss = "Hello and Welcome";
print('H' in ss);
print('z' in ss);
print('x' not in ss);
print('and' in ss);
print('or' in ss);
print('HW' in ss);
print()
#using lists
a=[10,20,30,"Sai",6.0,True];
print(10 in a);
print(100 in a);
print("Sai" in a);
print("Ram" not in a);
print(True not in a);

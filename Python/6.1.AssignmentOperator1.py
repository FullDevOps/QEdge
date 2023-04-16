##Program (AssignmentOperator1.py)
#Program to demo Assignment-Operator

a=10;
b=20;
sum=a+b;    #30
print(a,b,sum);

print()
####multi-var-assignment
a=b=c=10;   #multi-vars with same-value
x,y,z=11,22,33;     #multi-vars with diff-vals
print(a);
print(b);
print(c);
print(x);
print(y);
print(z);

print()
####sp-case
#Compound Assignments
a=11;
b=3;
a+=b;	#a=a+b;
print(a);
print(b);

a=11;
b=3;
a-=b;
print(a);
print(b);

a=11;
b=3;
a*=b;
print(a);
print(b);

a=11;
b=3;
a/=b;
print(a);
print(b);

a=11;
b=3;
a%=b;
print(a);
print(b);

a=11;
b=3;
a//=b;
print(a);
print(b);

a=11;
b=3;
a**=b;
print(a);
print(b);

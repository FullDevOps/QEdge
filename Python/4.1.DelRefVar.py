##Program (DelRefVar.py)
#Program to demo Reference Deletion

a=10
b=20
print(a,b)
print(id(a),id(b))

del a
del b
#print(a,b)     #NameError
c=10
d=20
print(c,d)
print(id(c),id(d))

del c,d;
#print(c,d)     #NameError







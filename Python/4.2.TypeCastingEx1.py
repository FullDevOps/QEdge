#Program (TypeCastingEx1.py)
#Program to demo Typecasting with python-functions

#int()
a=int(10)
a=int(10.8)     #complete deci-part is deleted
a=int("100")
#a=int("hi")       #ValueError
a=int(True)
#a=int(5+6j)    #complex is not-convertible
print(a)
print(type(a))


print()
#float()
a=float(10)     #deci-point(.) is added
a=float(10.8)
a=float("100")
#a=float("hi")       #ValueError
a=float(True)
#a=float(5+6j)    #complex is not-convertible
print(a)
print(type(a))


print()
#complex()
a=complex(10)
a=complex(10.8)
a=complex("100")
#a=complex("hi")       #ValueError
a=complex(True)
a=complex(5+6j)
a=complex("15+6j")
a=complex(5,6)
a=complex(5.5,6.6)
print(a)
print(type(a))


print()
#bool()
a=bool(1)
a=bool(0)
a=bool(10)      #non-zero is True & any zero is False
a=bool("hi")    #**sp-case any-string is T & empty-str is F
a=bool("False")
a=bool("")      #w.o any chars is empty-string
print(a)
print(type(a))


print()
#str()
a=str(10)
a=str(10.5)
a=str("hi")
a=str(True)
a=str(5+6j)
print(a)
print(type(a))
#sp-case
print(10+10)
#print(str(10)+10)       #"10"+10 (str+int) Error
print(str(10)+str(10))      #"10"+"10" ---> 1010




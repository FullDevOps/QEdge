##Program (RangeDatatypeEx1.py)
#Program to work with range-coll-datatype

r1 = range(10);	    #0 to 9
print(r1);
print(type(r1));
#access
print(r1[0],r1[-1])
print(r1[1],r1[-2])
print(r1[2],r1[-3])
print(r1[3],r1[-4])
print(r1[4],r1[-5])
print(r1[5],r1[-6])
print(r1[6],r1[-7])
print(r1[7],r1[-8])
print(r1[8],r1[-9])
print(r1[9],r1[-10])
print()
#using-loops-access
for i in r1:
	print(i);

    
print();
r1 = range(10,20);	   #10 to 19 
for i in r1:
	print(i);	

print()
r1 = range(10,20,2);     #10,12,14,16,18 (Step-value=2)
for i in r1: print(i);

print()
r1 = range(10,20,3);  
for i in r1: print(i);

print()
r = range(20,10,-2);  
for i in r:	print(i);


print()
r1 = range(1,20,-2);     #range not generated
for i in r1:	print(i);
#1,20(forward-range) but -2(Backward-step)


print()
r = range(20,1,2);     #range not generated
for i in r:	print(i);
#20,1(backward-range) but +2(Farward-step)


#range with indexes
print();
r = range(1,11);    #1 to 10 values		    
print(r[0]);
print(r[1]);
print(r[-1]);
print(r[-2]);	
#print(r[20]);	#IndexError	

print()
#range-coll in immutable
#r[0]=100;		#TypeError (range values are immutable-obj)

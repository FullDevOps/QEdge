##Program (CmdLineArgs.py)
#Program to demo Cmd-Line-Args

import sys;     #sys.py module-py-file
print(sys.argv);	#all values are strings in list-of-values

print()
#using indexes
print(sys.argv[0]);
print(sys.argv[1]);
print(sys.argv[2]);
print(sys.argv[3]);

print()
print(type(sys.argv));
print("No.of Args : ",len(sys.argv));       #len() func

print()
#using loop
for x in sys.argv:  #[4-values]
	print(x);



'''
##Assignment on Cmd-Line-Args
##WAP to accept to input-values as Cmd-Line-Args(11,3) & perform Arithmetic-Opers
a = int(sys.argv[1])
b = int(sys.argv[2])

##WAP to accept to input-values as Cmd-Line-Args(11.5,2.5) & perform Arithmetic-Opers
x = float(sys.argv[1])
y = float(sys.argv[2])
'''
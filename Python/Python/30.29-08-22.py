# 30th day 30.29-08-22

"""			
==>>> Files-Handling in Python:-
def:-
	= A computer-file is a collection of data, which is stored permanently on a disk using filename
Ex:
	abc.txt (text-files)
	Resume.doc (Doc-files)
	myoffice.ppt
	etc...
	
NOTE:-
**= The data which is processed in program is temporary
Ex:-
	a=10;
	b=20;
	print(a+b);
= Once execution is done it is deleted from memory
=** To make it permanent for future references, we use files
(program-data is stored in files and used for next-executions)
Ex:- 
	Student-data
	Employee-data
	Aadhar-data
	etc..

=> Types of Files:-
= There are 2-types of files used for python-programming
1) Text-Files
= Stores data in the form of characters
Ex:- "Hello, Welcome, bye"
2) Binary-Files
= Stores data in the form of binary-format (0,1) like images,audio,video files, setup-files etc



==> Steps(3)::-
1) Open the file
2) Perform Operation on File (R/W/A)
3) Close the file


==> Opening a file in Program:-
= For this we use open() function
= While opening a file, we have to specify file-opening-mode
Syntax:-
	f1 = open(filename,filemode);
Ex:-
	f1 = open("abc.txt","r");
==Diagram==
	[f1]------->[Org-file]"abc.txt"


==> File-Modes::-(7-types)	
=**Commonly used file-modes are,
1) r 
= Opens a file for read-mode (Reading-Purpose)
= It is default mode
= Inside the file, file-pointer(cursor) is placed at beginning
= If file is not exists then we get "FileNotFoundError" (exception)

2) w
= Opens a file for write-mode (Writing-Purpose)
= If file already there then it will over-write the file
= If file Not-there then it will create a new file

3) a
= Opens an existing file for append-mode (adding data from end-of-file)
= Inside the file, file-pointer(cursor) is placed at end for appending
= If file is Not-there then it will create a new file

4) r+
= Opens a file for read & write-data (Both-Purpose)
= Previous data in file is not deleted or not over-written
= File-Pointer (cursor) is placed at beginning of file

5) w+
= Opens a file for write & read-data (Both-Purpose)
= Previous data in file is over-written
= File-Pointer (cursor) is placed at beginning of file

6) a+
= Opens a file for append & read-data (Both-Purpose)
= Previous data in file is NOT over-written
= File-Pointer (cursor) is placed at end of file

7) x	(exclusive-write-mode)
= Opens a file in exclusion creation mode for write-operation
= If file already there then we get FileExistsError (exception) no over-writing

NOTE:-
= All modes are applicable for text-files
= Add or suffix "b" at end then it become binary-files modes
Ex:-
	rb, wb, ab, r+b, w+b, a+b, xb

Ex:-
f1 = open("aaa.txt","w");
= Opens a file "aaa.txt" for write-mode
= If no file then creates a new-file
= If file exists then over-writes the data in file
 
==> Closing a file:-
= After completing file-operations, we close the file using close() function
Ex:-
	f1.close();

NOTE:-
f1 is file obj.ref.var
==Diagram==
[f1]------>[aaa.txt]



==> File object properties:-
(in python everything is object, including files)
= Once file is opened in program, we have to work with file for read/write/append purpose
= To work with file operations, we have diff properties(variable)
1) name --> name of the opened-file Ex:- f1.name
2) mode --> Mode in which file is opened
3) closed --> checks for file open or closed (True/False)
4) readable() --> checks for file is readable or not (True/False)
5) writable() --> checks for file is writable or not (True/False)
"""
# Ex:-
#Program (FileEx1.py)
# (Program to open a file and check diff properties)
#Program to open a file and check diff properties

fname = input("Enter any filename : ");		#aa.txt
#f1 = open(fname,"w");
f1 = open(fname,"r");
print("File-name :",f1.name);
print("File-Mode :",f1.mode);
print("File-is Readable :",f1.readable());
print("File-is Writable :",f1.writable());
print("File-is Closed :",f1.closed);
f1.close();
print("File-is Closed :",f1.closed);


"""
==> Writing data to text-files:-
= It is done with 2-methods,
	1) write(str) #writes given str-data on file
	2) writelines(list of lines)
		#writes given list-data as multi-lines on file
"""
# Ex:-
#Program (FileEx2.py)
#Program to open a file and write data on it

fname = input("Enter any filename : ");  #bb.txt
#f1 = open(fname,"w");		#write-mode(over-write***)
f1 = open(fname,"a");		#append-mode(add-from-end)
print("File-is opened for Writing data");

#f1.write("Sai Kumar\n");
#f1.write("India Country\n");
#f1.write("Hyderabad City\n");
f1.write("Ram\n");
f1.write("India\n");
f1.write("Secbad\n");

f1.close();
print("File-Data Writing is done");


"""
NOTE:-
= If program is executed multiple-times using "w" then data is over-written with new-data
= for this we can use "a" mode (append-mode)
Ex:-
f1 = open(fname,"a");	
"""
# Ex:-
#Program (FileEx3.py)
#Program to open a file and write multi-line data on it writelines()

fname = input("Enter any filename : ");  #cc.txt
#f1 = open(fname,"w");
f1 = open(fname,"a");

print("File-is opened for Writing data");

list1 = ["Sai\n","Ram\n","Ali\n","Tom\n","Pop\n"];
f1.writelines(list1);
f1.close();
print("File-Data Writing is done");



# NOTE:-
# While using write() or writelines(), "\n" separator is compulsory for multiple lines of data o.w we get single-line data
	

"""
==> Reading Char data from Text-Files:-
= To read char-data from text-files, we use below methods,
1) read()	=> 	Reads total-data at a time from a file
2) read(n)  =>	Reads n-chars from a file
3) readLine() => Reads 1-line at a time
4) readLines() => Reads All-lines at a time into a List DS
"""
# Ex1:-
#Program (FileEx4.py)
# (Program to read data from a file with diff read-methods)
#Program to read total data from a file
#Program (FileEx4.py)


#read()			#bb.txt
fname = input("Enter any filename : ");
f1 = open(fname,"r");
data = f1.read();
print(data);
f1.close();
'''

'''
#read(n)
fname = input("Enter any filename : ");
f1 = open(fname,"r");
data = f1.read(10);
print(data);
f1.close();
'''


'''
#readline() #use loop to read all lines one by one till last
fname = input("Enter any filename : ");
f1 = open(fname,"r");		#bb.txt
line1 = f1.readline();
print(line1,end="");
line2 = f1.readline();
print(line2,end="");
line3 = f1.readline();
print(line3,end="");
f1.close();



#readLines()
fname = input("Enter any filename : ");
f1 = open(fname,"r");
listlines = f1.readlines();
print(listlines);
for line in listlines:
	print(line,end="");
f1.close();



"""
**sp-case of open()**
==> with statement to open a file:-
(it is header-stmt to open a file)
(it provides suite to perform diff operations on a file)
Ex:-
	with open(fname,"w") as f1:
		...
		...
		...
		...
		
= we can also use with statement to open a file
= with stmt can be used to group file-operations as a block of code
= Advantage is it closes the file after all operations are done, even if exception occurs not need to close explicitly
"""
# Ex:-
#Program (FileEx5.py)
#Program to demo with-stmt to open a file

fname = input("Enter any filename : ");
with open(fname,"w") as f1:		#dd.txt
	f1.write("Sai\n");
	f1.write("India\n");
	f1.write("Hyderabad\n");
	print("Is File closed(inside with body) :",f1.closed);

#f1.close()  #not-required
print("Is File closed(outside with body) :",f1.closed);


"""
==> seek() and tell() functions:-
1) tell():-
= It gives current position of a cursor(file-pointer) inside a file from beginning
= index-position of 1st-char in a file is 0 
(same like string-indexes)
Ex:-
	f1.tell()
#Program (FileEx6.py)
(Program to demo tell() & seek() functions)

2) seek():-
= It is used to move the cursor(file-pointer) to specified location
Syntax:-
	f1.seek(offset,fromwhere);
	offset -> no.of positions
	fromwhere -> 0(default is begin), 1(current-position), 2(from end)
Ex:-
	f1.seek(10)		#+ve forward-move
	##f1.seek(-10)	#-ve backward-move(not-supports)
	
NOTE:-
= Python-2 supports 0,1,2 values but Python-3 supports only 0
"""
# Ex:-
#Program (FileEx6.py)
# (Program to demo tell() & seek() functions)
#Program to demo tell() & seek() function (FileEx6.py)


#tell()
fname = input("Enter any filename : "); #bb.txt
f1 = open(fname,"r");
print(f1.tell());
print(f1.readline());
print(f1.tell());
print(f1.readline());
print(f1.tell());
print(f1.readline());
print(f1.tell());
f1.close();



#seek()
data = "Hello Students, Welcome to Python";
fname = input("Enter any filename : ");
f1 = open(fname,"w");		#ee.txt
f1.write(data);
f1.close();

with open(fname,"r+") as f1:
	text = f1.read();
	print(text);
	print("Cursor is at :",f1.tell());
	f1.seek(16);
	print("Cursor is at :",f1.tell());
	f1.write("Weldone");
	f1.seek(0);
	text = f1.read();
	print(text);
	f1.close();
	

"""
==> Checking for file exists or not?
= For this we can use OS library to get info. about files in our computer
= "os" module  has "path" sub-module, it contains isFile(), using which we can check file exists or not
Ex:-
	os.path.isFile(filename);
Ex:-
"""
#Program (FileEx7.py)
# (Program to check whether file exists or not and display its data)
#Program to check whether file exists or not and display its data 
#(FileEx7.py)

import os,sys;
fname = input("Enter File-name : ");

if os.path.isfile(fname):
	print("File is there :",fname);
	f1=open(fname,"r");
	print("File Contents :");
	data=f1.read();
	print(data);
else:
	print("File doest NOT exists :",fname);
	sys.exit(0);

print("End of the Program");

# NOTE:-
# = sys.exit(0); #exits program execution process there only, done by PVM
# = 0 indicates Normal-Termination
# = 1 is Abnormal-Termination


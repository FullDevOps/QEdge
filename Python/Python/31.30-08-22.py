# 31st day 31.30-08-22

"""
(Working with Binary-Files)
==> Handling Binary-Files data:-
(Images,Audio,Video,etc file)
= Here we store data in the form of binary-bits(0,1)
Ex:-
	images
	audio
	video
	etc...
= For this we use "b" with filemodes
Example, 
	(rb, wb, ab, r+b, w+b, a+b, xb) -->binary-modes
=** here we use same reading & writing methods
"""
# Ex:-
#Program (FileEx8.py)
# (Program to read Image-File and write to New-Image-File)
#Program to read Image-File and write to New-Image-File (FileEx8.py)

fname1 = input("Enter Image File-name : ");
fname2 = input("Enter Copy-Image File-name : ");
f1 = open(fname1,"rb");
f2 = open(fname2,"wb");
bytesdata = f1.read();
f2.write(bytesdata);
f1.close();
f2.close();
print("Image Copying is Done");

"""
"Assignment" (Ex9 and Ex10)
#WAP to perfrom cut & paste operation in python program
(1st copy org-file)		#read()
(2nd paste dup-file)	#write()
(3rd del org-file)		#??
#WAP to perfrom multiple files copy & paste in single python program
(use list of file-names with for-loop)


==> Handling CSV file:-
= CSV means comma separated values
= table-data as text-file
= to work with .csv files, we have "csv-module"
==Diagram==
Ex:-
#Program (FileEx9.py)
(Prog to work with CSV-file)

step1:-
	f1 = open("students.csv","w");
	w1 = csv.writer(f1) gives csv-writer-object-ref
step2:-
=** write data using csv-writer-object-ref,
	w1.writerow(); takes list of values as input-para
step3:-
=** close csv-writer-object(w1) & also f1-file-obj
	
"""
#Prog to work with CSV-file writing mode
#(FileEx9.py)

import csv;
#with open("student.csv","w",newline='') as f1:
with open("student.csv","w") as f1:
	w1 = csv.writer(f1);	
	w1.writerow(["SNo","SName","Height","Address"]);
	n = int(input("Enter No.of Students : "));
	for i in range(n):
		print("Enter Students Data:");
		sno=input("Roll-No : ");
		sname=input("Name : ");
		height=input("Height : ");
		addr=input("Address : ");
		w1.writerow([sno,sname,height,addr]);
        
print("All Student data successfully written to student.csv file");


"""
NOTE:-
= W.O newline='' attribute parameter, in csv-file we get blank-lines between data
= With newline='' attribute parameter from Python-3 is required
= Python-2, we use "wb" and newline='' attribute is not required
=** Internally DB-tables & Excel-files are .csv files only(text-data)



==> Reading data from .csv file:-
= Opens csv file and read the data from the file

==> Reading data from .csv file:-
= Opens csv file and read the data from the file
Ex:-
#Program (FileEx10.py)
(Prog to work with CSV-file)
(open .csv file(f1),attach to csv-reader-obj(r1),read-data)

Step1:-
	=** r1 = csv.reader(f1) to get csv-reader-obj on .csv file
Step2:-
	=** r1.list(csv-reader-obj) we get complete-data from .csv file as nested-list
"""
# Ex:-
#Program (FileEx10.py)
#Prog to work with reading-CSV-file (FileEx10.py)

import csv;

f1 = open("student.csv","r");
r1 = csv.reader(f1);	#gives csv-file reader obj
csvdata = list(r1);		#nested-list
print(csvdata);

#access data with loops

for row in csvdata:
	for col in row:
		print(col,"\t",end='');
	print();


for row in csvdata:
	print(row)

print("End of the Program")	;


"""
==> Zipping & UnZipping files:-
= Zipping means compressing the files
= UnZipping means un-compressing the files
= Advantage,
	- Less Memory Space
	- Easy File-sharing
	- Improves Performance
	
(***)	
= zipfile-module is used to work with this
= It contains "ZipFile" class

=> How to create .zip file:-
= Step1:-
= Create an object of ZipFile-class
(use zip-filename, mode, ZIP_DEFLATED constant)
Ex:-
f1 = ZipFile("files.zip","w",ZIP_DEFLATED);	
#ZIP_DEFLATED means creating a new-zipfile

= Step2:-
= Once file is created, add files to it using write() method
f1.write("aa.txt");
f1.write("bb.txt");
f1.write("cc.txt");
"""
# Ex:-
#Program (FileEx11.py)
# (Program to work with .zip files)
#Program to work with .zip files
#FileEx11.py

from zipfile import *
f1 = ZipFile("files.zip","w",ZIP_DEFLATED);
f1.write("aa.txt");
f1.write("bb.txt");
f1.write("cc.txt");
f1.close();
print("files.zip file is created");


"""
=> How to unzip a file?
= For this create ZipFile obj as follows,
Ex:-
	f1 = ZipFile("files.zip","r",ZIP_STORED);
= ZIP_STORED constant represents unzip operation
(its a default-value)
=** Once object is created, we get all file-names using namelist() method
Ex:-
	filenames = f1.namelist();
	f1.printdir()
	f1.extractall()
"""
	
	
# Ex:-
#Program (FileEx12.py)
# (Program to work with .zip files)
#Program to work with .zip files

import time;

from zipfile import *
f1 = ZipFile("files.zip","r",ZIP_STORED);
filenames = f1.namelist();
print(filenames);

time.sleep(5);
f1.printdir();

time.sleep(5);
f1.extractall();

print("End of the Program");	

"""
==> Working with Directories?
= Some common operations on directories are, (folders)
a) Current Working Directory
b) Create New Directory
c) Remove Existing Directory
d) Rename a Directory
e) List contents of Directory
etc
=** For this we use "os" module 
(to perform above operations)
=> Current Working Directory?
= getcwd()
Ex:
import os;
cwd = os.getcwd();
print(cwd);

#Program (FileEx13.py)
(Program to work with Directories)


=> Creating Sub-Directory?
= mkdir("sub-dir");
Ex:-
import os;
os.mkdir("subfiles");
print("subfiles sub-dir is created");

=> Creating sub-dir in another directory?
Ex:-
import os;
os.mkdir("subfiles/subsubfiles");
print("subsubfiles dir is created inside subfiles directory");

=> Creating multiple directories with sub-directories at a time?
= makedirs()
Ex:-
import os;
os.makedirs("sub1/sub2/sub3");
print("multiple directories with sub-directories created");


=> Remove a Directory?
= rmdir()	#1-dir at a time
Ex:-
import os;
os.rmdir("subfiles/subsubfiles");
print("subsubfiles directory is removed");

=> Removing multiple-directories in path?
= removedirs()	#multiple-dirs at a time
Ex:-
import os;
os.removedirs("sub1/sub2/sub3");
print("All sub1/sub2/sub3 directories are removed");

=> Rename Directory:-
= rename()
Ex:-
import os;
os.rename("subfiles","newsubfiles");
print("Directory is Renamed");

=> Directory Contents:-
= listdir()
Ex:-
import os;
print(os.listdir("."));		#. means current-directory
= It is displayed as list of data
"""


#Program
#Program to work with Directories (FileEx13.py)


#getcwd()
#Current Working Directory
import os;
cwd = os.getcwd();
print(cwd);
'''

'''
#mkdir()
#Creating Directory & Sub-Directory
import os;
os.mkdir("subfiles");
print("subfiles sub-dir is created");
'''
'''
import os;
os.mkdir("subfiles/subsubfiles");
print("subsubfiles dir is created inside subfiles directory");
'''

'''
#makedirs()
#creating multiple sub-directories at a time
import os;
os.makedirs("sub1/sub2/sub3");
print("multiple directories with sub-directories created");
'''

'''
#rmdir()
#Removing Directory
import os;
os.rmdir("subfiles/subsubfiles");
print("subsubfiles directory is removed");
'''

'''
#removedirs()
#Removing multiple sub-directories at a time
import os;
os.removedirs("sub1/sub2/sub3");
print("All sub1/sub2/sub3 directories are removed");
'''

'''
#rename()
#Renaming a Directory
import os;
os.rename("subfiles","newsubfiles");
print("Directory is Renamed");
'''

'''
#listdir()
#Listing all the contents of directory
import os;
print(os.listdir("."));		#. means current-directory


"""
(******)
-----------
==> Pickling and UnPickling of Objects:-
= It is Serialization and De-Serialization in Java
= It is used to write complete state of object to file and read complete state of object from a file
= Pickling means writing state of an object to a file
= UnPickling means reading state of an object from a file
Ex:- Student-obj or Employee-obj etc

=** To perform this we use pickle-module
= For Pickling we use dump() function
Ex:-	
	pickle.dump(object, filerefvar);
= For UnPickling we use load() function
Ex:-
	obj = pickle.load(filerefvar);
==Diagram==
(s1,s2,studentfile.txt)

NOTE:-
= Pickling & UnPickling is done as binary-data
(0's and 1's) ---> hence use "wb" and "rb" modes
"""
# Ex:-
#Program (PickUnpick.py)
# (Program to perform Pickling and UnPickling)
#Program to perform Pickling and UnPickling
#PickUnpick.py

import pickle;
class Student:
	def __init__(self,sno,sname,height):
		self.sno=sno;
		self.sname=sname;
		self.height=height;
	def display(self):
		print(self.sno,"\t",self.sname,"\t",self.height);
		
        
#pickling        
with open("studentfile.txt","wb") as f1:
	s1 = Student(1001,"Sai",6.0);
	pickle.dump(s1,f1);
	print("Student-Data is Pickled :");
 

#unpickling	
with open("studentfile.txt","rb") as f1:
	s2 = pickle.load(f1);
	print("Student-Data(after UnPickling) :");
	s2.display();









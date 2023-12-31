# 39th day 10.09.22
# --------------------------------------------
'''''
****Data-Science Modules in Python*****
= Data-Science means working with Big-data in program
Ex:-
	Getting-data
	Formatting-data
	Searching-data
	Sorting-data
	Cleaning-data
	Ananlysing-data
	etc...
= To work with data-science in python, we have 4-modules,
	a) NumPy
	b) Pandas
	c) SciPy or SciKit
	d) MatPlotLib
	
--------------------------------------------
===>>> NumPy Arrays in Python:- 
=> What is NumPy?
= NumPy means Numerical-Python
= NumPy is a python-library, which is used for working with Arrays in Python
= It also provides functions to work with Linear-Algebra, Matrices in Mathematics etc
= It was created by Travis Oliphant(2005)
= It is an open-source project and we can use it freely
(NumPy stands for Numerical-Python)

=> Why NumPy?
= In Python we have Lists & array-Module for Arrays concept, but they are slow to processing data
= NumPy provides an array-object (it is 50-times faster than Python-lists & Python-arrays)
= The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
= Arrays are used in Data-Science

NOTE:-
= NumPy are Faster than Lists because they are stored at one continuous place in memory unlike lists
= It is optimized to work with latest CPU architectures
= It is a Python library written in Python partially & in C or C++ for faster computations


==> Installation of NumPy:- (External-Library)
= Python and PIP should be already installed
= Next install NumPy
= Command goes like this,
cmd> pip install numpy		
(latest-version is numpy-1.23.3) -> Python-3.10.7
(internet-conn is compulsory)

NOTE:-(How to use NumPy in program?)
import numpy;


# //Program... (NumpyEx1.py)
#Program to work with NumPy module
import numpy;
arr = numpy.array([1, 2, 3, 4, 5]);
print(arr);

NOTe::-
= NumPy-Arrays are represented in [] brackets w.o ,(commas)

NOTE:-
= How to get numpy-version,
//Program... (NumpyEx1.py)
import numpy as np;
print(np.__version__);

==>How to Create a NumPy ndarray:-
= NumPy is used to work with arrays
= In NumPy, it is called ndarray
(it is done by using the array() function)
Ex:-
//Program... (NumpyEx1.py)
import numpy as np;
arr = np.array([11, 22, 33, 44, 55]);
print(arr);
print(type(arr));

NOTE:-
= To create an ndarray, we can pass a list[], tuple(),set{} or any array-like object into the array() method and it is converted into "ndarray"

Ex:- (NumpyEx1.py)
import numpy as np;
arr = np.array((11,12,13,14,15));	//[list],(tuple),{set}
print(arr);
'''

##Program... (NumpyEx1.py)
#Program to work with NumPy module (NumpyEx1.py)


import numpy;
arr = numpy.array([10, 20, 30, 40, 50]);
print(arr);
print(type(arr));
'''

'''
import numpy as np;
print(np.__version__);



import numpy as np;
arr = np.array({11,12,13,14,15});	#[list],(tuple),{set}
print(arr);
print(type(arr));



'''
==> NumPy Array Dimensions:- (0D/1D/2D/3D etc)
1) 0-D Arrays:-
= 0-D Arrays(Scalars), are the elements in an array
= Each value in an array is a 0-D array

Ex:- (NumpyEx2.py)
#Program to Create a Dimensional-Array (0D/1D/2D/3D etc)
#0D Array
import numpy as np;
arr = np.array(11);	
print(arr);
print(type(arr));

2) 1-D Arrays:-
= An array which has 0-D arrays as its elements is called Single/Uni-dimensional or 1-D array

Ex:- (NumpyEx2.py)
#1D Array
import numpy as np;
arr = np.array([15, 25, 35, 45, 55]);
print(arr);
print(type(arr));


3) 2-D Arrays:-
= An array that has 1-D arrays as its elements is called a 2-D array
(Mainly used to Tables(rows&cols), Matrices etc)

Ex:- (NumpyEx2.py)
#2D Array
import numpy as np;
arr = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]]);
print(arr);
print(type(arr));

=** Each array-represents 1-row & values as cols-elements

4) 3-D arrays:-
= An array that has 2-D arrays (matrices) as its elements is called 3-D array

Ex:- (NumpyEx2.py)
#3D Array
import numpy as np;
arr = np.array([ [[11,22,33],[44,55,66]], [[10,20,30],[40,50,60]] ]);
print(arr);
print(type(arr));

NOTE:-
=> How to Check Array-Dimensions?
= "ndim" attribute gives array-dimension (numpy-module)
Ex:- (NumpyEx2.py)
#ndim Array
import numpy as np;
arr1 = np.array(11);	
arr2 = np.array([15, 25, 35, 45, 55]);
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]]);
arr4 = np.array([ [[11,22,33],[44,55,66]], [[10,20,30],[40,50,60]] ]);
print(arr1.ndim);
print(arr2.ndim);
print(arr3.ndim);
print(arr4.ndim);


#Program to Create a Dimensional-Array (0D/1D/2D/3D etc)
#NumPyEx2.py

'''
#0D Array
import numpy as np;
arr = np.array(11);	
print(arr);
print(type(arr));
'''

'''
#1D Array
import numpy as np;
arr = np.array([15, 25, 35, 45, 55]);
print(arr);
print(type(arr));
'''

'''
#2D Array (rows & cols)
import numpy as np;
arr = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]]); #nested-lists
print(arr);
print(type(arr));
'''

'''
#3D Array
import numpy as np;
arr = np.array([ [[11,22,33],[44,55,66]], [[10,20,30],[40,50,60]] ]);
print(arr);
print(type(arr));
'''

'''
#ndim-var Array
import numpy as np;
arr1 = np.array(11);	
arr2 = np.array([15, 25, 35, 45, 55]);
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]]);
arr4 = np.array([ [[11,22,33],[44,55,66]], [[10,20,30],[40,50,60]] ]);
print(arr1.ndim);
print(arr2.ndim);
print(arr3.ndim);
print(arr4.ndim);
'''

#n-Dimension
import numpy as np;
arr = np.array([1, 2, 3, 4], ndmin=5);
print(arr);
print(arr.ndim);



******
==> Accessing NumPy Array Elements:-
(Using-Indexes)
= NumPy Array-indexing is same as any array
i.e, 0 to (n-1)	(F->L) Forward-direction
-1 to -n	(L->F) Backward-direction

Ex:- (NumpyEx3.py)
#NumPy Array Accessing-Elements(with Indexes)
import numpy as np;
arr = np.array([11, 22, 33, 44, 55]);
print(arr[0]);
print(arr[1]);
print(arr[2]);
print(arr[3]);
print(arr[4]);
print(arr[-1]);
print(arr[-2]);
print(arr[-3]);
print(arr[-4]);
print(arr[-5]);

=** The best-way to access the elements of array is Loops
(for-Loop)
Ex:-
#loops access
for x in arr:
	print(x);
i=0;
while i<len(arr):
	print(arr[i]);
	i=i+1;

=* len(arr) function gives length of an NumPy-array


=> Accessing 2-D Arrays with Indexes:-
= It is done with comma separated integers representing the dimension and the index of the element
Ex:-
	arr[0,0]	or a[0][0]
	arr[1,1]	or a[1][1]
	arr[2,2]	or a[2][2]
	
Ex:- (NumpyEx3.py)
#Access 2D Arrays with indexes arr[i,j] or arr[i][j]
import numpy as np;
arr = np.array([ [1,2,3], [4,5,6], [7,8,9] ]);
print(arr);
print(arr[0,0],"\t",arr[0,1],"\t",arr[0][2]);	#1st-row
print(arr[1,0],"\t",arr[1,1],"\t",arr[1][2]);	#2nd-row
print(arr[2,0],"\t",arr[2,1],"\t",arr[2][2]);	#3rd-row

#with Nested-Loops
i=0;
while i<3:
	j=0;
	while j<3:
		print(arr[i][j],end="\t");		#arr[i,j]
		j=j+1;
	print();
	i=i+1;
	
NOTE:-
= Similarly we can work with 3-D and n-D arrays
Ex:-
	arr[0,0,0]	or arr[0][0][0]
= Also we can use -ve indexes for accessing 2D or 3D or n-D arrays
Ex:- (NumpyEx3.py)
#-ve indexes
import numpy as np;
arr = np.array([[1,2,3],[4,5,6]])
print(arr[1,-1]);	#2nd-row, last-element
print(arr[-1][-3]);	#2nd-row, 1st-element
'''

#NumPy Array Accessing-Elements(with Indexes) 
#(NumpyEx3.py)


import numpy as np;
arr = np.array([11, 22, 33, 44, 55]);
print(arr[0]);
print(arr[1]);
print(arr[2]);
print(arr[3]);
print(arr[4]);
print(arr[-1]);
print(arr[-2]);
print(arr[-3]);
print(arr[-4]);
print(arr[-5]);

print()
#loops access
for x in arr:
	print(x);

print();	
i=0;
while i<len(arr):
	print(arr[i]);
	i=i+1;
'''
	
'''
#Access 2D Arrays with indexes arr[i,j] or arr[i][j]
import numpy as np;
arr = np.array([ [1,2,3], [4,5,6], [7,8,9] ]);
print(arr);
print(arr[0,0],"\t",arr[0,1],"\t",arr[0][2]);	#1st-row
print(arr[1,0],"\t",arr[1,1],"\t",arr[1][2]);	#2nd-row
print(arr[2,0],"\t",arr[2,1],"\t",arr[2][2]);	#3rd-row

print()
#with Nested-Loops
i=0;
while i<3:
	j=0;
	while j<3:
		print(arr[i][j],end="\t");		#arr[i,j]
		j=j+1;
	print();
	i=i+1;
	


#-ve indexes
import numpy as np;
arr = np.array([[1,2,3],[4,5,6]])
print(arr[1,-1]);	#2nd-row, last-element
print(arr[-1][-3]);	#2nd-row, 1st-element

	
'''	
***==> NumPy Array Slicing:-
= Slicing arrays means taking elements from one given index to another given index
= It is done as follow [start:end]	#end-index-value not included
= It can have step-value also, Ex:- [start:end:step]
= default-start-value(0)
= default-end-value(length-of-array)
= default-step-value (+1)

Ex:- (NumpyEx4.py)
#NumPy-array Slicing
import numpy as np;
arr = np.array([11,22,33,44,55,66,77,88]);
print(arr[1:5]);
print(arr[4:]);
print(arr[:4]);
#-ve slicing
print(arr[-3:-1]);
#step-value
print(arr[1:5:2]);
print(arr[::2]);
	
	
=> 2D-Array Slicings:-
= Here we use arr[b:e:s][b:e:s] or arr[b:e:s, b:e:s]
Ex:-(NumpyEx4.py)
#2D Array-Slicings
import numpy as np;
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]]);
print(arr[1, 0:2]);
print(arr[0:2,2]);
print(arr[0:2, 1:4]);


#Program to work with NumPy-array Slicings
#NumpyEx4.py


'''
#NumPy-array Slicing
import numpy as np;
arr = np.array([11,22,33,44,55,66,77,88]);
print(arr[1:5]);
print(arr[4:]);
print(arr[:4]);
#-ve slicing
print(arr[-3:-1]);
#step-value
print(arr[1:5:2]);
print(arr[::2]);


#2D Array-Slicings
import numpy as np;
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]]);
print(arr[1, 0:2]);
print(arr[0:2,2]);
print(arr[0:2, 1:4]);


'''
====================================================================
==>> Pandas in Python:-  (Tables & its columns-data)
= Pandas is a Python library, it is mainly used to "ANALYZE-Data"
(Data-Analysis)
= It is a Module (pandas)
= It is used as follows,
Ex:-
	import pandas as pd;
	pd.methodName()....;
	
NOTE::-
==> What?
= Pandas is a Python library, which is used to work with data-sets (records or table-data)
= It provides functions for,
	data-analysis, 
	data-cleaning, 
	data-exploring, 
	data-manipulations

= "Panel-Data" + "Python Data Analysis" ==> Pandas
= It was developed by "Wes McKinney"(2008)

=> Advantage,
	= Analyze big data and make conclusions (statistical theories)
	= Cleans confusion in data, and make them easy to work
	= Such data is use in data-science

Example::-
= Pandas provide correlation between 2 or more columns in a table-data
(i.e, Average/Max/Min value etc)
= Pandas can delete rows in table that are of no-use, or has wrong value (empty or NULLs) --> "Pandas-Data-Cleaning"


==> How to install Pandas??
= Make-sure to have python & pip already installed in your system & give the below,
cmd> pip install pandas
pandas-1.4.4

**(py -m pip install --upgrade pip)


Ex:-
//Program (PythonPandasEx1.py)
(Program to demo Pandas usage in python)
#Program to demo Pandas usage in python 
#(PythonPandasEx1.py)

'''
#data as dict-type using DataFrame() method
import pandas;
data1 = {
  'names': ["Sai", "Ram", "Ali"],
  'ages': [23, 27, 20],
  "heights" :[6.2, 6.4, 5.9]
};
newpandasdata1 = pandas.DataFrame(data1);
print(newpandasdata1);
'''

'''
print();
#import alias
import pandas as pd;
data1 = {
  'names': ["Sai", "Ram", "Ali","Krishna"],
  'ages': [23, 27, 20,24],
  "heights" :[6.2, 6.4, 5.9,5.5]
};
newpandasdata1 = pd.DataFrame(data1);
print(newpandasdata1);



print();
#pandas __version__
import pandas as pd;
print(pd.__version__);



'''
==>>> Pandas Series::- (table-column-data)
= Pandas Series is like a data in a table-columns
= It is coll.of.data like 1D-array (any type)
= In "pandas" module we have "Series()" method, to form a Pandas-series
Ex:-
//Program (PythonPandasEx2.py)
(Program to demo Pandas series using Series() method)
##Program (PythonPandasEx2.py)
#Program to demo Pandas series using Series() method

'''
#series from a list
import pandas as pd;
list1 = [11,88,55,22,99];
x = pd.Series(list1);
print(x);

#labels(indexes)
print(x[0]);
print(x[1]);
print(x[2]);
print(x[3]);
print(x[4]);


#own labels (row-names)
import pandas as pd;
list1 = [11,88,55,22,99];
x = pd.Series(list1,index=["a","b","c","d","e"]);
print(x);
print(x["a"]);
print(x["b"]);
print(x["c"]);
print(x["d"]);
print(x["e"]);

'''
NOTE:-
=> Pandas-Series "Labels":-
= The values of Pandas-Series are labeled with index number (0 to n-1)
Ex:- 0,1,2,...etc
= Label can be used to access Pandas-Series values
Ex:-
	x[0], x[1],....
	
=> Create labels?
= It is done with index=[....] argument to Series() method
Ex:-
x = pd.Series(list1, index=["a","b",....]);
(here we can have our own indexes to Pandas-Series values)
= Access with our own labels,
Ex:-
	x["a"], x["b"],....




==> Pandas Series with (Key:Value) pairs::-
= We can have, Key:Value pair Objects as Pandas-Series
(for this, we can use dictionary type)
Ex:-
students_data = {1001:"Sai", 1002:"Ram", 1003:"Ali"};

//Program (PythonPandasEx3.py)
(Program to demo Pandas series with (Key:Value) pairs of dict-type)
#Program (PythonPandasEx3.py)
#Program to demo Pandas series with (Key:Value) pairs of dict-type

'''
import pandas as pd;
students_data = {1001:"Sai", 1002:"Ram", 1003:"Ali"};
x = pd.Series(students_data);
print(x);

print();
#keys as labels(indexes)
print(x[1001]);
print(x[1002]);
print(x[1003]);
#print(x[1004]);	#KeyError


print();
#Series with specific elements of dictionary
import pandas as pd;
students_data = {1001:"Sai", 1002:"Ram", 1003:"Ali"};
x = pd.Series(students_data, index=[1001,1003]);
print(x);


'''
NOTE:-
= Here dict-type "keys" are taken as labels(indexes) for Pandas-Series values
= such keys can be used to access individual values of Pandas-Series
Ex:-
	x[1001], x[1002],...

**=> Here we can include only specific elements of a dictionary as Pandas-Series values using index=[...] argument to Series() method
Ex:-
x = pd.Series(students_data, index=[1001,1003]);
 


*** (Pandas DataFrames)
===>> Pandas-Series DataFrames::-
= Data sets in Pandas are multi-dimensional tables, known as DataFrames
= Series is like a column & DataFrame is like a whole table
=** For this, we use DataFrame() method
Ex:-
students_data={
	"rollno":[1001,1002,1003],
	"names":["Sai","Ram","Ali"]
};
#pd.DataFrame(students_data);

//Program (PythonPandasEx4.py)
(Program to demo Pandas series with DataFrames)
#Program to demo Pandas series with DataFrames
#PythonPandasEx4.py

'''
#Series with DataFrames
import pandas as pd;
students_data={
	"rollno":[1001,1002,1003],
	"names":["Sai","Ram","Ali"]
};
x = pd.Series(students_data);
print(x);
print();
x = pd.DataFrame(students_data);
print(x);


#Locating Row loc[index]
print();
df = pd.DataFrame(students_data);
print(df.loc[0]);
print();
print(df.loc[1]);
print();
print(df.loc[2]);
#print(df.loc[3]);


print();
#with list of indexes(sub-list)
print(df.loc[[0,1,2]]);
print(df.loc[[0,1]]);
print(df.loc[[0]]);
#print(df.loc[[0,1,2,3]]);



print();
#Named-indexes
import pandas as pd;
students_data={
	"rollno":[1001,1002,1003],
	"names":["Sai","Ram","Ali"]
};
df = pd.DataFrame(students_data, index=["Stud1", "Stud2", "Stud3"]);
print(df);

print();
print(df.loc["Stud1"]);
print(df.loc["Stud2"]);
print(df.loc["Stud3"]);
#print(df.loc["Stud4"]);

'''
NOTE:-
= Pandas DataFrame is a 2D data structure, same-like a 2D-array, or a table with rows and columns

=> Pandas DataFrame Locate-Rows:-
(working with rows)
= To get rows from Pandas DataFrame, we use "loc" attribute
(it gives specified rows with given index(0 to n-1))
Ex:-
df = pd.DataFrame(students_data);
	df.loc[0];
	df.loc[1];
	df.loc[2];
	#df.loc[3];		#ValueError & KeyError

//Program (PythonPandasEx4.py) ==SAME==
(Program to demo Pandas series with DataFrames)

Ex:- (list of indexes)
df.loc[[0,1,2]];
=** Here result is Pandas DataFrame (using [list-of-indexes])


=> Named indexes::-
= using index="" attribute for DataFrame() method, we can give our own indexes to Pandas-DataFrame
Ex:-
df = pd.DataFrame(students_data, index = ["Stud1", "Stud2", "Stud3"]);
print(df);

=** instead of indexes(0,1,2,...), we get (Stud1,Stud2,Stud3)

=> Locate-Row with Named Indexes::-
= Use "loc" attribute to get the specified row with attribute-name
Ex::-
print(df.loc["Stud1"]);
print(df.loc["Stud2"]);
print(df.loc["Stud3"]);
#print(df.loc["Stud4"]);	#KeyError



==>> Pandas with CSV files:-
(Reading data from CSV files)
= Pandas provide functions using with we can work with Big Data-Sets like CSV files (comma separated values)
Ex:-
RollNo,Name,Age,Height
1001,Sai,21,6.2
1002,Ram,22,5.9
1003,Ali,23,5.5
1004,John,20,6
1005,Krishna,24,5.1
1006,Tom,21,5.2
1007,Anup,19,5.8
1008,Sita,18,5.6
1009,Kishore,24,5.4
1010,Pavan,20,5.5

= CSV files contains plain-text with data-sets
Ex:-
	student_data.csv
	employee_data.csv
	
=** to read data from CSV files, we use read_csv() function from pandas-module

Ex:-
import pandas as pd;
df = pd.read_csv("student_data.csv")
print(df);
print(df.to_string());


#Program (PythonPandasEx5.py)
#Program to demo Pandas series with CSV files

import pandas as pd;
df = pd.read_csv("student_data.csv")
print(df);		
print(type(df));
print();
print(df.to_string());
print(type(df.to_string()));

print();



==>> Pandas with JSON files:-
(Reading data from JSON files)
(Javascript Object-notation i.e, dict-data)
= Storing Big-data in the form of Key:Value pairs is done with JSON
Ex:-
"student_data.json" 
{
	"rollno" : {"0":1001,"1":1002,"2":1003},
	"sname" : {"0":"Sai","1":"Ram","2":"Ali"},
	"age" : {"0":21,"1":"23","2":"20"},
	"height" : {"0":6.2,"1":"5.5","2":"5.9"},
	"address" : {"0":"hyderabad","1":"Secbad","2":"Hitech"}
}

= JSON is a plain-text data-set, it is javascript object {....}
= It is used as a Data-transfer from server to client Ui-Apps
(partial page updates)


=** To read data from JSON files, we use read_json() function from pandas-module
Ex:-
import pandas as pd;
df = pd.read_json("student_data.json");
print(df);
print(type(df));
print(df.to_string());


//Program (PythonPandasEx6.py)
(Program to demo Pandas series with JSON files)

=> If .json file is not available, then we can use python "dict" variable in program to read json-data
(for this we use DataFrame() function)
Ex:-
student_data = {
	"rollno" : {"0":1001,"1":1002,"2":1003},
	"sname" : {"0":"Sai","1":"Ram","2":"Ali"},
	"age" : {"0":21,"1":"23","2":"20"},
	"height" : {"0":6.2,"1":"5.5","2":"5.9"},
	"address" : {"0":"hyderabad","1":"Secbad","2":"Hitech"}
};
df = pd.DataFrame(student_data);


#Program to demo Pandas series with JSON files 
#(PythonPandasEx6.py)

'''
import pandas as pd;
df = pd.read_json("student_data.json");
print(df);
print(type(df));
print();
print(df.to_string());



print();
#dict-data as json-data
import pandas as pd;
student_data = {
	"rollno" : {"0":1001,"1":1002,"2":1003},
	"sname" : {"0":"Sai","1":"Ram","2":"Ali"},
	"age" : {"0":21,"1":23,"2":20},
	"height" : {"0":6.2,"1":5.5,"2":5.9},
	"address" : {"0":"hyderabad","1":"Secbad","2":"HitechCity"}
};
df = pd.DataFrame(student_data);
print(df);



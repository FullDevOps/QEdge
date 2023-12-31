#40th day 09-12-22
'''
==>> SciPy(SciKit) Arrays in Python:-
(Data-Science Module)
= SciPy stands for Scientific Python
= SciPy is a scientific calculation library that internally uses NumPy only


==> SciPy Introduction::-
= SciPy is a scientific calculations library, which uses NumPy only
= SciPy stands for Scientific Python (SciKit)
= SciPy is open-source module (python-lib)
=**
	SciPy was invented by "Travis Olliphant" (same for NumPy)

=> Why SciPy?
= It gives more optimized functions than NumPy library
= SciPy is written in Python only


==>> How to install SciPy module??
(pre-requisites)
= Makesure Python & Pip are already installed in system
cmd> pip install scipy

#Program (PythonSciPyEx1.py)
(Program to demo SciPy module)
#Program to demo SciPy module (PythonSciPyEx1.py)

from scipy import constants;
print(constants.liter);		#1-liter as cubic-meters (mathematical-constants)

import scipy;
print(scipy.__version__);



==> Working with SciPy Constant Units::-
= SciPy provides built-in scientific constants
Ex::-
	pi
Ex:-
from scipy import constants;
print(constants.pi);

#Program (PythonSciPyEx2.py)
(Program to demo SciPy module with Constants)

=> listing all constants units,
Ex:-
dir(constants);
print(constants.year);
print(constants.week);
etc...

NOTE:-
=> Unit Categories (for all Constants)
(Metric,Binary,Mass,Angle,Time,Length,Pressure,Area,Volume,Speed,Temperature,Energy,Power,Force)
'''

#Program to demo SciPy module with Constants
#Program (PythonSciPyEx2.py)

from scipy import constants;
print(constants.pi);

print();
print(dir(constants));

print();
print(constants.e);	
print(constants.kilo);	
print(constants.gram);	

print(constants.hour);
print(constants.minute);

print(constants.mile);
print(constants.day);

print(constants.carat);
print(constants.week);

print(constants.speed_of_sound);
print(constants.speed_of_light);

print(constants.sigma);


'''
==> Working with SciPy Optimizers::-
= Optimizers are set of procedures defined in SciPy 
Ex:-  	finding the min-value of a function
		getting root of mathematical equations
		etc..

=> Root of Equation::-
= In NumPy, we can get root for polynomials or linear equations
(but it does not have root for non linear equations)
Ex:-
	x + sin(x)

=** For this, we can use SciPy "optimze.root" function
Ex:-
	root(equation-function,x)
	
equation-function (represents an non-linear equations as return-value)
x -> initial guess for the root-value of equation

NOTE::-
= For SciPy Optimizers, we use "scipy.optimize" module

#Program (PythonSciPyEx3.py)
(Program to demo SciPy module with Optimizers)
#Program (PythonSciPyEx3.py)
#Program to demo SciPy module with Optimizers

from scipy.optimize import root;
from math import cos;

def equation(x):
	return x + cos(x);

rootresult = root(equation,0);
print(rootresult.x);
print(rootresult)


================================================================================================================================
==>> MatPlotLib in Python:- (Mathematical-Graphs)

=> What is Matplotlib?
= Matplotlib is graphs-plotting library in python
= It provides visualization of data
= Matplotlib was created by John D. Hunter
(open-source lib)
= It is mojorly written in python and minorly written in C, Objective-C and Javascript

=> Matplotlib Codebase?
= Source-Code for Matplotlib is in github repository https://github.com/matplotlib/matplotlib


==> Installation of Matplotlib:-
= Make sure Python and PIP are already installed in your system
= Next, install Matplotlib

[CMD> pip install matplotlib]

NOTE:-
= Alternatively, use python-distributions like Anaconda, Spyder etc, that already has Matplotlib in-built


==> Working with MatPlotLib in Programs::-
= for this, we use import statement,
Ex:-
	import Matplotlib;

##Program (MatPlotLibEx1.py)
import matplotlib
print(matplotlib.__version__);



==> Pyplot sub-module::-
= Matplotlib utilities are given under the pyplot sub-module
= It is usaully imported as "plt" alias
Ex:-
	import matplotlib.pyplot as plt;

##Program (MatPlotLibEx2.py)
#Draw a line in a diagram from position (0,0) to position (5,200)

import matplotlib.pyplot as plt;
import numpy as np;

xpoints = np.array([0, 5]);
ypoints = np.array([0, 200]);

plt.plot(xpoints, ypoints);
plt.show();


=> Plotting x and y points on graph::-
= For this plot() function is used to draw points in a graph
= By default, the plot() function draws a line from point to point
Syntax::-
	plt.plot(xpoints, ypoints);
(xpoints is an array with x-axis points)
(ypoints is an array with y-axis points)
Ex:-
	For plottin a line from (1, 1) to (10, 10), pass two arrays [1, 10] and [1, 10]
'''
##Program (MatPlotLibEx2.py) ==SAME-Prog==
#Draw a line in a diagram from position (1,1) to position (10,10)

import matplotlib.pyplot as plt;
import numpy as np;

xpoints = np.array([1,10]);
ypoints = np.array([1,10]);

plt.plot(xpoints, ypoints)
plt.show();


# ==> Plotting Without Line::-
# = To plot only markers, we use string-notation as parameter 'o', it means 'rings'

##Program (MatPlotLibEx2.py) ==SAME-Prog==
#Draw two points in the diagram, one at position (1,1) and one in position (8,8)

import matplotlib.pyplot as plt;
import numpy as np;

xpoints = np.array([1,8]);
ypoints = np.array([1,8]);

plt.plot(xpoints, ypoints, 'o');
plt.show();


# ==> Plotting with Multiple Points::-
# = We can plot as many points as required, but make sure we have same number of points in both the axis

##Program (MatPlotLibEx2.py) ==SAME-Prog==
#Draw a line in a diagram from position (1, 1) to (3,6) then to (5,1) and finally (8,8)

import matplotlib.pyplot as plt;
import numpy as np;

xpoints = np.array([1,3,5,8]);
ypoints = np.array([1,6,1,8]);

plt.plot(xpoints,ypoints);
plt.show();


# ==> Default X-Points::-
# = If we do not specify the x-axis points, then it will take default values as 0,1,2,3,4,.... etc. depending on the length of the y-axis-points
# (The x-points are [0, 1, 2, 3, 4, 5])

##Program (MatPlotLibEx2.py) ==SAME-Prog==
#Plotting without x-axis-points

import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints);
plt.show();


# (***)
# ==>>> Matplotlib Markers::-
# = We can use the argument/para "marker='o'", to mark each point in a graph with a specified marker

##Program (MatPlotLibEx3.py)
#Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints, marker = 'o');
plt.show();

'''
NOTE:-
**= Some Pre-defined Marker References:-
Marker	Description
--------------------
'o'		Circle	
'*'		Star	
'.'		Point	
','		Pixel	
'x'		X	
'X'		X (filled)	
'+'		Plus	
'P'		Plus (filled)	
's'		Square	
'D'		Diamond	
'd'		Diamond (thin)	
'p'		Pentagon	
'H'		Hexagon	
'h'		Hexagon	
'v'		Triangle Down	
'^'		Triangle Up	
'<'		Triangle Left	
'>'		Triangle Right	
'1'		Tri Down	
'2'		Tri Up	
'3'		Tri Left	
'4'		Tri Right	
'|'		Vline	
'_'		Hline



==> Format Strings fmt:-
= We can also use the shortcut string notation parameter to specify the marker
= This parameter is also called fmt, it is written as follows,
"marker|line|color"
'''
##Program (MatPlotLibEx3.py)
#Mark each point with a circle:(using fmt)

import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints, 'o:r');
plt.show();

'''
NOTE:-
= Some pre-defined Line References are,
Line-Syntax		Description
-------------------------------------
'-'				Solid-line	
':'				Dotted-line	
'--'			Dashed-line	
'-.'			Dashed/dotted-line	
-------------------------------------

= Some Color References are,
Color-Syntax	Description
-------------------------------------
'r'				Red	
'g'				Green	
'b'				Blue	
'c'				Cyan	
'm'				Magenta	
'y'				Yellow	
'k'				Black	
'w'				White
-------------------------------------
'''

# ==> Marker Size::-
# = Here we use the argument/para markersize(ms) to set the size of the markers

##Program (MatPlotLibEx3.py)
#Set the size of the markers to 15:

import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints, marker = 'o', ms = 15);
plt.show();


# ==>Marker Color::-
# = Here we can use the argument/para markeredgecolor(mec) to set the color for edge of the markers

##Program (MatPlotLibEx3.py)
#Set the EDGE color to red

import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints, marker = 'o', ms = 15, mec = 'r');
plt.show();


# NOTE:-
# = We can also use the argument/para markerfacecolor(mfc) to set the color inside the edge of the markers

##Program (MatPlotLibEx3.py)
#Set the FACE color to red

import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints, marker='o', ms=20, mfc='r');
plt.show();


# NOTE:-
# = We can use both mec and mfc arguments/para to color of the entire marker

##Program (MatPlotLibEx3.py)
#Set the color of both the edge and the face to red

import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 5, 1, 8, 3, 4]);

plt.plot(ypoints, marker='o', ms=15, mec='r', mfc='r');
plt.show();

'''
NOTE:-
= We can also use Hexadecimal-color-values or color-names,
Ex:-
plt.plot(ypoints, marker='o', ms=15, mec='#4CAF50', mfc='coral');
= Other hexa-values & color-names are,(140)
AliceBlue
#F0F8FF
AntiqueWhite
#FAEBD7
Aqua
#00FFFF
Aquamarine
#7FFFD4
Azure
#F0FFFF
Beige
#F5F5DC
Bisque
#FFE4C4
Black
#000000
BlanchedAlmond
#FFEBCD
Blue
#0000FF
BlueViolet
#8A2BE2
Brown
#A52A2A
BurlyWood
#DEB887
CadetBlue
#5F9EA0
Chartreuse
#7FFF00
Chocolate
#D2691E
Coral
#FF7F50
CornflowerBlue
#6495ED
Cornsilk
#FFF8DC
Crimson
#DC143C
Cyan
#00FFFF
DarkBlue
#00008B
DarkCyan
#008B8B
DarkGoldenRod
#B8860B
DarkGray
#A9A9A9
DarkGrey
#A9A9A9
DarkGreen
#006400
DarkKhaki
#BDB76B
DarkMagenta
#8B008B
DarkOliveGreen
#556B2F
DarkOrange
#FF8C00
DarkOrchid
#9932CC
DarkRed
#8B0000
DarkSalmon
#E9967A
DarkSeaGreen
#8FBC8F
DarkSlateBlue
#483D8B
DarkSlateGray
#2F4F4F
DarkSlateGrey
#2F4F4F
DarkTurquoise
#00CED1
DarkViolet
#9400D3
DeepPink
#FF1493
DeepSkyBlue
#00BFFF
DimGray
#696969
DimGrey
#696969
DodgerBlue
#1E90FF
FireBrick
#B22222
FloralWhite
#FFFAF0
ForestGreen
#228B22
Fuchsia
#FF00FF
Gainsboro
#DCDCDC
GhostWhite
#F8F8FF
Gold
#FFD700
GoldenRod
#DAA520
Gray
#808080
Grey
#808080
Green
#008000
GreenYellow
#ADFF2F
HoneyDew
#F0FFF0
HotPink
#FF69B4
IndianRed
#CD5C5C
Indigo
#4B0082
Ivory
#FFFFF0
Khaki
#F0E68C
Lavender
#E6E6FA
LavenderBlush
#FFF0F5
LawnGreen
#7CFC00
LemonChiffon
#FFFACD
LightBlue
#ADD8E6
LightCoral
#F08080
LightCyan
#E0FFFF
LightGoldenRodYellow
#FAFAD2
LightGray
#D3D3D3
LightGrey
#D3D3D3
LightGreen
#90EE90
LightPink
#FFB6C1
LightSalmon
#FFA07A
LightSeaGreen
#20B2AA
LightSkyBlue
#87CEFA
LightSlateGray
#778899
LightSlateGrey
#778899
LightSteelBlue
#B0C4DE
LightYellow
#FFFFE0
Lime
#00FF00
LimeGreen
#32CD32
Linen
#FAF0E6
Magenta
#FF00FF
Maroon
#800000
MediumAquaMarine
#66CDAA
MediumBlue
#0000CD
MediumOrchid
#BA55D3
MediumPurple
#9370DB
MediumSeaGreen
#3CB371
MediumSlateBlue
#7B68EE
MediumSpringGreen
#00FA9A
MediumTurquoise
#48D1CC
MediumVioletRed
#C71585
MidnightBlue
#191970
MintCream
#F5FFFA
MistyRose
#FFE4E1
Moccasin
#FFE4B5
NavajoWhite
#FFDEAD
Navy
#000080
OldLace
#FDF5E6
Olive
#808000
OliveDrab
#6B8E23
Orange
#FFA500
OrangeRed
#FF4500
Orchid
#DA70D6
PaleGoldenRod
#EEE8AA
PaleGreen
#98FB98
PaleTurquoise
#AFEEEE
PaleVioletRed
#DB7093
PapayaWhip
#FFEFD5
PeachPuff
#FFDAB9
Peru
#CD853F
Pink
#FFC0CB
Plum
#DDA0DD
PowderBlue
#B0E0E6
Purple
#800080
RebeccaPurple
#663399
Red
#FF0000
RosyBrown
#BC8F8F
RoyalBlue
#4169E1
SaddleBrown
#8B4513
Salmon
#FA8072
SandyBrown
#F4A460
SeaGreen
#2E8B57
SeaShell
#FFF5EE
Sienna
#A0522D
Silver
#C0C0C0
SkyBlue
#87CEEB
SlateBlue
#6A5ACD
SlateGray
#708090
SlateGrey
#708090
Snow
#FFFAFA
SpringGreen
#00FF7F
SteelBlue
#4682B4
Tan
#D2B48C
Teal
#008080
Thistle
#D8BFD8
Tomato
#FF6347
Turquoise
#40E0D0
Violet
#EE82EE
Wheat
#F5DEB3
White
#FFFFFF
WhiteSmoke
#F5F5F5
Yellow
#FFFF00
YellowGreen
#9ACD32



==>> Matplotlib Lines::-
==> Linestyle:-
= We can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line
'''
##Program (MatPlotLibEx4.py)

#Use a dotted line
import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 8, 3, 6, 1, 9]);

plt.plot(ypoints, linestyle='dotted');
plt.show();

'''
NOTE:-
=> Using a dashed-line,
Ex:-
	plt.plot(ypoints, linestyle = 'dashed')
##Program (MatPlotLibEx4.py)	
	
=> Short-way Syntax,
Syntax:-
	linestyle as ls
	dotted as :
	dashed as --
Ex:-
	plt.plot(ypoints, ls=':');
##Program (MatPlotLibEx4.py)

=> Other Line Styles,
Ex:-
'solid' (default)	'-'	
'dotted'			':'	
'dashed'			'--'	
'dashdot'			'-.'	
'None'				'' or ' '	
##Program (MatPlotLibEx4.py)


=> Line Color:-
= We can use the argument color or short-way (c) to set the color of line
Ex:-'''

##Program (MatPlotLibEx4.py)
#Set the line color to red

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([2, 8, 3, 6, 1, 9]);

plt.plot(ypoints, color = 'r')
plt.show()	

'''
NOTE:-
= We can also use hexadecimal-values
Ex:-
	plt.plot(ypoints, c='#4CAF50');


==> Line-width::-
= We can use argument linewidth or (lw) to change the width of the line
= Its value is floating number, in points
'''
##Program (MatPlotLibEx4.py)
##Line Width
import matplotlib.pyplot as plt;
import numpy as np;

ypoints = np.array([2, 8, 3, 6, 1, 9]);

plt.plot(ypoints, linewidth = '5.4');
plt.show();


# ==> Multiple Lines Plotting::-
# = We can plot as multiple-lines as per requirement by adding multiple plt.plot() functions in code
# Ex:-
##Program (MatPlotLibEx4.py)
#Draw two lines by specifying a plt.plot() function for each line
import matplotlib.pyplot as plt;
import numpy as np;

y1 = np.array([2, 8, 3, 6, 1, 9]);
y2 = np.array([1, 6, 2, 5, 1, 8]);

plt.plot(y1, c='r');
plt.plot(y2, c='g');

plt.show();


# NOTE:-
# = Here we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3)
# = We can use both x-axis-points and y-axis-points for multiple-line plotting

# Ex:-
##Program (MatPlotLibEx4.py)
#plotting with both x-axis-points & y-axis-points
import matplotlib.pyplot as plt;
import numpy as np;

x1 = np.array([0, 1, 2, 3, 4, 5]);
y1 = np.array([2, 8, 3, 6, 1, 9]);

x1 = np.array([0, 1, 2, 3, 4, 5]);
y2 = np.array([1, 6, 2, 5, 1, 8]);

plt.plot(x1, y1, x2, y2);
plt.show();



# ==>> Matplotlib Labels and Title::-
# = For this, we use the xlabel() and ylabel() functions to set a label for the x-axis and y-axis

##Program (MatPlotLibEx5.py)
#Adding labels for x-axis and y-axis

import numpy as np;
import matplotlib.pyplot as plt;

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

plt.plot(x,y);

plt.xlabel("Roll-Numbers");
plt.ylabel("Student-Ages");

plt.show();



# ==> Create a Title for a Graph(Plot)::-
# = For this, we use title() function to set a title for the plot/graph

##Program (MatPlotLibEx5.py)
#Add a graph/plot title and labels for x-axis and y-axis

import numpy as np;
import matplotlib.pyplot as plt;

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

plt.plot(x,y);

plt.title("Student-Details/Report-Card");
plt.xlabel("Roll-Numbers");
plt.ylabel("Student-Ages");

plt.show();



# ==> Set Font Properties for Title and Labels::-
# = For this, we use the fontdict="" parameter in xlabel(), ylabel(), and title() functions to set font properties for the title and labels

##Program (MatPlotLibEx5.py)
#Set font properties for the title and labels

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

font1 = {'family':'Courier','color':'Red','size':23};
font2 = {'family':'Courier','color':'Maroon','size':17};

plt.plot(x,y);

plt.title("Student-Details/Report-Card",fontdict=font1);
plt.xlabel("Roll-Numbers",fontdict=font2);
plt.ylabel("Student-Ages",fontdict=font2);

plt.show();


'''
==> Position the Title::- (left/right/center)
= Here we can use the loc parameter in title() function to position the title
= Accepted-values are: left/right/center
= Default value is "center"
'''
##Program (MatPlotLibEx5.py)
#Position the title to the left:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

plt.title("Student-Details/Report-Card",loc="left");
plt.xlabel("Roll-Numbers");
plt.ylabel("Student-Ages");

plt.plot(x,y);
plt.show();


# (***)
# ==>> MatPlotLib Grids:::- 
# = For this, we use grid() function to add grid lines to the plot/graph

##Program (MatPlotLibEx6.py)
#Add grid lines to the plot

import numpy as np;
import matplotlib.pyplot as plt;

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

plt.title("Student-Details/Report-Card");
plt.xlabel("Roll-Numbers");
plt.ylabel("Student-Ages");

plt.plot(x, y)
plt.grid()
plt.show()

'''
==> Specify Which Grid Lines to Display::-
= For this, we use the axis="" parameter in the grid() function to specify which grid lines to display
= Accepted-values are 'x','y' and 'both'
(Default value is 'both')
'''
##Program (MatPlotLibEx6.py)
#Display only grid lines for the x-axis

import numpy as np;
import matplotlib.pyplot as plt;

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

plt.title("Student-Details/Report-Card");
plt.xlabel("Roll-Numbers");
plt.ylabel("Student-Ages");

plt.plot(x, y);
plt.grid(axis='x');
plt.grid(axis='y');
plt.show();



# ==> Setting Line-Properties for the Grid::-
# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

##Program (MatPlotLibEx6.py)
#Setting line-properties of the grid

import numpy as np;
import matplotlib.pyplot as plt;

x = np.array([1001,1002,1003,1004,1005]);
y = np.array([23, 25, 22, 20, 21]);

plt.title("Student-Details/Report-Card");
plt.xlabel("Roll-Numbers");
plt.ylabel("Student-Ages");

plt.plot(x, y);
plt.grid(color='orange', linestyle='--', linewidth=1.0);
plt.show();


# (***)
# ==> Matplotlib Subplots::-
# (Displaying Multiple Plots/Graphs)
# = With the subplots() function you can draw multiple plots in one figure

##Program (MatPlotLibEx7.py)
#Drawing 2 plots at a time

import matplotlib.pyplot as plt;
import numpy as np;

#graph1
x = np.array([0, 1, 2, 3]);
y = np.array([0, 5, 2, 8]);

plt.subplot(1, 2, 1);
plt.plot(x,y);

#graph2
x = np.array([0, 1, 2, 3]);
y = np.array([0, 1, 2, 3]);

plt.subplot(1, 2, 2);
plt.plot(x,y);
plt.show();

'''
**NOTE::-
=> subplots(arg1,arg2,arg3) Function
= It takes 3-args which describes layout of the figure
(layout is organized in rows and columns, which are represented by the 1st and 2nd argument)
(3rd argument represents the index of the current plot)
'''

##Program (MatPlotLibEx7.py)
#Draw 2 plots on top of each other (2-rows & 1-col)

import matplotlib.pyplot as plt;
import numpy as np;

#graph1
x = np.array([0, 1, 2, 3]);
y = np.array([0, 5, 2, 8]);

plt.subplot(2, 1, 1);
plt.plot(x,y);

#graph2
x = np.array([0, 1, 2, 3]);
y = np.array([0, 1, 2, 3]);

plt.subplot(2, 1, 2);
plt.plot(x,y);
plt.show();


'''
==> Multiple Plots ::-
= We can draw as many plots as required in one figure
= For this give no.of.rows, no.of.cols, and the index of the plot
'''

##Program (MatPlotLibEx7.py)
#Draw 6 plots (2-rows & 3-cols)

import matplotlib.pyplot as plt;
import numpy as np;

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()



# ==> Titles for Subplots::-
# = You can add a title to each plot with the title() function

##Program (MatPlotLibEx7.py)
#2 sub-plots, with titles

import matplotlib.pyplot as plt;
import numpy as np;

#graph1
x = np.array([0, 1, 2, 3]);
y = np.array([0, 5, 2, 8]);

plt.subplot(1, 2, 1);
plt.plot(x,y);
plt.title("Students");

#graph2:
x = np.array([0, 1, 2, 3]);
y = np.array([0, 1, 2, 3]);

plt.subplot(1, 2, 2);
plt.plot(x,y);
plt.title("Depts");
plt.show();



# ==> Super Title::-
# = We can add a title to the entire figure with the suptitle() function

##Program (MatPlotLibEx7.py)
#Add a title for the entire figure

import matplotlib.pyplot as plt;
import numpy as np;

#graph1
x = np.array([0, 1, 2, 3]);
y = np.array([0, 5, 2, 8]);

plt.subplot(1, 2, 1);
plt.plot(x,y);
plt.title("Students");

#graph2:
x = np.array([0, 1, 2, 3]);
y = np.array([0, 1, 2, 3]);

plt.subplot(1, 2, 2);
plt.plot(x,y);
plt.title("Depts");

plt.suptitle("College-REPORT")
plt.show()


'''
#(*****)
==> Matplotlib Scatter::-
=> Creating Scatter Plots/Graphs
= Using a Pyplot module and scatter() function, we can draw a scatter plot
= scatter() function plots one dot for each co-ordinate in graph
= It uses 2-arrays of same-size
(x-axis,y-axis)
'''
##Program (MatPlotLibEx8.py)
#Simple scatter plot/graph

import matplotlib.pyplot as plt;
import numpy as np;

x = np.array([2,4,6,8,10,12,14,16,18,20,22,24])
y = np.array([95,80,85,75,70,45,100,25,10,50,35,20])

plt.scatter(x,y);
plt.show();

# =** it takes corresponding values from each array as co-ordinate


# ==> Comparing Plots::-
# = For comparing multiple-plots, we use multiple (x,y) co-ordinates from multiple-arrays

##Program (MatPlotLibEx8.py)
##Draw two plots in the same graph
import matplotlib.pyplot as plt;
import numpy as np;

x = np.array([2,4,6,8,10,12,14,16,18,20,22,24]);
y = np.array([95,80,85,75,70,45,100,25,10,50,35,20]);

plt.scatter(x, y);

x = np.array([2,4,6,8,10,12,14,16,18,20,22,24]);
y = np.array([90,85,80,70,75,40,95,30,15,55,30,25]);

plt.scatter(x, y);
plt.show();

'''
NOTE:-
=> Colors::-
= We can set colors for scatter plots using "color" (or) "c" argument
Ex:- ==Same-Program==
plt.scatter(x, y, color="#88c999");
plt.scatter(x, y, color="green");

=> Colors for each dot::-
= We can have specific color for each dot by using an array of colors as value for the c argument
(We cannot use the color argument for this, only the c argument)
Ex:- ==Same-Program==
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan"])
plt.scatter(x, y, c=colors);


=> Sizes::-
= We can change the size of dots using s="" argument
= Same like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis co-ordinatess
Ex:- ==SAME-Prog==
sizes = np.array([10,20,30,40,50,60,70,80,90,100,110,120]);
plt.scatter(x, y, s=sizes);


=> Alpha::-
= We can provide transparency of dots using alpha="" argument
Ex:- ==SAME-Prog==
plt.scatter(x, y, s=sizes, alpha=0.5);		#0.0 to 1.0

=** Finally, we can combinew s="", c="", alpha=0.5 all at a time



(*****)
==>>> Matplotlib Bars::-
=> Creating Bars
= For this, we use bar() function to drawing bar-graphs
'''

##Program (MatPlotLibEx9.py)
#Draw 4 bars using MatPlotLib

import matplotlib.pyplot as plt;
import numpy as np;

x = np.array(["A","B","C","D"]);
y = np.array([5,9,2,6]);

plt.bar(x,y);
plt.show();

'''
**NOTE:-
= For bar() function, we can pass arguments
= Arguments are given as arrays
Ex::-
plt.bar(x, y)


=> Horizontal Bars::-
= For horizontal bars, use the barh() function
'''
##Program (MatPlotLibEx9.py)
#Draw 4 horizontal bars
import matplotlib.pyplot as plt;
import numpy as np;

x = np.array(["A","B","C","D"]);
y = np.array([5,9,2,6]);

plt.barh(x, y);
plt.show();

'''
NOTE:-
=> Bar Colors:-
= bar() and barh() we can give keyword-argument color="", to set the color of the bars
Ex:- ==SAME-Prog==
	plt.bar(x, y, color = "green");		#color-name
	plt.bar(x, y, color = "#4CAF50");	#hexadecimal-value

=> Bar Width:-
= For bar() we can give keyword-argument width="", to set the width of the bars
Ex:- ==SAME-Prog==
	plt.bar(x, y, width=0.1);
	plt.bar(x, y, width=0.5);
(default width is 0.8)

=> Bar Height:-
= For barh() we can give keyword-argument height="", to set the height of the bars
Ex:- ==SAME-Prog==
	plt.barh(x,y,height=0.1);
	plt.barh(x,y,height=0.5);
(default height is 0.8)	



(*****)
==>> Matplotlib with Histograms::-
(Histogram)
= A histogram is a graph showing frequency distributions
= It is a graph with no. of observations with-in given interval-time
Ex::-
=> Create Histogram?
= For this, we use hist() function to create histograms
= hist() function takes an array of numbers as input-para(args)
 '''
 
##Program (MatPlotLibEx10.py) 
import matplotlib.pyplot as plt;
import numpy as np;

x = np.random.normal(100,5,200);

plt.hist(x);
plt.show();

'''
NOTE:-
= Array with 200-values, where the values will concentrate around 100, and the standard deviation is 5


(*****)
==>> Matplotlib with Pie-Charts::-
=> Creating Pie Charts,
= Using Pyplot module, we can use pie() function to draw pie charts
'''
#A simple pie chart
import matplotlib.pyplot as plt;
import numpy as np;

y = np.array([30,20,35,15]);

plt.pie(y);
plt.show();

'''
NOTE:-
**= Here, pie-chart draws one piece (called a wedge) for each value in the array 
Ex:- [30,20,35,15]
(by default, the plotting of the first wedge starts from the x-axis and moves anti-clockwise)

**= The size of each wedge is determined by comparing the value with all the other values, by using this formula: x/sum(x)


=> Labels:-
= We can add labels to the pie chart with the label="" parameter
= label="" parameter is an array with one label for each wedge
Ex:- ==SAME-Prog==
mylabels = ["A","B","C","D"]
plt.pie(y, labels = mylabels)


=> Start-Angle::-
= Default start angle is at the x-axis(0-degrees)
= However, we can change the start angle by specifying a startangle="" parameter
Ex:- (==SAME-Prog==)
	plt.pie(y, labels = mylabels,startangle=45);


=> Explode::-
= For any-one wedge to stand-out(separated from pie-chart as single-piece), we use explode="" parameter
= The explode="" parameter, is an array with one value for each wedge
(Each value represents how far from the center each wedge is displayed)
Ex:-
myexplode = [0.2, 0, 0.3, 0];
plt.pie(y, labels= mylabels, explode=myexplode);


=> Shadow::-
= We can shadow to the pie-chart, by giving shadows="" parameter to True
Ex:-
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)


=> Colors::-
= We can set the color of each wedge with the colors="" parameter
= colors="" parameter, is an array with one value for each wedge
Ex:-
mycolors = ["blue","yellow","#4CAF50","b"];
plt.pie(y, labels=mylabels, colors=mycolors);

NOTE:-
= Hexadecimal-color-values (or) color-names, (or) color-name-shortcuts
Ex:-
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White



=> Legend::-
= We can add a list of explanation for each wedge, use the legend() function
Ex:-
mylabels = ["A","B","C","D"]
plt.pie(y, labels = mylabels)
plt.legend()


=> Legend With Header::-
= For adding header to the legend, add the title="" parameter to the legend function
Ex:-
plt.legend(title="Four-Parts");




***Next-class(DJANGO)***
-----------------------------
14-SEP-2022(WED) @9am

'''
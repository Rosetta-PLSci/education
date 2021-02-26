import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

########################################################################

"""
dataOne = np.arange(10)
plt.title("DATA TITLE")
# .title --> creating title
plt.xlabel("X PATH NAME")
# .xlabel --> creating x path name
plt.ylabel("Y PATH NAME")
# .ylabel --> creating y path name
plt.plot(dataOne)
# .plot --> creating a new graphic
"""

########################################################################

"""
x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y,"ro")
# "ro" --> graphic line type --> red o
# "b--" --> graphic line type --> blue --
# "g^" --> graphic line type --> green ^
# "rs" --> graphic line type --> red square
"""

########################################################################

"""
dataTwo = np.arange(0,20,2)
plt.plot(dataTwo,dataTwo,"b--",dataTwo,dataTwo**2,"rs",dataTwo,(dataTwo * 3),"g^")
# plt.plot() polyline in a single graphic
"""

########################################################################

"""
figure = plt.figure()
# empty graphics area
dataThree = np.random.randint(0,10,20)

x1 = figure.add_subplot(2,2,1)
x2 = figure.add_subplot(2,2,2)
x3 = figure.add_subplot(2,2,3)
# .figure.add_subplot(graphic size,position)
# .figure.add_subplot(nrows,ncols,index)

x1.plot(dataThree, "g^")
x2.plot(dataThree, "ro")
x3.plot(dataThree, "k--")
# creating multiple charts in a single area
"""

########################################################################

"""
figure = plt.figure()
x = [1,5,7,9]
y = [10,11,12,13]
ax = figure.add_subplot(1,1,1)
ax.plot(x, y, linestyle="--", color="b")
# graphic of x relative to y
# linestyle = 
# color =
"""

########################################################################

"""
dataFour = np.random.rand(50).cumsum()
figure = plt.figure()
ax = figure.add_subplot(1,1,1)
ax.set_xticks([0,15,30,45])
# .set_xticks() changing indicator ranges in path x
ax.set_xticklabels(["ONE","TWO","THREE","FOUR"], rotation=15, fontsize="small")
# .set_xticklabels() changing indicator names in path x
informations = {"title":"GRAPHIC",
                "xlabel":"X PATH",
                "ylabel":"Y PATH"}
ax.set(**informations)
# plotting previously determined properties
plt.plot(dataFour)
"""

########################################################################

"""
figure = plt.figure()
ax = figure.add_subplot(1,1,1)

data1 = np.random.randn(1000).cumsum()
data2 = np.random.randn(1000).cumsum()
data3 = np.random.randn(1000).cumsum()

ax.plot(data1,"k",label="ONE")
ax.plot(data2,"r--",label="TWO")
ax.plot(data3,"b.",label="THREE")
ax.legend(loc="best")
# label= determines the name of the lines in the chart
# .legend() determines the names and position of the lines without using labels
"""

########################################################################

"""
figure = plt.figure()
ax = figure.add_subplot(1,1,1)

data = np.linspace(0,50,30)
ax.set_xticks([0,10,20,30,40,50])
ax.set_xticklabels(["ZERO","TEN","TWENTY","THIRTY","FOURTY","FIFTY"], rotation=20, fontsize="small")
ax.annotate("PING", xy=(20,50), arrowprops=dict(facecolor="red"))
# .annotate() puting a mark on a desired place
# .annotate("name", xy=where, type)
ax.plot(data,"k-.", label="DATA")
"""

########################################################################

"""
plt.style.use("classic")
# .style.use() selecting a template for graphics
x = np.linspace(0,10,20)
y = np.random.randint(0,100,20)
plt.legend("123456789", ncol=2, loc="best")
plt.plot(x,y)
sns.set()
# seaborn (sns) library can work with matplotlib
"""

########################################################################

"""
iris = sns.load_dataset("iris")
# sns.load_dataset("data name") can load a data from internet

iris.sepal_width.plot.hist()
# .plot.hist() creating a histogram graphic
# .sepal_width is a part of data --> example
"""

########################################################################

"""
iris = sns.load_dataset("iris")
sns.kdeplot(iris.sepal_length, shade=True, color="k")
# sns.kdeplot() density value graphic of a desired data
"""

########################################################################

"""
iris = sns.load_dataset("iris")

sns.distplot(iris.sepal_length)
sns.distplot(iris.sepal_width)
# sns.distplot() displaying both histogram and density value of a desired data on the same graphic.
"""

########################################################################

"""
iris = sns.load_dataset("iris")

sns.jointplot("sepal_length", "sepal_width", data=iris)

# sns.jointplot() both histogram and scatter plot shown together
"""

########################################################################

"""
iris = sns.load_dataset("iris")

sns.pairplot(iris,hue="species")

# sns.pairplot() showing general graphic depending on a value of data set
"""

########################################################################

"""
tips = sns.load_dataset("tips")
# another dataset is loaded

grid = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)
grid.map(plt.hist, "tip", bins=np.linspace(0,40,20))
# sns.FacetGrid() creating a square graph area depending on the desired values
# .map() making comparison depending on a desired value
# .map(graphic type, desired value, spacing)
"""

########################################################################

"""
tips = sns.load_dataset("tips")

sns.catplot("day", "total_bill", "smoker", data=tips)
# sns.catplot() creating graphic for relationship between the desired data
# sns.catplot(data for x path, data for y path, desired data, data=target data)
"""

########################################################################

"""
x = np.linspace(0,20,50)

plt.plot(x, np.sin(x), color="r", linestyle="--")
plt.xlim(-5,20)
plt.ylim(-3,3)
# plt.xlim() constraining the path x within the specified range
# plt.ylim() constraining the path y within the specified range
"""

########################################################################

"""
x = np.linspace(0,10,15)
y = np.sin(x)
t = 5.7

plt.fill_between(x, y, t, alpha=0.4)
# plt.fill_between() painting desired area
# plt.fill_between(x path, desired area, up to the designated place, alpha=opacity)
"""

########################################################################

"""
iris = sns.load_dataset("iris")

plt.scatter(iris.petal_width, iris.sepal_length, s=75, c="m", marker="v", edgecolors="black", linewidths=1)
# plt.scatter() creating a scatter plot
# plt.scatter(x path, y path)
# s= size
# c= color
"""

########################################################################

"""
math = np.random.randint(50,100,7)
science = np.random.randint(50,100,7)
eng = np.random.randint(50,100,7)
index = np.arange(7)

plt.bar(index, math, label="MATH")
plt.bar(index, science, label="SCIENCE")
plt.bar(index, eng, label="ENGLISH")
plt.legend(loc="best")
# plt.bar() creating a vertical bar graphic
# plt.bar(x path, y path)
"""

########################################################################

"""
x = np.linspace(0,10,30)
y = np.random.randint(0,5,30)

plt.errorbar(x, y, yerr=1, fmt="k.", ecolor="red", elinewidth=2)
# plt.errorbar() creating a error bar
# plt.errorbar(x path, y path, yerr or xerr)
# yerr= how many units to draw on the y-axis
# xerr= how many units to draw on the x-axis
# fmt= type of point of error location
"""

########################################################################

"""
iris = sns.load_dataset("iris")

mean = np.mean(iris, axis=0)
std = np.std(iris, axis=0)
between = range(4)

plt.barh(between, mean, color="b", xerr=std, alpha=0.5, align="center")
# plt.barh() creating a horizontal bar graphic
# plt.barh(x path, y path, xerr or yerr)
"""

########################################################################

"""
data = np.random.randn(1000)
bins = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
median = np.median(data)

plt.hist(data, edgecolor="black", bins=bins)
plt.axvline(median,color="red")
# plt.axvline() marking a desired value
"""

########################################################################

"""
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-3, 2, 1000)
x3 = np.random.normal(2, 1, 1000)

plt.hist2d(x1, x2, bins=30, cmap="Reds")
sidebar = plt.colorbar()
sidebar.set_label("SIDE BAR")
# plt.hist2d() creating two-dimensional histogram graphic
# plt.colorbar() creating a side bar for values
"""

########################################################################

plt.plot() --> """creating a basic graphic"""
plt.hist() --> """creating a histogram graphic"""
plt.hist2d() --> """creating two-dimensional histogram graphic"""
plt.scatter() --> """creating a scatter graphic"""
plt.bar() --> """creating a vertical bar graphic"""
plt.barh() --> """creating a horizontal graphic"""
plt.errorbar() --> """creating a error bar graphic"""
plt.xlabel() --> """creating x path name"""
plt.ylabel() --> """creating y path name"""
plt.figure() --> """creating empty graphics area"""
plt.legend() --> """determines the names and position of the lines without using labels"""
plt.xlim() --> """constraining the path x within the specified range"""
plt.ylim() --> """constraining the path y within the specified range"""
plt.fill_between() --> """painting desired area"""
plt.axvline() --> """marking a desired value"""
plt.colorbar() --> """creating a side bar for values"""
.add_subplot() --> """creating a subplot graphic"""
.set_xticks() --> """changing indicator ranges in path x"""
.set_yticks() --> """changing indicator ranges in path y"""
.set_xticklabels() --> """changing indicator names in path x"""
.set_yticklabels() --> """changing indicator names in path y"""
.annotate() --> """puting a mark on a desired place"""
sns.load_dataset() --> """importing and loading a data set from internet"""
sns.kdeplot() --> """density value graphic of a desired data"""
sns.distplot() --> """displaying both histogram and density value of a desired data on the same graphic"""
sns.jointplot() --> """both histogram and scatter plot shown together"""
sns.pairplot() --> """showing general graphic depending on a value of data set"""
sns.catplot() --> """creating graphic for relationship between the desired data"""
sns.FacetGrid() --> """creating a square graph area depending on the desired values"""
.map() --> """making comparison depending on a desired value"""

import numpy as np

########################################################################

NPArrayData = np.array(["NEW YORK",1,"TURKEY",2.5,"ARGENTINA"])
print(type(NPArrayData))
# all elements in it are always uniform
# If there is both a string, an integer or a float value in it, all integer values become strings

########################################################################

NumberList = [1,2,3,44,56,78,1020]
NPNumberData = np.array(NumberList)
print(NPNumberData)
# a previously defined list can be converted to array data
# a dictionary also can be converted to array data

########################################################################

ResultOne = [1,22,34,3,45,6]
ResultTwo = [2,33,12,5,6,34]
ResultMean = (np.array(ResultOne) + np.array(ResultTwo)) / 2
print(ResultMean)
# data in array is processed as mutual indexes
print(ResultMean[ResultMean < 25])
# desired conditions are checked

########################################################################

NewNumpyData = np.array(["George",22,"Germany",4.6])
print(NewNumpyData[0])
print(NewNumpyData[2])
print(NewNumpyData[-1])
print(NewNumpyData[:3])
print(NewNumpyData[1:3])
print(NewNumpyData[::])
# accessing information in data

########################################################################

NPArangeData = np.arange(0,20,2)
print(NPArangeData)
# np.arange(first,last,step)
# creating a numpy data in the desired range
# the last value in the specified range is not processed

########################################################################

NPLinspaceData = np.linspace(2,300,20)
print(NPLinspaceData)
# np.linspace(first,last,how many values)
# creating a numpy data of numbers in the desired range, evenly spaced as desired
# the determined starting and final values are processed

########################################################################

NPLogspaceData = np.logspace(0,3,4)
print(NPLogspaceData)
# np.logspace(first,last,how many values)
# creating the logarithm of the numbers in the array
# first and last values are processed

########################################################################

NPDimensionalData = np.array([[12,33,4,5],[22,33,567,1],[22,12.3,44,5]])
print(NPDimensionalData)
# np.array([[---],[---],[---]]) creating a two-dimensional numpy data

########################################################################

NPDataForReshape = np.arange(20).reshape(4,5)
print(NPDataForReshape)
# .reshape() adapting a data to the desired shape
# in this example it has been made into 4 rows and 5 columns
# values of data to be converted must be proportional to the number of rows and columns
# for example 4x5 = 20

########################################################################

NPDimensionalDataForTransactions = np.arange(40).reshape(5,8)
print(NPDimensionalDataForTransactions)
print(NPDimensionalDataForTransactions[2:3,3:4])
print(NPDimensionalDataForTransactions[:3,:4])
# reaching the desired value in two dimensional data
# [row,columns]
# for example [2:3-->row range,3:4-->columns range]

########################################################################

NPThreeDimensionalData = np.array([[[22,33,44,56],[34,123,45,4445],[3.4,55.6,3.1,2]],[[22,33,4,55],[33,22,11,4],[4.5,22.2,33.1,34]]])
print(NPThreeDimensionalData)
print(NPThreeDimensionalData.shape)
# np.array([[[---],[---],[---]],[[---],[---],[---]]]) creating a three-dimensional numpy data
# height, row, column or how many, row, column
# for example 2 height, 3 rows, 4 columns or 2 data of 3 rows and 4 columns

########################################################################

NPThreeDimensionalDataForTransactions = np.array([[[22,33,44,56],[34,123,45,4445],[3.4,55.6,3.1,2]],[[22,33,4,55],[33,22,11,4],[4.5,22.2,33.1,34]]])

print(NPThreeDimensionalDataForTransactions.sum(0))
# .sum(0) height sum
print(NPThreeDimensionalDataForTransactions.sum(1))
# .sum(1) column sum
print(NPThreeDimensionalDataForTransactions.sum(2))
# .sum(2) row sum
print(NPThreeDimensionalDataForTransactions.max())
# maximum value
print(NPThreeDimensionalDataForTransactions.min())
# minimum value
print(NPThreeDimensionalDataForTransactions.argmax())
# index of maximum value
print(NPThreeDimensionalDataForTransactions.argmin())
# index of minimum value
print(NPThreeDimensionalDataForTransactions.ptp())
# subtraction between maximum value and minimum value

########################################################################

a = np.array([[12,33,44,5],[234,21,33,4],[321,44,6,7]])
b = np.array([[34,21,4,5],[123,456,3,4],[98,70,68,6]])

print(a-b)
print(a+b)
print(a/b)
print(a*b)

print(np.sum(a[:, 1]))
print(np.sum(a[:, 2]))
print(np.sum(a[1, :]))

########################################################################

x = np.random.uniform(low=1,high=50,size=16).reshape(4,4)
print(x)
# np.random.uniform() with the desired numpy sequence is obtained with random values within the specified upper and lower limits
# low= first value
# high= last value
# size= how many

########################################################################

np.array([---]) --> """creating a simple numpy data"""
np.array([[---],[---],[---]]) --> """creating a simple two dimensional numpy data with several values"""
np.array([[[---],[---],[---]],[[---],[---],[---]]]) --> """creating a simple three dimensional numpy data with several values"""
np.arange() --> """creating a numpy data in the desired range"""
np.random.uniform() --> """with the desired numpy sequence is obtained with random values ​​within the specified upper and lower limits"""
np.linspace() --> """creating a numpy data of numbers in the desired range, evenly spaced as desired"""
np.logspace() --> """creating the logarithm of the numbers in the array"""
np.amax() --> """showing the maximum value in the column or row"""
np.amin() --> """showing the minimum value in the column or row"""
np.concatenate() --> """placing two desired data on top of each other or side by side"""
np.full() --> """creating a data with the desired dimensions and the specified value"""
np.intersect1d() --> """showing common values ​​in the two data"""
np.isin() --> """checking values in a data"""
np.isnan() --> """checking NaN values in a data"""
np.ones() ---> """creating a data with one(1)"""
np.zeros() ---> """creating a data with zero(0)"""
np.repeat() --> """creating a data of the desired number of repeating values"""
np.reshape() --> """using to shape a data"""
np.setdiff1d() --> """showing values of a data that are not in the second data"""
np.unique() --> """showing only once if a data has duplicate values"""
np.where() --> """showing values ​​that meet the desired conditions in a data"""
np.mean() --> """calculating the mean of values"""
np.median() --> """finding the middle value"""
.sum() --> """addition all values in a data""" 
.max() --> """showing maximum value"""
.min() --> """showing manimum value"""
.argmax() --> """showing index of maximum value"""
.argmin() --> """showing index of manimum value"""
.ptp() --> """subtraction between maximum value and minimum value in a data"""
.dtype() --> """showing type of a data"""
.shape() --> """showing the structure of a data"""

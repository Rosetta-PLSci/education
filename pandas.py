import pandas as pd
import numpy as np

########################################################################

listOne = ["George",23,"Germany"]

PandasDataOne = pd.Series(listOne)
print(PandasDataOne)

# pd.Series() converting one-dimensional lists to Pandas series
# Pandas series can be converting a list too

########################################################################

DictOne = {"name":"John","surname":"Watson","age":22}

PandasDataTwo = pd.Series(DictOne)
print(PandasDataTwo)

# pd.Series() converting one-dimensional dictionaries to Pandas series
# key values in the dictionary are determined as index names
# Pandas series can be converting a dictionary too

########################################################################

DataOne = pd.Series(["Feymann","Belgium",1,3,5,"CE"])
print(DataOne)

# pd.Series([]) a list is written in it, the written list turns into a series
# it is defined as object if there are mixed values such as int-str-float
# series can also be created from boolean values such as True or False

########################################################################

DataTwo = pd.Series(data=["Gerr",22,"Male"],index=["NAME","AGE","GENDER"])
DataTwo.name = "DATA TWO PANDAS SERIES"
print(DataTwo)

# data= writing values to be converted to series
# index= writing index names of values
# .name writing a title of series

########################################################################

ListWithDict = [{"name":"George","age":22,"gender":"MALE"},
                {"name":"Helena","age":43,"gender":"FEMALE"},
                {"name":"Garry","age":32,"gender":"MALE"}]
ConverToDF = pd.DataFrame(ListWithDict)
# pd.DataFrame() converting to Pandas Data Frame
# creating a data frame with the dictionary in the list
print(ConverToDF)

DictWithList = {"names":["George","Helena","Garry"],
                "age":[22,43,32],
                "gender":["MALE","FEMALE","MALE"]}
ConverToDFTwo = pd.DataFrame(DictWithList)
print(ConverToDFTwo)
# creating a data frame with the list in the dictionary

ListWithList = [["George","Helena","Garry"],
                [22,43,32],
                ["MALE","FEMALE","MALE"]]
ConverToDFThree = pd.DataFrame(ListWithList)
print(ConverToDFThree)
# creating a data frame with the list in the list
# index and columns names start from 0, for example 0-1-2-3

SingleList = ["George","Helena","Garry"]
ConverToDFFour = pd.DataFrame(SingleList)
print(ConverToDFFour)
# creating a data frame with the single list

SingleDict = {"George": pd.Series(data=[22,"MALE"],index=["AGE","GENDER"])}
ConverToDFFive = pd.DataFrame(SingleDict)
print(ConverToDFFive)
# creating a data frame with the single dictionary
# if Data Frame will be created from a single dictionary, data = and index = must be specified with pd.Series()

########################################################################

Numbers = pd.Series([33,2.4,120,6])

print(Numbers.sum())
# .sum() --> addition of all values
print(Numbers.mean())
# .mean() --> mean of all values
print(Numbers.product())
# .product() --> multiplication of all values

# all methods of sum, sub, mul, div can be used

########################################################################

DataFour = pd.Series(["Hell","Houst","CE",23],["NAME","SURNAME","JOB","AGE"])
# data = and index = need not be specified, the first is value entered, the second is index entered

print(DataFour["NAME"])
print(DataFour["AGE"])
# finding a certain value by typing index name
print(DataFour[["SURNAME","JOB"]])
# if you want to reach more than one value, two square brackets must be used
print(DataFour[0])
print(DataFour[1])
print(DataFour[-1])
# finding a value by typing the index number, instead of the index name
print(DataFour[[0,2]])
# if you want to reach more than one value by using index number, two square brackets must be used
print(DataFour[0:3])
# finding values within a certain range
print(DataFour["NAME":"AGE"])
# the range can also be specified by typing the index name
print(DataFour.loc["JOB"])
# .loc[] --> writing a index name for finding values
print(DataFour.iloc[1])
# .iloc[] --> writing a index number for finding values
print(sorted(DataFour))
# sorting values, but values must be same type
print(max(DataFour))
# finding maximum value
print(min(DataFour))
# finding minimum value

########################################################################

DataFive = pd.Series(["Germany",123400989,"North","West"],["COUNTRY","POPULATION","GMP","TMP"])

DataFive["COUNTRY"] = "UK"
DataFive.loc["POPULATION"] = 14909239
# a valua can be changed by using index name or .loc[]
DataFive.iloc[2] = "East"
#a value can be changed by using index number with .iloc[]

########################################################################

DataSix = pd.Series(["Germany",123400989,"North","West"],["COUNTRY","POPULATION","GMP","TMP"])

NewDataSix = DataSix.drop("COUNTRY")
# .drop() deleting a value
# can be assigned a new parameter to make the deletion valid
DataSix.drop("TMP",inplace=True)
# if inplace=True is used, deletion can be valid for main series

########################################################################

DataSeven = pd.read_csv("ReviewContent.csv",usecols=["Review ID"],squeeze=True,encoding="utf-8",engine="python")
# pd.read_csv() csv file reading and assigning to a parameter
# usecols=[] selecting a target column it it is needed
# squeeze= converting a column to Data Frame from series, if it is needed
# encoding= format of data 
# engine= format of coding language
# there are a lot of reading attributes for all type of document

########################################################################

DataEight = pd.read_csv("ReviewContent.csv")

print(type(DataEight))
# DataFrame types are multidimensional, series are unidimensional, but unidimensional series can also be DataFrame.

print(DataEight.head(10))
# .head() showing the requested amount of values from the beginning of the data, 5 lines come as default

print(DataEight.tail(10))
# .tail() showing the requested amount of values from the end of the data, 5 lines come as default

print(DataEight.info())
# showing general information about rows and columns

print(DataEight.dtypes)
#showing the data type of the rows

print(DataEight.sort_values(inplace=True,ascending=False))
# the values are sorted from min to max
# if ascending=False, data's values are sorted from max to min
# if inplace=True, changing can be valid

print(DataEight.sort_index(inplace=True,ascending=False))
# the index is sorted from min to max
# if ascending=False, data's index is sorted from max to min
# if inplace=True, changing can be valid

print(DataEight.get(4))
# finding value for the desired index
# it does not get an error if index is not in the data but it gets -None-
# if a single value is requested, the type of that value will be numpy types.

print(DataEight.get([0,100]))
# finding the desired values in a certain range

print(DataEight.isnull())
# returns False for parts with values in data, and True for non-value parts.

print(DataEight.isnull().sum())
# showing the sum of non-value in each column

print(DataEight.notnull())
# returns True if there is avalue, False otherwise

print(DataEight.count())
# showing the number of values in columns

print(DataEight.dropna())
# deleting all rows and columns that are NaN

print(DataEight.fillna())
# filling in NaN values by preference

print(DataEight.name)
# showing name of series

print(DataEight.size)
# showing how many values it consists of

print(DataEight.ndim)
# showing how many dimensions are

print(DataEight.columns)
# showing all the columns name

print(DataEight.isin())
# showing indexes with the requested values

print(DataEight.between())
# showing values in the desired range

print(DataEight.drop_duplicates())
# deleting repetitive values

print(DataEight.unique())
# showing values as singular

print(DataEight.nunique())
# showing how many different values are used

########################################################################

SingleDictToTest = {"GEORGE": pd.Series(data=["MALE",32,"CE","USA"],index=["GENDER","AGE","JOB","COUNTRY"]),
                    "HALE": pd.Series(data=["FEMALE",22,"TE","TURKEY"],index=["GENDER","AGE","JOB","COUNTRY"]),
                    "GARRY": pd.Series(data=["MALE",32,"PDR","UK"],index=["GENDER","AGE","JOB","COUNTRY"])}

ConverToDFFromDict = pd.DataFrame(SingleDictToTest)


ConverToDFFromDict["TIM"] = ["MALE",45,"IT","USA"]
# adding a new value corresponding to the index

AddingNew = pd.DataFrame({"GEORGE":"GASPORA","HALE":"TURGUT","GARRY":"PATTY","TIM":"FEYMANN"},index=["SURNAME"])
ConverToDFFromDict = ConverToDFFromDict.append(AddingNew)
# adding a new column with values
print(ConverToDFFromDict)
print()

ConverToDFFromDict.pop("TIM")
# deleting a desired column with all values

ConverToDFFromDict = ConverToDFFromDict.drop("AGE",axis=0)
# deleting a desired column or row
# if axis=1, desired column will be deleted
# if axis=0, desired row will be deleted

ConverToDFFromDict = ConverToDFFromDict.drop(["JOB","SURNAME"],axis=0)
# deleting multiable columns or rows

print(ConverToDFFromDict)

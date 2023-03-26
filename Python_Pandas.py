import pandas as pd
# #read csv file
# df = pd.read_csv(r'Z:\Shiju\Technical Docs\Python\party.csv')
# print(type(df))
# print(df)

#Dataframes:
# print(df.shape) #size of the csv file(row,columns)
# print(df.info())  # file info
# print(list(df.columns)) # to get the column names
# print(list(df.isna().sum())) # null values in columns
# print(df.duplicated().sum()) # duplicate rows
# df.set_index('column1')
# print(df.iloc[0:11 , 0:2]) #iloc - index loc,  slicing the Dataframe. 0:11 - row, 0:2 - column
# print(df.iloc[0:11 , : ]) #loc - in loc we use string value of both column and row not index,  slicing the Dataframe. 0:11 - row, : - all columns

#panda series:
#Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
#The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.
#only one datatype aloowed in series (for eg: either int  or float)
# s1 = pd.Series([10, 20, 30, 40, 50])
# print(s1)

#Data frame is two dimensional object but Series is one dimensional object. df is collection of series but one index.
#series is immutable but DF is mutable.
# df = pd.DataFrame({'column1':[1,2,3,4,5],'column2':[10,20,30,40,50]})
# print(df)
# print(df['column1'])
# print(df['column2'])

# #we can add any index in Series
# s1 = pd.Series(([10, 20, 30, 40, 50]), index = ['a','b','c','d','e'])
# print(s1)
# print(s1[3])
# print(s1[1:3])

#map, apply and applymap
#map(), applymap(), and apply() methods are methods of Pandas library in Python
#
# df = pd.DataFrame({'column1':[1,2,3,4,5],'column2':[10,20,30,40,50],'column3':[50,51,52,53,54]})
# # print(df)
# df['column1']
# def double(n):
#     return n*2
#
# # #:apply this function in DF and Series
# #
# # #apply apply() function to double function - it can be done for both series and Dataframe
# # x = df['column1'].apply(double)
# # print(x)
# #
# # y = df.apply(double)
# # print(y)
# #
# # # #map - applies only to series
# # # z = df.map(double) # this will throw an error since map applies only to series not to DF
# # # print(z)
# #
# x = df['column1'].map(double)
# print(x)
# # # #applymap only to DataFrame
# # x = df['column1'].applymap(double)  # this will throw an error
# # print(x)
# # #applymap only to DataFrame
# x = df.applymap(double)
# print(x)


#read csv file
df = pd.read_csv(r'Z:\Shiju\Technical Docs\Python\party.csv')
df =pd.read_clipboard()
print(df.columns)
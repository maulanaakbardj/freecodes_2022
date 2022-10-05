import pandas as pd
print("---This program will help you to get all statistics information of a dataframe---")
dfname = input("Enter Dataframe Name : ")
colname = input("Enter specified column name to get statistics on : ")
print(
"Min value of the coulmn ; ",
dfname[colname].min(),
"Max value of the column ; ",
dfname[colname].max(),
"Mode of column ; ",
dfname[colname].mode(),
"Median value of column ; ",
dfname[colname].median(),
"Mean/Avg value of column ; ",
dfname[colname].mean(),
"Mean Absolute Deviation of Column ; ",
dfname[colname].mad(),
"Count of values in column ; ",
dfname[colname].count(),
"Sum of values of cloumn ; ",
dfname[colname].sum()
)

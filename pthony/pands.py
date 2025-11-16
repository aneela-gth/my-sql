# pandas

import pandas as pd
detials={
    "names":["aneela","akhil","nani"],
    "marks":[20,59,25]
}
# creating a dataframe
df=pd.DataFrame(detials)
print(df)
print(type(df))

df_2=pd.Series([1,2,3,4,5])
print(df_2)
print(type(df_2))

# json excel csc(comma seprated value)
df=pd.read_csv("../orers.csv",header=None)
print(df)

df=pd.read_csv("./orders.csv")
# 1.head-- it returns top most rows in the data
# default is 5
print(df.head(50))  #it returns top 10 rows

# 2.tail---bottam valuse use
print(df.tail(10))

# 3.info
print(df.info())

# 4.describeit returns the statitical data
print(df.describe()) # 


# 5. shape:
print(df.shape) #returns the row and col count

# 6.colums
print(df.columns)

# 7.datatype
print(df.dtypes)

# object float int
print(df["sales"])

# latest updates in python
# data analayess
# 1.data cleanning



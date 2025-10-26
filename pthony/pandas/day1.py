
import pandas as pd

# pandas:
# data analysis
# machinelearnig
# datascience
# stastitis


# 1d---series
# 2d---dataframe

# details={
#     "name":["aneela","akhila","sunny"],
#     "marks":[45,60,67]
# }
# df=pd.DataFrame(details)
# print(df)
# print(type(df))

# # creating a dataframe
# df_2=pd.Series([1,2,3,4,5])
# print(df_2)
# print(type(df_2))

# # json exceal csv (comma seprated value)
# df=pd.read_csv("./csv.csv")
# print(df)

# df=pd.read_csv("./csv.csv")
# print(df.head(10)) ---->#it returns top 10 rows

#2.tail---bottom valuse use
# df=pd.read_csv("./csv.csv")
# print(df.tail(10))

# 3.info:
# df=pd.read_csv("./csv.csv")
# print(df.info())----->describe

# 4.describeit returns the statitical data
# print(df.describe())

# methode
# 5.shape:
# print(df.shape) -----> #returns the row and col count

# 6.colums:
# print(df.columns)

# 7.dtype:
# print(df.dtypes)

# 8.object float int
# print(df["sales"])

heros={
    "names":["nani","prabsh","allurjun","maheshbabu"],
    "hit":["ega","bahubali-2","bussnesman","pushpa-2"]
}
# print(heros.get("heronames")) 
# df=pd.DataFrame(heros)
# print(df)
# print(df.head(1))
# print(df.tail(1))
# print(df.info())

# 1.loc
# print(df.loc[0:2])
# print(df.loc[0,"ega"]) ---->#column bases
# print(df.loc[0,"social"])

df=pd.read_csv("./csv.csv")
# print(df)
# print(df.loc[9,"profit"])----> #enntire  table patuclure valu acess 

# 2.iloc:it displays to date of the colume
# print(df.iloc[1,1])
# print(df.iloc[2,4])

# 3.at: is is displiys to position , position nothing but index
# perpose:fast scalar access:at(label)iat(integars)
# print(df.iat[2,3]) -----> #second indexrow column

# print(df.get("region")) 



# query()
# fie using string
# print(df.query('ship_mode=="second class" and region=="south"'))
# print(df[df["ship_mode"=="second class"] & df["region"=="south"]])
# print(df[(df['ship_mode']=="second class") | (df['region']=='south')])
# print(df[(df["profit"]).between(5,10)])
# print(df.isnull())
# print(df["profit"].isnull())
# print(df.dropna(axis=1,inplace=True))
# print(df.dropna(axis=0))

# fillna():
# print(df.fillna("example"))

# replace():
# print(df.replace(to_replace="south",value="something"))
# print(df.replace(to_replace="south",value="something")["region"])

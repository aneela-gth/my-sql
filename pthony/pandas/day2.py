#  data creation:
import pandas as pd
data={
    "name":["aneela","akhila","nani"],
    "age":[23,22,23],
    "city":["hyd","vizag","delhi"]
}
dt=pd.DataFrame(data)
print(dt)



# # 2. Data Input / Output:
# # pd.read_csv()
# df=pd.read_csv("./csv.csv")
# print(df.head())
# print(df.head(10))
# print(df.tail())
# print(df.describe())
# print(df.info())
# df.sort_values(by="profit")
# print(df)

# #  1.loc
# print(df.loc[0:2])
# print(df.loc[0,"ega"]) #column bases
# print(df.loc[0,"social"])
# print(df)
# print(df.loc[9,"profit"])   #enntire  table patuclure valu acess 

# # 2.iloc:it displays to date of the colume
# print(df.iloc[1,1])
# print(df.iloc[2,4])

# # 3.at: is is displiys to position , position nothing but index
# # perpose:fast scalar access:at(label)iat(integars)
# print(df.iat[2,3])  #second indexrow column
# # fillna():
# print(df.fillna("example"))

# # replace():
# print(df.replace(to_replace="south",value="something"))
# print(df.replace(to_replace="south",value="something")["region"])
# # 5.shape:
# print(df.shape)     #returns the row and col count

# # 6.colums:
# print(df.columns)

# # 7.dtype:
# print(df.dtypes)

# # 8.object float int
# print(df["sales"])

# # print(df.info())
# # 1.astype
# df["quantity"]=df["quantity"].astype(float)
# print(df)
# df["profit"]=df["profit"].astype(str)
# print(df.info())

# new_df=df.rename(columns={"quantity":"quant"},inplace=True)
# print(new_df)

# df.rename(columns={"release_year":"year"},inplace=True)
# print(df)

# # #2. sort_values
# new_df=df.sort_values(by="sales",ascending=True)
# print(new_df)
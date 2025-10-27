import pandas as pd
# creating data set
# data={
#     "name":["aneela","akhila","nani","rani","usha","sunny"],
#     "age":[23,22,23,20,43,18],
#     "city":["hyd","vizag","delhi","khammam","rebm","hyderabad"]
# }
# d=pd.DataFrame(data)
# print(d)

df=pd.read_csv("./csv.csv")
# print(df.head())
# print(df.head(2))
# print(df.tail(2))
# print(df.tail(10))
# print(df.describe())
# print(df.shape)
# print(df[0:10:1])
# print(df["order_id"])
# print(df[["order_id","order_date"]])
# print[df[["order_id"]][0:10:1]]
# for rec in df.iterrows():
#     print(rec)
# print(df.loc[1])
# print(df.loc[20])
# print(df.loc[19,"sales"])
# print(df.loc[0:5])
# print(df.head)
# print(df.iloc[0:4]) #0to3 colems despily
# print(df.iloc[2,1])   #row noumbe of columen number


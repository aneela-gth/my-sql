import pandas as pd
df=pd.read_csv("./csv.csv")
# print(df.info())
# # 1.astype
# df["quantity"]=df["quantity"].astype(float)
# print(df)
# df["profit"]=df["profit"].astype(str)
# print(df.info())

# new_df=df.rename(columns={"quantity":"quant"},inplace=True)
# print(new_df)

# df.rename(columns={"release_year":"year"},inplace=True)
# print(df)

# #2. sort_values
# new_df=df.sort_values(by="sales",ascending=True)
# print(new_df)

# new_df=df.sort_values(by="category",ascending=False)
# print(new_df)

# cat=input("enter the category:")
# ordrer=input("ace or desc:")
# new_df=df.sort_values(by=cat,ascending=False)
# print(new_df)

# if "fales":
#     print("false")

# con="false"
# if con:
#     print("false")

# truthsy- numbers except 0,non empty string,true,{},(),[]
# falsy--0,"",false,{},(),[]

# print(bool("true"))


# 3.value_count
# print(df)
# print(df["sales"].value_count())

# 4.groupby()
# print(df.groupby("category"))

# 5.joines()
# merge()
# df_2=pd.read_csv(",/netflex_extra.csv")
# # print(df_2)
# print(df.merge(df_2,on="title"))
# print(pd.merge(df,df_2="title",how="inner"))
# print(pd.merge(df,df_2="title",how="left"))
# print(pd.merge(df,df_2="title",how="right"))
# print(pd.merge(df,df_2,how"cross"))

# concat()
# print(pd.concat([df,df_2]))         -----0 is horizonteal
# print(pd.concat([df,df_2],axis=1)) ------>1 data verticelly ga adda avuta

# df[["name_of_student1","student2"]][0:10:1]
# for rec in df.iterrows():
#     print(rec)
# print(df.loc[1])
# print(df.loc[20])
# print([df.iloc[0:5]])
# print(df.loc[0:5,"order_date"])
# print(df.loc[0:5,"order_date","sales"])
# print(df.head())
# print(df.loc[0:4,"order_date":"profit"])
print(df.iloc[0:4])


































# pivot_table----------------->reserch topic
# make a linked in post
# import pandas as pd

# data = {
#     'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT'],
#     'Employee': ['aneela', 'naresh', 'akhila', 'naveen', 'sunny', 'teja'],
#     'Salary': [5000, 6000, 4000, 4500, 7000, 7500],
#     'Bonus': [500, 600, 300, 350, 800, 900]
# }

# df = pd.DataFrame(data)
# print(df)
# pivot = df.pivot_table(values='Salary', index='Department', aggfunc='sum')
# print(pivot)
# pivot = df.pivot_table(values=['Salary', 'Bonus'], 
#                        index='Department', 
#                        aggfunc='mean')
# print(pivot)
# pivot = df.pivot_table(values='Salary', 
#                        index='Department', 
#                        columns='Employee', 
#                        aggfunc='sum')
# print(pivot)

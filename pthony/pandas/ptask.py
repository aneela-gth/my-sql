import pandas as pd
# 1.Load both CSVs into separate DataFrames.
df=pd.read_csv("./csv.csv")
print(df)

# 2.Display the first 5 rows of each DataFrame.
print(df.head(5))

# 3.Merge the two DataFrames on StudentID using an inner join.
# student1_df=pd.read_csv("./student1.csv")
# student2_df=pd.read_csv("./studen2.csv")
# merged_df = student1_df.merge(student2_df, on="StudentID",how="inner")
# print(merged_df)

# 4.Merge the two DataFrames using a left join.
# student1_df=pd.read_csv("./student1.csv")
# student2_df=pd.read_csv("./studen2.csv")
# print(student1_df.columns)
# print(student2_df.columns)
# # merged_df=student1_df.merge(student2_df,on="studentID",how="left")
# merged_df = student1_df.merge(student2_df, left_on="StudentID", right_on="ID", how="left")
# print(merged_df)


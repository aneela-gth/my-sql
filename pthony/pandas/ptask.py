

import pandas as pd

# 1.load both CSV s into separate dataframes
student_df=pd.read_csv("./student1.csv")
# print(student_df)

student_extra=pd.read_csv("./student2.csv")
print(student_extra)

# # 2.display the first 5 rows of each dataframe
print(student_df.head())

print(student_extra.head())

# #3.Merge the two DataFrames on StudentID using an inner join
inner_join=pd.merge(student_df,student_extra,on="StudentID",how="inner")
print(inner_join.head())

# # 4.Merge the two DataFrames using a left join
left_join=pd.merge(student_df,student_extra,on="StudentID",how="left")
print(left_join.head())

# # 5.Sort the merged DataFrame by Marks in descending order
sorted_df=left_join.sort_values(by="Marks",ascending=False)
print(sorted_df.head())

# # 6.Filter students who play Football
fp=left_join[left_join["Sports"]=="Football"]
print(fp)

# # 7.Filter students who have Marks > 85 and play Football
df=left_join[(left_join["Marks"]>85) & (left_join["Sports"]=="Football")]
print(df)

# # 8.Find how many students are there in each Class
# class_count=student_df["Class"].value_counts()
# print(class_count)

# # 9. Find the average Marks for each Club
avg=left_join.groupby("Group")["Marks"].mean()
print(avg)

# # 10. Find the student with the highest Attendance and display their Name, Marks, and Club
max_attendance= left_join.loc[left_join["Attendance"].idxmax(), ["Name", "Marks", "Group"]]
print(max_attendance)
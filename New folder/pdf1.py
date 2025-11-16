# Interview-Style Programming Questions: Basic Math and Logic
# 1. Area of Square
# Question: Calculate the area of a square. - Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25
# side=5
# area=side*side
# print(area)

# 2. Area of Rectangle
# Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24
# length=6
# breadth=4
# area = length*breadth
# print(area)

# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height. - Formula: Area = (1/2) × base × height - Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0
# base=8
# heigth=5
# area=(1/2)*base*heigth
# print(area)

# 4. Perimeter of Square
# Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - Side = 6 - Output: - Perimeter of square is: 24
# side=6
# Perimeter = 4*side
# print(Perimeter )

# 5. Perimeter of Rectangle
# Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) - Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16
# length=5
# breadth=3
# perimeter=2*(length+breadth)
# print(perimeter)

# 6. Perimeter of Triangle
# Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18
# side1=5
# side2=6
# side3=7
# perimeter=side1+side2+side3
# print(perimeter)

# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200

# toteal_amount=3700
# note_1000=toteal_amount//1000
# remining_after_1000=toteal_amount%1000
# note_500=remining_after_1000//500
# remaining=remining_after_1000%500
# print("1000s:", note_1000)
# print("500s:", note_500)
# print("Remaining:", remaining)

# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
# total_seconds=3672
# hours=total_seconds//3600
# remaining_second=total_seconds%3600
# minutes=remaining_second//60
# seconds=remaining_second%60
# print("Hours:", hours)
# print("Minutes:", minutes)
# print("Seconds:", seconds)

# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263
# m=85
# p=90
# c=88
# total=m+p+c
# print("Total marks:", total)

# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67
# m=85
# p=90
# c=88
# average=(m+p+c)/3
# print("average:",average)
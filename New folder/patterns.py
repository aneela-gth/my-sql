# Pattern-Based Programming Questions (All 35 Questions - Interview Style)
# 🔷 Square, Rectangle, and Triangle Patterns (1–15)
# 1.	Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()
# 2.	Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *
# n=3
# for i in range(1,n+1):
#     for j in range(1,2*n+1):
#         print("*",end=" ")
#     print()

# 3.	Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# 4.	Right-Angled Triangle (Right-Aligned)
# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# 5.	Inverted Triangle (Left-Aligned)
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
# 6.	Inverted Triangle (Right-Aligned)
# n = 5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# 7.	Centered Pyramid Pattern
# n = 6
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i-1):
#         print("*",end=" ")
#     for m in range(i):
#         print("*",end=" ")
#     print()

# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *
# 8.	Diamond Pattern
# n = 5

# for i in range(n,0,-1):
#     for k in range(n-i):
#         print("",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     for m in range(i):
#         print("*",end=" ")
#     print()
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *
# 9.	Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *
# 10.	Left-Aligned Half Diamond
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# 11.	Right-Aligned Half Diamond
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
# 12.	Sandglass Pattern
# Input: n = 4
# Output:
# * * * *
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *
# 13.	Increasing Width Triangle
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# 14.	Decreasing Width Triangle
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
# 15.	Right-Aligned Hill Pattern
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
# ________________________________________
# 🔲 Hollow Patterns (16–25)
# 16.	Hollow Square Pattern
# Problem: Print a hollow square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *

# n = 5
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print("* " * n)
#     else:
#         print("* " + "  " * (n - 2) + "*")


# 17.	Hollow Rectangle Pattern
# Problem: Print a hollow rectangle of m rows and n columns.
# Input: m = 4, n = 5
# Output:
# * * * * *
# *       *
# *       *
# * * * * *
# n=6
# for i in range(n):
#     if i==0 or i==n - 1:
#         print("* " * n)
#     else:
#         print("* "+"  "*(n - 2)+ "*")

# 18.	Hollow Right-Angled Triangle (Left-Aligned)
# Input: n = 5
# Output:
# *
# * *
# *   *
# *     *
# * * * * *

# n=5
# for i in range(1, n+1):
#     if i==1 or i==n:
#         print("* "* i)
#     else:
#         print("*"+" " * (2 * i - 3)+ "*")

# 19.	Hollow Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     *   *
#   *     *
# * * * * *

# n=5
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "* i)
#     else:
#         print("*"+" " * (2 * i - 3)+ "*")



# 20.	Hollow Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# *     *
# *   *
# * *
# *
# 21.	Hollow Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   *     *
#     *   *
#       * *
#         *
# 22.	Hollow Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     *   *
#   *       *
# * * * * * * *
# 23.	Hollow Diamond Pattern
# Input: n = 3
# Output:
#     *
#   *   *
# *       *
#   *   *
#     *
# 24.	Hollow Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# *   *   *
# *       *
# *   *   *
# * *   * *
# *       *
# 25.	Hollow Hourglass Pattern
# Input: n = 5
# Output:
# * * * * *
# *       *
#   *   *
#     *
#   *   *
# *       *
# * * * * *
# ________________________________________
# 🔢 Number-Based Patterns (26–35)
# 26.	Increasing Number Triangle
# Problem: Print numbers from 1 to n in triangle form.
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 27.	Repeating Row Number Triangle
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(i,end=" ")
#     print(i)
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 28.	Continuous Number Triangle
# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 29.	Reverse Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 30.	Inverted Number Triangle
# Input: n = 5
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# 31.	Right-Aligned Number Triangle
# Input: n = 5
# Output:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# 32.	Pyramid Number Pattern
# Input: n = 4
# Output:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
# 33.	Even Number Triangle
# Input: n = 5
# Output:
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# 34.	Odd Number Triangle
# Input: n = 5
# Output:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# 35.	Pascal’s Triangle
# Input: n = 5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# ________________________________________
# ✅ All 35 pattern questions are now fully formatted in an interview-style layout with problem statements, inputs, and expected outputs.
# Would you like to:
# •	🐍 Add Python code for each?
# •	📥 Export as a PDF?

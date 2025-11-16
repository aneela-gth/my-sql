# # 1.	Solid Square Pattern
# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()

# # 2.	Solid Rectangle Pattern
# for i in range(1,2*5):
#     for j in range(1,2*5):
#         print("*",end=" ")
#     print()

# # 3.	Right-Angled Triangle (Left-Aligned)
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# # 4.	Right-Angled Triangle (Right-Aligned)
# n=5
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ",)
#     for k in range(i):
#         print("*",end=" ")
#     print()

# # 5.	Inverted Triangle (Left-Aligned)
# n=6
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print("*",end=" ")
#     for k in range(i):
#         print(end=" ")
#     print()

# # 6.	Inverted Triangle (Right-Aligned)
# n=5
# for i in range(n,0,-1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# # 7.	Centered Pyramid Pattern
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("",end=" ")
#         for i in range(i-5):
#             print("*",end=" ")
#     for k in range(i-4):
#         print("*", end=" ")
#     print()

# # 26.	Increasing Number Triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print(i)
# # 27
# m=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# m=5
# count=0
# for i in range(1,m+1):
#     for j in range(i):
#         print(i,end=" ")
#         count+=1
#     print(count)


# # 1.	Solid Square Pattern
# n=5
# for i in range(5):
#     for j in range(1,5+1):
#         print("*",end=" ")
#     print()

# # 2.	Solid Rectangle Pattern
# n=5
# for i in range(n):
#     for j in range(1,2*5):
#         print("*",end=" ")
#     print()

# # 3.	Right-Angled Triangle (Left-Aligned)
# n=6
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     for k in range(i):
#         print(" ",end=" ")
#     print()

# # 4.	Right-Angled Triangle (Right-Aligned)
# n=6
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# # 5.	Inverted Triangle (Left-Aligned)
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# # 6.	Inverted Triangle (Right-Aligned)
# n=5
# for i in range(n,0,-1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# # 7.	Centered Pyramid Pattern
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i-1):
#        print("*",end=" ")  
#     for m in range(i):
#        print("*",end=" ")  
#     print()

# # 8.revers Pyramid Pattern
# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i-1):
#        print("*",end=" ")  
#     for m in range(i):
#        print("*",end=" ")  
#     pr


# # 8.	Diamond Pattern
# n=3
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i-1):
#        print("*",end=" ")  
#     for m in range(i):
#        print("*",end=" ")  
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i-1):
#        print("*",end=" ")  
#     for m in range(i):
#        print("*",end=" ")  
#     print()

# # 9.	Butterfly Pattern
# n=3
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i-1):
#        print("*",end=" ")  
#     for m in range(i):
#        print("*",end=" ")  
#     print()

# n=5
# for i in range(n,n+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# # 26.	Increasing Number Triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print(i)
 
# # 27.	Repeating Row Number Triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(i,end=" ")
#     print(i)

# # 29.	Reverse Row Number Triangle
# n=5
# i_count=1
# for i in range(n):
#     for j in range(1,i):
#         print(i,end=" ")
#         i_count+=1
#     print(i)

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


# puse pattern+
# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n):
#          print(" ",end=" ")
#     for m in range(n+1):
#          print("*")
#     for k in range(1,j-1):
#          print("*",end=" ")
#     print()

# a="1.1.1.1.1.1"
# b=""
# for i in a:
#     if i==".":
#         b+="*"
#     else:
#         b+=i
# print(b)
        

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        s+=str(i)+" "
    print()
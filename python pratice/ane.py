# a=2
# b=3
# temp=a
# b=a
# temp=b
# a,b=b,a
# print("aftear swapping:a=",a,"b=",b)

# n=5
# for i in range(1,n+1):
#     s=""
#     for j in range(1,n+1):
#         if j==1 or j==n or i==(n//2)+1:
#           s+="*"+" "
#         else:
#            s+=" "+" "
#     print(s)          

# n=5
# for i in range(n):
#     s=""
#     for j in range(n):
#         if(i==0 or j==(n//2)):
#             s+="* "
#         else:
#             s+="  "
#     print(s)

n=5
for i in range(n):
    s=" "
    for j in range(1,n+1):
        if(i==0 or i==n+1 or i==n or j==n-i or j==(n+1//2)+1):
          s+="*"+" "
    else:
        s+=" "
    print(s)
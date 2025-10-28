# a=[1,2,3,4,5]
# print(a)

# x=[1,9,2,34,5,6,7,8]
# print(x[3])

# y=[1,2,3,4,5,6,7]
# y[2]=10
# print(y)

# y=[1,2,3,4,5,6,7]
# print(len(y))

# y=[1,2,3,4,5,6,7]
# y.append(30)
# print(y)

# y=[1,2,3,4,5,6,7]
# y.insert(2,10)
# print(y)

# x=[1,2,3,4,5,6]
# x.remove(3)
# print(x)

# x=[1,2,3,4,5,6]
# x.pop(4)
# print(x)

# x=["apple","banana","mango"]
# if "mango" in x:
#     print("mango is in the list")
# else:
#     print("mango is not in the list")

# names=["aneela","akhila","usharani","hirapaya"]
# for names in names:
#     print(names)

# inermediate level
# 1.Combine two lists using + or extend().
# x=[1,2,3,4]
# y=[5,6,7,8]
# x.extend(y)
# print(x)

# 2.Sort a list in ascending and then descending order.
# x=[2,5,0,7,9,1,4,8,7]
# x.sort()
# print(x)

# x=[2,5,0,7,9,1,4,8,7]
# x.sort(reverse=x)
# print(x)

# 3.Reverse a list using reverse() and slicing [::-1].
# x=[10,20,30,40,50]
# x.reverse()
# print(x)
# x=[10,20,30,40,50]
# revers=x[::-1]
# print(revers)
# x="hello"
# revers=x[::-1]
# print(revers)


# class student:
#     id=102
#     name="aneela"
#     age=23
#     place="khammam"
#     course="pythonfull stack"
#     def sleep(self):
#         print("student is sleeping")
#     def eat(self):
#         print("student is eating")
#     def study(self):
#         print("student is studding")
# stu=student()
# print(stu.name)
# print(stu.age)
# print(stu.place)
# print(stu.id)
# stu.sleep()
# stu.eat()


# class student:
#     id=102
#     name="aneela"
#     age=23
#     place="khammam"
#     course="pythonfull stack"
#     def datails(self):
#         print(f"id:{self.id},name:{self.name},age{self.age}")
#     def sleep(self):
#         print("student is sleeping")
#     def eat(self):
#         print("student is eating")
#     def study(self):
#         print("student is studding")
# stu=student()
# print(stu.name)
# print(stu.age)
# print(stu.place)
# print(stu.id)
# stu.sleep()
# stu.eat()

# class car:
#     name="beinze"
#     color="black"
#     speed="100km"
#     range="50k"
#     cost="50lakes"
#     def car_detiles(self):
#         print(f"name:{self.name},color:{self.color},speed:{self.speed},range:{self.range},cost:{self.cost}")
#     def car_start(self):
#         print("engean is started")
#     def car_stop(self):
#         print("engean is stoped")
# c=car()
# print(c.name)
# print(c.color)
# print(c.speed)
# c.car_detiles()
# c.car_start()
# c.car_stop()

# class employes:
#     id=102
#     name="aneela"
#     salarly="50k"
#     role="software"
#     compnye_name="wipro"
#     age=23
#     exprence="2eyers"
#     def detils(self):
#         print(f"id:{self.id},name:{self.name},age:{self.age},salarly:{self.salarly},compnye_name:{self.compnye_name},exprence:{self.exprence}")
#     def work(self):
#         print("employe is creat a website")
#     def project(self):
#         print("employe developed a project")
#     def role(self):
#         print("compnye name  based on the work")
# emp=employes()
# emp.detils()
# emp.work()
# emp.project()
# emp.role()

# name="madam"
# str=""
# for i in name:
#     str=str+i
# print(str)

# num=321
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# num=567
# rev=0
# while num>0:
#     term=num%10
#     rev=rev*10+term
#     num=num//10
# print(rev)

# num=126
# sum=0
# while num!=0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)

# num=121
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if(rev==temp):
#     print("palindrom")
# else:
#     print("not palindrom")

# name="aneela"
# rev=""
# for i in name:
#     rev=i+rev
# print(rev)
# num=6
# sum=0
# for i in range(1,num):
#     if num%i==0:
#      sum=sum+i
# if num==sum:
#     print("perfect number")
# else:
#     print("not perfect")


# str="hello"
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)

# num=12543
# e_count=0
# od_count=0
# while num!=0:
#     temp=num%10
#     if temp%2==0:
#        e_count+=1
#     else:
#         od_count+=1
#     num=num//10
# print(e_count)
# print(od_count)

# n=int(input("entear a numbear"))
# if(n>0):
#     print("positive")
# elif(n<0):
#     print("negitive")
# else:
#     print("zero")


# num=143
# sum=0
# temp=num
# digit=len(str(num))
# while temp>0:
#     rem=temp%10
#     sum+=rem**digit
#     temp=temp//10
# if(sum==num):
#     print("amgstrong")
# else:
#     print("not an amstronge")

# num=121
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if(rev==temp):
#     print("palindrom")
# else:
#     print("not a palindrom")

# name="madam"
# rev=""
# for i in name:
#   rev=i+rev
# if(rev==name):
#   print("palindrom")
# else:
#   print("not palindrom")








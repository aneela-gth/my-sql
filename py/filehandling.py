#1.red file
x=open("./sample.txt",'r')
data=x.read()
print(data)
#write file
x=open("./sample.txt",'w')
x.write("hellow world")
#read file
x=open("./sample.txt",'r')
data=x.read()
print(data)
print(x.closed)
x.close()
print(x.closed)
with open("./sample.txt",'r')as f:
  data=f.read()
  print(data)
  print(f.closed)
print(f.closed)

with open("./sample.txt",'w')as f:
  f.write("hello world weloceme")
with open("./sample.txt",'r')as f:
  data=f.read()
  print(data)

with open("./sample.txt",'a')as f:
    f.write("\naneela")
with open("./sample.txt",'r')as f:
    data=f.read()
    print(data)

with open("./demo.txt",'w') as f:
    f.write("good evening")
    print(f.readable())
with open("./demo.txt",'r')as f:
    data=f.read()
    print(data)
    print(f.readable())

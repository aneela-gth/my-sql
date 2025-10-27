#add country code to phone numbers
def process(fun,x):
    result=[]
    for i in x:
        op=fun(i)
        result.append(op)
op=map(lambda x:'+91'+x,['9874563214','9632587410','9784563210'])
print(list(op))

#convert prices from dollars to rupees
op=map(lambda x:x*83,[10,20,40,100])
print(list(op))

#filter gmail ids
op=filter(lambda x:"@gmail.com"+x,["harish@gmail.com","acd@yahoo","xyz@gail.com"])
print(list(op))
# get short prodct names
op=filter(lambda x:len(x)<5,['pen','Notebook','laptop','charger','bag'])
print(list(op))
#filter expired products
op=filter(lambda x:'current year=2025',[2022,2023,2024,2025])
print(list(op))
#mask credit card numbers
op=map(lambda x:''+str(x)[-4:],[321456987,789654123,456321789])
print(list(op))

#filter high saiary employees

op = filter(lambda x: x >= 40000, [25000, 45000, 60000, 15000, 80000])
print(list(op))
#format product labels
op=map(lambda x: 'product:apple'+x,["apple","mango","orange"])
print(list(op))
#students passed
op=filter(lambda x: x >=40,[35,80,55,20,90])
print(list(op))
#filter strong passwords
op = filter(lambda x: len(x) >= 8 and ('@' in x or '&' in x),
            ["abc123", "admin@123", "hello", "pa$$word"])

print(list(op))




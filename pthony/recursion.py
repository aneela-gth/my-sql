#recursion
def open_giftbox(n):
    if n>1:
        open_giftbox(n-1)
    else:
        print('gift found')
open_giftbox(5)

def open_giftbox(n):
  if n>1:
    print(f'box{n}is opened')
    open_giftbox(n-1)
  else:
    print(f'gift found in box{n}')
open_giftbox(5)

#factorieal of recursion
def factorial(n):
   fact=1
   if n==1 or n==0:
      return fact
   else:
      factorial_n=n*factorial(n-1)
      return factorial_n
print(factorial(5))

#is instance
x=[1,2,3,[4,5,6]]
sum=0
for val in x :
   if isinstance (val,list):
      for i in val:
         sum+1
      else:
         sum+=val
         print(sum)
#fibonacci serious using recursion
def f(n):
   if n<=0:
      return 0
   elif n==1:
      return 1
   else:
      return f(n-1)+f(n-2)
terms=int (input('enter into number'))
print("fiboncci serirs")
for i in range(terms):
      print(f(i),end=" ")
       
   

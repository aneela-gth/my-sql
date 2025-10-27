#nameerror:
try:
  print(x)
except NameError:
  print("name is not courect")
#type error:
try:
  x=2
  y='hello'
  print(x+y)
except TypeError:
  print("values are not match")
#zero divigion error:
try:
  x=3
  y=0
  print(x/y)
except ZeroDivisionError:
  print("divizon is not defied")
#value error:
try:
   x=int(input('enter a number'))
   y=int(input("enter a number"))
   print(x+y)
except ValueError:
  print("choose the currect value in the input")
#indentaction erroe:
try:
 a=[7,8,9]
 print(a[6])
except IndentationError:
  print("index is out of range")
#attribut error:
try:
 x=4
 x.append(13)
 print(x)
except AttributeError:
  print('this method is not avilable') 
#key error:
try:
  dict={'name':'aneela','age':23}
  print(dict['city'])
except KeyError:
  print('key is not avaiblr in the given dictonery')
#file not found:
try:
 open('./aneela','r')
except FileNotFoundError:
 print('file not error')
#module error:
try:
 import some
except ModuleNotFoundError:
 print('module is not available')
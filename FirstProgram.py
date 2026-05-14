print("Hello world", "this is ronak")
print("this is ronak")
print (23)
print(23+35)
print(23.23)
name = "Ronak"
age = 23
price = 23.99
name2 = name
print("My name is : ",name2)
print("My age is : ",age)
print("price is : ",price)

print(type(name))
print(type(age))
print(type(price))

name1 = "Ronak"
name2 = 'Ronak'
name3 = '''Ronak'''

print(name1)
print(name2)
print(name3)

age5 = 233
old = False
a = None
print(type(old))
print(type(a))

a = 2
b = 5
print("Sum = ",a+b)

A, B = 2,3
Txt = "@"
print(2*Txt*3)

A,B="2",3
Txt= "@"
print((A+Txt)*B)

A,B = 2,3
C = 4
print(A+B*C)

A, B = 10, 5.0
C = A*B
print(C)



A, B = 1, 2
C = A/B
print(C)


A,B = 1.5,3
C = A//B
print(C,A/B)

A,B=12,5
C = A//B
print(C)

A,B=-12,5
C = A//B
print(C)

A,B=12,-5
C = A//B
print(C)

A,B=-5,2
C = A%B
print(C)

A,B=5,2
C = A%B
print(C)

A,B=5,-2
C = A%B
print(C)

#Taking input form user & printing it
""""
name = input("name : ")
age = int(input("age : "))
price = float(input("price  : "))

print ("My name is", name, "and I am", age, "year old")
"""

"""
light = input("light color : ")
if(light == "red"):
  print("stop")
elif(light == "yellow"):
  print("look")
elif(light == "green"):
  print("go")
else:
  print("light is broken")
"""

"""
marks = int(input("marks : "))
if(marks >= 90):
  print("A")
elif(marks >= 80 and marks < 90):
  print("B")
elif(marks >= 70 and marks < 80):
  print("C")
else:
  print("D")
  """
"""
A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
  print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
  print("fee is 200")
elif(A == 5 and G =="M"):
  print("fee is 300")
else:
  print("no fee")
  """

a =  float(input("a  : "))
b =  float(input("b  : "))
c =  float(input("c  : "))
print(a*b*c/100)

p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (p*r*t)/100
print(si)
#str1 = "This is a string.\nwe are creating it in python."
#print (str1)
"""
str1 = "Ronak"
str2 = "Tailor"
print (str1+str2)
print (len(str1+str2))

str = "apna college"
#ch =  str[0]
#print(ch)
print(str[0:12])
print(str[:4]) #[0:4]
print(str[5:]) #[5 :len(str)]

str3 = "apple"
print(str3[-3:-1])
"""

"""
str = "i am studing python form apnacollege"
print(str.endswith("ege"))
print(str.capitalize())
print(str)
print(str.replace("python", "javascript"))
print(str.find("o"))
print(str.count("o"))
"""

# Q => wap to input user's first name & print its lenght.

#name = input("Enter your name : ")
#print("length of your name is ",len(name))

# Q => wap to find the occurence of '$' in a string

"""
str = "Hi, $Iam the $ symbol $99.99"
print(str.count("$"))

light = "red"

if(light == "red"):
  print("stop")
elif(light == "yellow"):
  print("look")
elif(light == "green"):
  print("go")
else:
  print("light is broken")

num = 5

if(num > 2):
  print("greater than 2")
elif (num > 3):
  print("greater than 3")


age = 24

if( age>= 18):
  print("can vote") #indentation
else:
  print("canot vote")

marks = int(input("Enter a number : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student -> ", grade)
"""
age = 34

#nesting 
"""
if(age >= 18):
   if(age >= 80):
      print("cannot drive")
   else:
      print("can drive")
else:
   print("cannot drive")
  """    

# Q wap to check if a number entered by the user is odd or even   

"""   
num = int(input("Enter the number : "))
print("given number is ")
if(num%2==0):
   print("Even")
else:
   print("odd")
"""

# Q wap to find the greatest 3 number entered by the user.

"""
a =  int(input("Enter the number a : "))
b =  int(input("Enter the number b : "))
c =  int(input("Enter the number c : "))

if(a>=b & a>=c):
  print("A is greatest")
elif(b>=c):
  print("B is greatest")
else:
  print("C is greatest")

"""

"""
a =  int(input("Enter the number a : "))
b =  int(input("Enter the number b : "))
c =  int(input("Enter the number c : "))
d =  int(input("Enter the number d : "))

if(a>=b & a>=c & a>=d):
  print("A is greatest")
elif( b>=c & b>=d):
  print("B is greatest")
elif (c>= d):
  print("C is greatest")
else:
  print("D is gretest")
  """


# Q wap to check if a number is a multiple of 7 or not

num = int (input("Enter a number : "))

if(num%7==0):
  print("number if multiple of 7 ")
else:
  print("not multiple of 7 ")
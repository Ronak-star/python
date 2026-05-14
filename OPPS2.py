'''class student:
  def __init__(self, name):
    self.name = name
  
s1 = student("Ronak")
print(s1.name)
del s1.name
print(s1.name)

'''
# private attribute
'''
class Account:
  def __init__(self, acc_no, acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass

  def reset_pass(self):
    print(self.__acc_pass)

acc1 = Account("123456", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())
'''

'''
class person:
  __name = "anonymous"

  def __hello(self):
    print("hello person!")
  
  def welcome(self):
    self.__hello()

p1 = person()
print(p1.welcome())
'''

#  singel inheritance

'''

class car:
  color = "black"
  @staticmethod
  def start():
      print("car started..")
  
  @staticmethod
  def stop():
      print("car stopped.")

class Toyotacar(car):
   def __init__(self, name):
       self.name = name
      

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.color)
'''

# multi level inheritance

'''
class car:

  @staticmethod
  def start():
      print("car started..")
  
  @staticmethod
  def stop():
      print("car stopped.")

class Toyotacar(car):
   def __init__(self, brand):
       self.brand = brand
      
class Fortuner(Toyotacar):
   def __init__(self, type):
       self.type = type

car1 = Fortuner("diesel")
car1.start()
'''

# multiple inheritance

'''
class A:
  varA = "welcome to class A"

class B:
  varB = "welcome to class B"

class C(A, B):
  varC = "welcome to class C "

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
'''

# super method

'''
class car:
  def __init__(self, type):
    self.type = type
  
  @staticmethod
  def start():
      print("car started..")
  
  @staticmethod
  def stop():
      print("car stopped.")

class Toyotocar(car):
   def __init__(self, name, type):
       super().__init__(type)
       self.name = name
       super().start()
     

car1 = Toyotocar("prius", "electric")
print(car1.type)
'''

'''
class person:
  name = "anonymous"

  #def changeName(self, name):
  #  self.__class__.name = "Rahul"

  @classmethod
  def changeName(cls, name):
    cls.name = name

p1 = person()
p1.changeName("rahul kumar")
print(p1.name)
print(person.name)
'''


'''
class student:
  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math
#def calcpercentage(self):
#    self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

  @property
  def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = student(98, 97, 99)
print(stu1.percentage) 

stu1.phy = 86
print(stu1.percentage)
'''

# polymorphism : operator overloading

'''
class complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img

  def showNumber(self):
    print(self.real,"i +", self.img,"j")
  
  def __add__(self, num2):
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return complex(newReal, newImg)
  
  def __sub__(self, num2):
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return complex(newReal, newImg)


num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()
#num3 = num1.add(num2)
#num3.showNumber()
'''

# Q => Define a Circle class to create with radius r uing the constuctor Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

'''
class circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return(22/7) * self.radius ** 2
  
  def perimeter(self):
    return 2 * (22/7) * self.radius

c1 = circle(21)
print(c1.area())
print(c1.perimeter())
'''

# Q => Define a Employee class with attributes role, department & salary. This class also a showDetails() method . create an Engineer class that inherits properties from Employee &  has additional attrubutes : name & age.

'''
class Employee:
  def __init__(self, role, dept, salary):
    self.role = role
    self.dept = dept
    self.salary = salary

  def showDetails(self):
    print("role = ",self.role)
    print("dept = ",self.dept)
    print("salary = ", self.salary)

class Engineer(Employee):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()
'''

# Q => create a class called order which stores itme & price. use dunder function__gt__() to convey that: order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)
    
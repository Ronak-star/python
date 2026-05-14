#class Student:
#  name = "Karan"
#s1 = Student()
#print(s1.name)
#
#s2 = Student()
#print(s2.name)


#class car:
#  color = "Black"
#  brand = "merecedes"
#car1 = car()
#print(car1.color)
#print(car1.brand)

"""
class Student:
 # default constructors
 def __init__(self):
     pass
 # parameterized constructors
 def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print("adding new student in database..")


s1 = Student("karan",97)
print(s1.name, s1.marks)

s2 = Student("arjun",88)
print(s2.name,s2.marks)
"""

"""
class Student:
     college_name = "Arya college"
 
     def __init__(self, name, marks):
             self.name = name
             self.marks = marks
             print("adding new student in database..")

     def welcome(self):
       print("welcome student,", self.name)
   
     def get_marks(self):
      return self.marks

s1 = Student("karan",97)
print(s1.name, s1.marks)

s2 = Student("arjun",88)
print(s2.name,s2.marks)

print(s2.college_name) 
s1.welcome()
print(s1.get_marks())

"""

# Q => create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average

"""
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is :", sum / 3)

s1 = student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()

"""


# static method

"""
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
   
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is :", sum / 3)

s1 = student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()
s1.hello()
"""
# Abstraction

'''
class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False

  def start(self):
       self.clutch = True
       self.acc = True
       print("car started..")

car1 = Car()
car1.start()  
'''

# Q => Create Account class with 2 attrubutes - balance & account no. Create methods for dibit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    # balance check
    def get_balance(self):
        return self.balance


acc1 = Account(100000, 1234567)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
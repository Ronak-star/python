# Random number generator

'''
import random

target = random.randint(1, 100)

while True:
  userChoice = input("Guess the target or Quit : ")
  if(userChoice == "Quit"):
    break

  userChoice = int(userChoice)
  if(userChoice == target):
    print("Sucesss : Correct Guess!!")
    break
  elif(userChoice < target):
    print("Your number was too small. Take a bigger guess..")
  else:
    print("your number was too bin. Take a small guess..")

print("----GAME OVER----")
'''

# Random password Generator

import random
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])

# password = ""
# for i in range(pass_len)
#    password += random.choice(charValues)


print("your random password is: ",password)
# 1. While Loop
#count = 1
#while count <= 5 :
#  print("hello")
#  count += 1
#
#  print(count)

#i = 1
#while i<=10:
#  print("Ronak",i)
#  i += 1

#i = 1
#while i<=10:
#  print(i)
#  i += 1

# Q=> print numbers from 1 to 100

#i = 1
#while i<=100:
#  print(i)
#  i += 1

# Q => print number form 100 to 1.

#i = 100
#while i>=1:
#  print(i)
#  i -= 1

# Q => print the multiplicatin table of a number n.

#num = int(input("Enter the number : "))
#print("The table is : - ")
#i = 1
#while i<=10:
#  print(num*i)
#  i += 1

# Q => print the element of the following list using loop:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#idx = 0
#while idx < len(nums):
#  print(nums[idx])
#  idx += 1

# Q => Search for a number x in this tuple using loop:(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


#nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#x = 36
#i = 0 # initialization
#while i<len(nums):
#  if(nums[i] == x):
#      
#      print("found at  index", i)
#      break
#  else:
#     print("finding..")
#  i += 1

#i = 1
#while i<= 5:
#  print(i)
#  if(i == 3):
#     break
#  i += 1



#i = 0
#while i<= 10:
# 
#  if(i%2== 0):
#     i += 1
#     continue
#  print(i)
#  i += 1
#
#
#i = 0
#while i<= 10:
# 
#  if(i%2!= 0):
#     i += 1
#     continue
#  print(i)
#  i += 1


# for loop

#nums = [1, 2, 3, 4, 5]
#
#for val in nums:
#  print(val)

#str = "apnacollege"
#
#for char in str:
#     if(char == 'o'):
#         print("o is found")
#         break
#     print(char)
#else:
#  print("end")

# Q => print the elements of the following list using loop:
 # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#for el in nums:
#  print(el)

  # Q => Search for a number x in this tuple using loop:(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

#nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#x = 36
#idx = 0
#for el in nums:
#      if(el == x):
#         print("founded",idx)
#         break
#      idx += 1
   
#for i in range(10): # range(stop)
#  print(i)

#for i in range(2, 10): # range(star, stop)
#  print(i)

#for i in range (2, 10, 2): #range(start, stop, step)
#  print(i)

# Even number
#for i in range(2, 100, 2):
#  print(i)
#
## Odd number
#for i in range(1, 100, 2):
#  print(i)

# Q => print numbers from 1 to 100

#for i in range(1,101,1):
#  print(i)

# Q => print number from 100 to 1.

#for i in range(100,0,-1):
#  print(i)

# Q=> print the multiplication table of a number n.
#n = int (input("Enter the nummber: "))
#
#for i in range (1,11):
#  print(n*i)

# pass statement

#for i in range(5):
#  pass
#print("some useful work")

# Q => wap to find the sum of first n number. (using while)

#n = int(input("Enter the number : "))
#
#sum = 0
#for i in range (1, n+1):
#   sum += i
#
#print("total sum = ",sum)


#n = 7
#sum = 0
#i = 1
#while i<= n:
#  sum += i
#  i += 1
#print("Total sum = ",sum)

# Q => wap to find the factorial of first n numbers. (using for)

#n = int(input("Enter the numner : "))
#fact = 1
#i = 1
#while i<=n:
#    fact *= i
#    i += 1
#print("factorial is = ",fact)

n = int(input("Enter the number : "))

fact = 1
for i in range(1, n+1):
  fact *= i
  print("factorial is = ",fact)
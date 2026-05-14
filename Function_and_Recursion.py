#def cal_sum (a,b):
#  sum = a + b
#  print(sum)
#  return sum
#
#cal_sum(5,10)
#cal_sum(2,10)
#cal_sum(12,17)

# function definition
#def calc_sum(a, b): # parameters
#  return a + b
#sum = calc_sum(1, 2) # function call; arguments
#print(sum)

#def print_hello():
#  print("hello")
#print_hello()
#print_hello()
#
#output = print_hello()
#print(output)

# average of 3 numbers
#def calc_avg(a, b, c):
#   sum = a + b + c
#   avg = sum/3
#   print(avg)
#   return avg
#
#calc_avg(98, 97, 95)

#print("apnacollege", end=" ") # sep = " "
#print("shradhaKhapra") #end = "\n"

#def cal_prob (a = 1, b = 2):
#  print(a*b)
#  return a* b
#cal_prob()

# Q => wap to print the lenght of a list (list is the parameter)

#cities = ["delhi", "gurganon", "noida", "pune","mumbai",#"chennai"]
#heroes = ["thor",  "ironman", "captain america", "shaktiman"]
#
#def print_len(list):
#  print(len(list))
#
#print_len(cities)
#print_len(heroes)

# Q => wap to print the elements of a list in a single line.(list is the parameter)

#cities = ["delhi", "gurganon", "noida", "pune","mumbai",#"chennai"]
#heroes = ["thor",  "ironman", "captain america", "shaktiman"]
#
#def print_len(list):
#  print(len(list))
#
#def print_list(list):
#  for item in list:
#    print(item, end=" ")
#print_list(heroes)
#print_list(cities)

# Q => wap to find the factorial of n. (n is the parameter)

#def fact_calc(n):
#  fact = 1
#  for i in range (1, n+1):
#    fact *= i
#    print(fact)
#  
#fact_calc(7)

# Q => wap to convert USD to INR.

#def converter(usd_val):
#  inr_val = usd_val * 95.68
#  print(usd_val, "USD = ",inr_val, "INR")
#
#converter(100)

#def number(n):
#   if(n%2==0):
#     
#      print("Even")
#   
#   else:
#    print("odd ")
#
#number(14)


# Rucurence function

#def show(n):
#  if(n == 0):
#    return
#  print(n)
#  show(n-1)
#
#show(5)

#def fact(n):
#  if(n ==0 or n ==1):
#    return 1
#  else:
#    return fact(n-1)*n
#print(fact(5))

# Q => write a recursive function to calculate the sum of first n natural numbers.



#def calc_sum(n):
#  if(n == 0):
#     return 0
#  return calc_sum(n-1) + n
# 
#sum = calc_sum(5)
#print(sum)

# Q => write a recursice function to print all elements in a list. hint: use list & index as parameters.

def print_list(list, idx=0):
  if(idx == len(list)):
    return
  print(list[idx])
  print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)
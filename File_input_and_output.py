#f = open("demo.txt","a")
#data = f.read()
##print(data)
##print(type(data))
#line1 = f.readline()
#print(line1)
#
#line2 = f.readline()
#print(line2)
#
#line3 = f.readline()
#print(line3)

#f.write("\nthen I will move to reactjs")
#f.close() 

#f = open("demo.txt","r+")
#f.write("abc")
#print(f.read())
#f.close()

#with open("demo.txt", "r") as f:
#  data = f.read()
#  print(data)
#
#with open("demo.txt", "w") as f:
#  f.write("new data")

#import os
#os.remove("sample.txt")


# Q => create a new file "practice.txt" using python. Add the follwing data in it:
# Hi everyone 
#we aer learning File I/O
#using java.
#I like programming in java.

#with open("practice.txt","w") as f:
#  f.write("Hi everyone\n we are learning File I/O\n")
#  f.write("using java.\n I like programming in java.")

# Q => wap that replace all occurences of "Jaca " with "python " in above file.

#with open("practice.txt","r") as f:
#  data = f.read()
#
#new_data = data.replace("java", "pyrthon")
#print(new_data)
#
#with open("practice.txt", "w") as f:
#  f.write(new_data)

# Q => seach if the word "learning" exist in the file or not.

#word = "learning"
#with open("practice.txt", "r") as f:
#  data = f.read()
#  if(data.find(word) != -1):
#    print("found")
#  else:
#    print("not found")

# Q => wap to find in which line of the file does the word "learning" occur first. 
# print -1 if word not found

"""
def check_for_line():
  word = "programming"
  data = True
  line_no = 1
  with open("practice.txt", "r") as f:
    while data:
      data = f.readline()
      if(word in data):
         print(line_no)
         return
      line_no += 1

      return -1
      
  print(check_for_line())

  """

#Q => from a file containing number separated by comma, print the count of even number.
count = 0
with open("practice.txt", "r" ) as f:
  data = f.read()

  nums = data.split(",")
  for val in nums:
    if(int(val) % 2 == 0):
      count += 1

print(count)
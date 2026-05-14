"""marks = [94.4, 84.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1:4])
print(marks[-3:-1])

student = ["karan", 95.52, 17, "delhi"]
print(student[0])
student[0] = "arjun"
print(student)

"""
"""
list = [2, 1, 3, 1]
#list.append(4)
#print(list.sort(reverse=True))
#print(list)
#list.insert(1,5)
list.pop(2)
print(list)

tup = (2, 1, 3, 1)
print(type(tup))
print(tup.index(2))

"""
# Q => wap to ask the user to enter names of their 3 favorite movies & store them in a list

"""
movies = []
mov1 = input("Enter 1st movie : ")
mov2 = input("Enter 2st movie : ")
mov3 = input("Enter 3st movie : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
"""

# Q => wap to check if a list contains a palindrome of elements. (hint: use copy() method)

"""
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
  print("palindrome")
else:
  print("not palindrome")
  """

# Q => wap to count the number of students with the "A" grade in the following tuple

#grade = ["C", "D", "A", "A", "B", "B", "A"]
#print(grade.count("A"))

# Q => store the above values in a list & sort them "A" to "D"


grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)

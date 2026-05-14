 # Dictionary
"""info = {
  "key" : "value",
  "name" : "apnacollege",
  "learning" : "coding",
  "age" : 35,
  "is_adult" : True,
  "marks" : 94.4

}
print(info)
print(type(info))
"""
# nested dictionary
"""
student = {
  "name" : "rahul kumar",
  "subject" : {
    "physics" : 97,
    "chemistry" : 98,
    "mathe" : 95
  }
}
print(student)
print(student['subject']["chemistry"])
print(student.keys())
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
pairs =  list(student.items())
print(pairs[0])

#print(student["name2"]) #error
print(student.get("name2")) # no error -> None

#print("BEFORE")
#print(student["name2"]) #error
#print("AFTER")

new_dict = {"city" : "delhi", "age": 16}
student.update(new_dict)

print(student)
"""
# Sets

#collection = {1, 2, 2,  2, 3, 4, "hello", "world"} 
#
#print(collection)
#print(type(collection))
#print(len(collection))

#collection = set()
#collection.add(1)
#collection.add(2)
#collection.add(2)
#collection.add("apnacollege")
#collection.add((1, 2, 3))
##collection.add([1, 2, 3]) #error
##collection.remove(1)
#collection.clear()
#print(len(collection))

#collection = {"hello", "apnacollege", "world", "coding",#"python"}
#
#print(collection.pop())
#print(collection.pop())
#print(collection)

#set1 = {1, 2, 3}
#set2 = {2, 3, 4}
#
#print(set1.union(set2)) 
#print(set1.intersection(set2))

# Q => store following word meanings in python dictionary
       # table : "a piece of furniture", list of facts & figure"
       # cat : "a small animal"
"""
dictionary = {
  "cat" : "a small animal",
  "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dictionary)
"""

# Q you are given a list of subjects for students. Assume one classrooom is required for 1 subject. How many classroom are needed by all students.
# "python", "java", "c++","python","javascript",
# "java","python", "java","C++","c"

#subjects = {
#"python", "java", "c++","python","javascript",
#"java","python", "java","c++","c"
#}
#print(subjects)
#print(len(subjects))

# Q => wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. Use subject name as key & marks as value.


"""
marks = {} 

x = int(input("Eneter physics : "))
marks.update({"physics" : x})


x = int(input("Eneter maths : "))
marks.update({"maths" : x})


x = int(input("Eneter chemistry : "))
marks.update({"chemistry" : x})

print(marks)
"""

# Q => Figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built-in data types)

values = {
  ("float", 9.0),
  ("int",9)
}

print(values)
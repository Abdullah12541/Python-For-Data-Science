#4. Tuple Methods:
#4.1 Count() and index:
#Count() returns the number of times a vlue appears 
#index() return the position of a vlaue in the first occurrance

mixed = (10, 20, 20, 10, 30, 30, "Pyhton", "C++", "Python")
print(mixed.count(20))
print(mixed.count(100))
print(mixed.index(10))
print(mixed.index(10, 1 , 4))

#5. Tuple Packing and Unpacking:

data = "Abdullah", 20 , "Data Science" , 4
print(data)
name, age, program , semester = data
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Program:{program}")
print(f"Semester:{semester}")
print(type(name))
print(type(age))

languages = ("Python", "C++", "Java", "SQL", "R", "JavaScript")

a, *b, c = languages
print(a)
print(b)
print(c)
a, b, *c = languages
print(a,b,c)
*a, b, c = languages
print(a,b,c)
# *a or *b or *c = Starred variable

#6. Nested Tuples:

students = (
    ("Ali", 20, "Data Science"),
    ("Sara", 21, "Computer Science"),
    ("Ahmed", 19, "AI")
)  
print(students[1][0][1][2])
name2 , age2 , dep2 = students[1]
print(name2)
print(age2)
name3, age3, dep3 = students[2]
print(dep3)
name1, age1, dep1 = students[0]
print(dep1)
print(age3)


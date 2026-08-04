#1. Creating Tuples:

numbers = (10,20,30)
names = ("Ali", "Sara", "Ahmad")
mixed_t = (10, 2.2, 'A', "Salman")
single_t = (5,)
empty_t = ()
students = "Ali", "Ahmad", "Khan"
print(numbers)
print(names)
print(mixed_t)
print(single_t)
print(empty_t)
print(students)

#2. Accessing Tuple Elements using indexes and using Slicing:

std = ("Ali", "Sara", "Ahmed", "Fatima", "Usman")
print(std[0])
print(std[2])
print(std[-1])
print(std[-2])
print(std[0:3])
print(std[-4:-1])
print(std[::-1])
print(std[1:3])

#3. Tuples Oerations:
#3.1 Concatenantion(+):

boys = ("Ali", "Ahmad")
girls = ("Sara", "Fatima")
stud = boys + girls
print(boys)
print(girls)
print(boys + girls)
print(stud)
print(boys)

#3.2 Repetition(*):

numbers = (10,20,30)
r_tuple = numbers * 3
print(r_tuple)
print(numbers)

#3.3 Membership Operators(in, not in):

data = ("Salma", "Python", "C++", 2.3, 9.99, 2, 4, "SQL")
result = "Salman" in data
print(result)
result1 = "Python" not in data
print(result1)

if 2.3 in data :
    print("Exists.")
else :
    print("Not Exist.")
if 9.99 not in data :
    print("Not Exist.")
else :
    print("Exists.")

#3.4 Comparison operators(==, <, > , <= , >= , !=):
#Key Rule to Remember:.
#When comparing tuples, Python compares elements from left to right.
#Compare the first elements.
#If they're equal, compare the second.
#Keep going until a difference is found.
#The first different pair determines the result.
#This is called lexicographical comparison.

t1 = (10,20,30,40,50)
t2 = (10,20,30,50,40)
print(t1 == t2)
print(t1 < t2)
print(t1 > t2)
print(t1 <= t2)
print(t1 >= t2)
print(t1 != t2) 
# If the first characters are the same, Python compares the next characters. 
# The first position where the characters differ determines which string is larger. 
# The character that comes later alphabetically makes that string larger.
str_t1 = ("Ahmad", "Khan", "Bilal")
str_t2 = ("Kaleem", "Salman", "Hakeem")
print(str_t1 > str_t2)

b_t1 = (False, True)
b_t2 = (True, False)
print(b_t1 > b_t2)
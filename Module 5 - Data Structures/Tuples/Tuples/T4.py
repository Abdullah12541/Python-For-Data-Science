#Solving problems :
#1.Find middle element without hardcoding index:
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[-1])
print(numbers[len(numbers) // 2 ])

#2. print the tuple in reverse order without [::-1] use a loop :
data = (10, 20, 30, 40, 50, 60)
for i in range(len(data)-1,-1,-1) :
    print(data[i])

#3. Find maximum and minimum number in a tuple without using max() and min():

marks = (85, 72, 91, 68, 95, 77)
maximum = marks[0]
minimum = marks[0]
for i in marks :
    if i > maximum :
        maximum = i
    if i < minimum :
        minimum =  i
print(maximum)
print(minimum)
#4.Create a new tuple that contains only even numbers:

numbers = (10, 15, 20, 25, 30, 35, 40)
even = ()
for i in numbers :
    if i % 2 == 0 :
         even = even + (i,)
print(even)
            # OR
even_list = []
for i in numbers :
    if i % 2 == 0 :
        even_list.append(i)
even = tuple(even_list)
print(even)

#5. Print only those who scored greater than 90:
students = (
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 78),
    ("Fatima", 95),
    ("Usman", 88)
)
for name, mark in students :
    if mark > 90 :
        print(F"{name} : {mark}")

        
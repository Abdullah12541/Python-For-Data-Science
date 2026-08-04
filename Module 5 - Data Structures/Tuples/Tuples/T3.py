#7. Built in Functions:
# len(), max(), min(), sum(), sorted(), tuple() :

numbers = (15, 10, 25, 30, 40)
l = len(numbers)
ma = max(numbers)
mi = min(numbers)
su = sum(numbers)
so = sorted(numbers)
print(l)
print(ma)
print(mi)
print(su)
print(so)
print(numbers)

languages = ("Python", "Java", "C++", "SQL")
largest_string = max(languages)
smallest_string = min(languages)
sorted_t = sorted(languages)
print(largest_string)
print(smallest_string)
print(sorted_t)
print(languages)

li = [10,15,20,25]
new_t = tuple(li)
print(new_t)
print(type(new_t))

word = "Abdullah"
t = tuple(word)
print(t)

#8. Traversing Tuples:

marks = (65, 70, 75, 80, 85, 90, 95, 100)
for mark in marks :
    print(mark)

for mark in marks :
    if mark > 85 :
        print(mark)

for mark in marks :
    if mark % 2 == 0 :
        print(mark)

total = 0
for mark in marks :
    total += mark
average = total / len(marks)
print(total)
print(average)

for i in range(len(marks)) :
    print(f"Index {i}: {marks[i]}")

for i in range(len(marks)) :
    if marks[i] > 85 :
        print(f"Index:{i}")

for i in range(len(marks)) :
    if marks[i] > 85 :
        print(f"Index {i}: {marks[i]}")


      
employees = (
    ("Ali", 50000, "HR"),
    ("Sara", 65000, "IT"),
    ("Ahmed", 70000, "AI"),
    ("Fatima", 55000, "Finance")
)

for employee in employees :
    print(employee)
for employee in employees :    
    print(employee[0])
    print(employee[2])
    
#for employee in employees :
    #print(employee[2])

for name, salary, dep in employees :
    print(name, salary, dep)

#for name, salary, dep in employees :  
    #print(salary)

#for name, salary, dep in employees :
    #print(dep)

for name, salary, dep in employees :
    if salary > 55000 :
        print(name)



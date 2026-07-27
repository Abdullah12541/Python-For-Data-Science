#List Operations:

#1.Concatenation:

odd_numbers = [1,3,5,7,9,11]
even_numbers = [2,4,6,8,10,12]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#2.Repetition:
stars = ["*"]
result = stars * 5
print(result)

list1 = [10,20]
list2 = [30,40]
joined_list = list1 + list2
final_list = joined_list * 3
print(final_list)

        #List Methods:

#1.Index(value):

fruits = ["Apple", "Mango", "Peach", "Orange", "Banana"]
result = fruits.index("Mango")
print(result)

n = [5, 10, 15, 10, 20]
print(n.index(10))

lang = ["java", "C++", "C", "Python"]
if "Python" in lang:
    print(lang.index("Python"))
else:
    print("Python is not in the list.")

roll_numbers = [101, 102, 103, 104, 105, 106]
if 104 in roll_numbers:
    print(f"Roll Number 104 is found at index {roll_numbers.index(104)}.")
else:
    print("104 is not in the list")

slicing = [10,20,10,30,20,40]
print(slicing.index(20,2,5))

#2.Count():

nm = [5, 10, 15, 10, 20, 10]
re = nm.count(10)
print(re)

fr = ["Apple", "Banana", "Apple", "Orange", "Apple", "Grapes"]
occurrence = fr.count("Apple")
print(occurrence)

lan = ["Python", "C++", "Python", "Java"]
res = lan.count("Python")
print(f"Python appears {res} times in this list.")

grades = ["A", "B", "A", "C", "B", "A", "D", "B", "A"]
print(f"Number of A grade Students are: {grades.count('A')}")
print(f"Number of B grade Students are: {grades.count('B')}")
print(f"Number of C grade Students are: {grades.count('C')}")
print(f"Number of D grade Students are: {grades.count('D')}")

#3.Sort():

marks = [65, 90, 72, 55, 88, 40, 95, 78, 60, 82]
print(marks)
marks.sort()
print(marks)
marks.sort(reverse = True)
print(marks)

fr = ["Apple", "Orange", "Apple", "Banana", "Apple", "Grapes"]
fr.sort()
print(fr)

#4.reverse():

marks = [65, 90, 72, 55, 88, 40, 95, 78, 60, 82]
marks.reverse()
print(marks)

fr = ["Apple", "Orange", "Apple", "Banana", "Apple", "Grapes"]
fr.reverse()
print(fr)

#5.copy():

marks = [50,60,70,80]
marks_copy = marks.copy()
marks_copy.append(90)
print(marks)
print(marks_copy)

#Buit_in Functions:
#1.sorted:

prices = [450, 1200, 300, 850, 600]
ascending_prices = sorted(prices)
descending_prices = sorted(prices, reverse=True)
print(prices)
print(ascending_prices)
print(descending_prices)

#2.len(),sum(),min(),max():

prices = [450, 1200, 300, 850, 600]

total_items = len(prices)
total_price = sum(prices)
minimum_price = min(prices)
maximum_price = max(prices)

print(total_items)
print(total_price)
print(minimum_price)
print(maximum_price)
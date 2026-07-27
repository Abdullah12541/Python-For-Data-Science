#Adding elements into a list using append():

numbers = [1,2,3,4]
numbers.append(5)
numbers.append([6,7])
print(numbers)

#Adding elements into a list using inset():

animals = ["Monkey", " lion", "Tiger"]
animals.insert(0, "Deer") 
#animals.insert(4, "Zebra")
#print(animals)
animals.insert(len(animals), "Zebra")
print(animals)

#Adding elements into a list using extend(iterable):

data = ['A', 3.14, "B", True]
data.extend(['C', 3.15, "D", False])
print(data)

languages = ["Java", "C", "Rust"]
languages.insert(0, "Python")
languages.extend(["C++", "C#"])
languages.append("Javascript")
print(languages)

            #Removing Elements
#Removing elements using Remove(value):

data = ['A', 'A', "A", "A", 3.14, 3.14, True, True, False, False]
data.remove('A')
data.remove("A")
data.remove(3.14)
data.remove(True)
data.remove(False)
if 4.15 in data:
    data.remove(4.15)
print(data)

#Removing elements using pop(index):

numbers1 = [1,2,3,4,5]
rem = [numbers1.pop(0), numbers1.pop()]
print(rem)
print(numbers1)

names = ["Abdullah", "Salman", "Hammad", "Ali", "Ahmad"]
names.pop(-1)
names.pop(-2)
print(names)

#Removing elements usin del keyword:

n = [1,2,3,4,5,6]
del n[2]
print(n)

letters = ["A", "B", "C", "D", "E", "F"]
del letters[1:4]
print(letters)

#Removing elements using clear():

list1 = [1,2,3,4,5]
list1.clear()
list1.append(1)
print(list1)


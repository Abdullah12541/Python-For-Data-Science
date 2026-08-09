#1. Creating Sets :

colors = {"Red", "Blue", "Green", "Yellow", "Violet"}
print(colors)

ages = {15, 20, 25, 30, 35}
print(ages)

cities = {"Peshawar", "Karachi", "Lahore", "Peshawar", "Lahore"}
print(cities)

mixed_data = {"Abdullah", 20, 83.2, True}
print(mixed_data)

data_science = {"NumPy", "Pandas", "Matplotlib", "Seaborn", "Scikit Learn"}
print(data_science)

empty_set = set()
print(empty_set)
print(type(empty_set))

dic = {}
print(dic)
print(type(dic))

numbers_list = [10, 20, 30, 20, 40, 30, 50]
new_set = set(numbers_list)
print(new_set)

fruits = ("Apple", "Banana", "Apple", "Orange")
f_set = set(fruits)
print(f_set)

word = "Abdullah"
w_set = set(word)
print(w_set)

#2.Set Methods:
#2.1 Adding Elements:
fruits = {"Apple", "Banana", "Mango", "Orange"}
fruits.add("Grapes")
print(fruits)

integers = {1, 2, 3, 4, 5}
integers.add(6)
print(integers)

languages = {"Python", "C++", "C", "Java"}
languages.add("C++")
print(languages)

f_ruits = {"Apple", "Banana"}
f_ruits.update({"Orange", "Mango", "Grapes"})
print(f_ruits)

i_ntegers = {10, 20, 30}
i_ntegers.update([40, 50, 60])
print(i_ntegers)

l_anguages = {"Python", "Java"}
l_anguages.update(("C++", "JavaScript"))
print(l_anguages)

wo_rd = {"A", "B"}
wo_rd.update("HELLO")
print(wo_rd)

#2.2 Removing Elements:
fruit_s = {"Apple", "Banana", "Apple", "Orange"}
fruit_s.remove("Banana")
print(fruit_s)

int_egers = {10, 20, 30, 40}
int_egers.remove(40)
print(int_egers)

frui_ts = {"Apple", "Banana", "Apple", "Orange"}
frui_ts.discard("Apple")
print(frui_ts)

inte_gers = {10, 20, 30, 40}
inte_gers.discard(100)
print(inte_gers)

lan = {"Python", "Java", "C++"}
lan.discard("JavaScript")
print(lan)

fru = {"Apple", "Banana", "Mango", "Grapes", "Orange"}
removed = fru.pop()
print(removed)
print(fru)

num = {10, 20, 30, 40}
removed1 = num.pop()
removed2 = num.pop()
print(removed1)
print(removed2)
print(num)

# s = set()
# r = s.pop()
# print(r)

f = {"Apple", "Banana", "Mango", "Grapes", "Orange"}
f.clear()
print(f)

n = {1, 2, 3, 4, 5}
n.clear()
print(n)
print(type(n))

#2.3 Copying sets elements:

fr = {"Apple", "Banana", "Mango", "Grapes", "Orange"}
copy_fr = fr.copy()
copy_fr.add("Pear")
print(fr)
print(copy_fr)

numb = {1, 2, 3, 4}
copy_numb = numb.copy()
copy_numb.remove(4)
print(numb)
print(copy_numb)
#3. Set Opeartions:

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

C = A.union(B)
D = A | B
print(f"Union of set A and set B is : {C}")
print(f"Union of set A and set B is : {D}")

E = A.intersection(B)
F = A & B
print(f"Intersection of set A and set B is : {E}")
print(f"Intersection of set A and set B is : {F}")

G = A.difference(B)
H = A - B
I = B.difference(A)
J = B - A
print(f"Difference of set A and set B is : {G}")
print(f"Difference of set A and set B is : {H}")
print(f"Difference of set B and set A is : {I}")
print(f"Difference of set B and set A is : {J}")

K = A.symmetric_difference(B)
L = A ^ B
print(f"Symmetric Difference of set A and set B is : {K}")
print(f"Symmetric Difference of set A and set B is : {L}")

#4. Membership Opeartors:

mixed_data = {"Python", "C++", "C", 3.1, 2, 2.2, True, "Numpy"}
print("Python" in mixed_data)
print("TenserFlow" in mixed_data)
print(True in mixed_data)
print(False in mixed_data)

print("Pandas" not in mixed_data)
print(2.22 not in mixed_data)
print(3.1 not in mixed_data)

#5. Built in Functions:

num = {3, 1, 2, 5, 4}
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sorted(num))

A = {0, False, ""}
print(any(A))
print(all(A))

B = {1, 2, 3}
print(any(B))
print(all(B))

#6. Traversing sets:


mixed_data = {"Python", "C++", "C", 3.1, 2, 2.2, True, "Numpy"}
for m in mixed_data :
    print(m)

numbers = {20, 10, 15, 3.1, 1, 0, 3}
for n in numbers :
    print(n)
a = 10
b = 4
sum2 = a+b
sub = a-b
mult = a*b

print(f"Addition : {sum2}")
print(f"Subtraction : {sub}")
print(f"Multiplication : {mult}")
if b != 0:
    div = a/b
    fdiv = a//b
    rem = a%b
    print(f"Division : {div}")
    print(f"Floor Division : {fdiv}")
    print(f"Remainder : {rem}")
else:
    print(f"Division: Can't be divided by 0.")
    print(f"Floor Divivsion: Can't be divided by 0.")
    print(f"Remainder: Can't be divided by 0.")
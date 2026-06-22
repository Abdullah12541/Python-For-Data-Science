colour = input("Enter the colour of the signal : ") .strip() .lower()

if colour == "red" :
    print(f"Stop.")
elif colour == "green" :
    print(f"Go.")
elif colour == "yellow" :
    print(f"Go Slowly")
else:
    print(f"Light is broken.")


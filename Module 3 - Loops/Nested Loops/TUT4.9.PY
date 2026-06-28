#Pyramid:

for row in range(1,6):
    for spaces in range(5-row):
        print(" ", end="")
    for stars in range(2*row-1):
        print("*", end="")
    print()
    
# Inverted Pyramid:

# for row in range(5,0,-1):
#     for spaces in range(5-row):
#         print(" ", end="")
#     for stars in range(2*row-1):
#         print("*", end="")
#     print()

#Diamond:

# for row in range(1,6):
#     for spaces in range(5-row):
#         print(" ", end="")
#     for stars in range(2*row-1):
#         print("*", end="")
#     print()
# for row in range(4,0,-1):
#     for spaces in range(5-row):
#         print(" ", end="")
#     for stars in range(2*row-1):
#         print("*", end="")
#     print()


#Rectangle:

# for row in range(1,6):
#     for col in range(1,8):
#         print("*", end="")
#     print()


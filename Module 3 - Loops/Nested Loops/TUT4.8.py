# Right_Aligned Triangle:

for row in range(1,6) :
    for spaces in range(5-row) :
        print(" ", end="")
    for stars in range(1,row+1) :
        print("*", end="")
    print()


#Right_Aligned Triangle Inverted:

# for row in range(1,6) :
#     for spaces in range(row-1) :
#         print(" ", end="")
#     for stars in range(6-row) :
#         print("*", end="")
#     print()
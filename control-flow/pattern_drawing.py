length = int(input("Enter the size of the pattern:"))
row = length
while row > 0 :
    for i in range(length): print("*", end="")
    print()
    row -=1

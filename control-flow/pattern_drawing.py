pattern_size = int(input("Enter the size of the pattern: "))

if pattern_size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < pattern_size:
        for col in range(pattern_size):
            print("*", end="")
        print()  
        row += 1


size = int(input(" Enter a number to see its multiplication table"))

if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0

    
    while row < size:
        
        for col in range(size):
            print("*", end="")
        
        print()
        
        row += 1

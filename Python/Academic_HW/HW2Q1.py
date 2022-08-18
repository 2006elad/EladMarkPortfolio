x = int(input("Please enter Digit between 0 - 10 "))

while x<0 or x>10:  # Input validation
    x = int(input("Please try again and enter Digit only between 0 - 10 "))

for i in range(x+1):    # Print the outline
    if i == 0:
        print("\t\t", sep='', end='')
    print("(", i, ")\t", sep='', end='')

print("\n", end='')

for row in range(x+1):  # Print the table
    print("(", row, ")   \t", sep='', end='')
    for column in range(x+1):
        print(row*column, "\t", sep='', end='')
    print("\n", end='')

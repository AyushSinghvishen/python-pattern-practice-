def hollow_square(n):
    square = []

    for i in range(n):
        if i == 0 or i == n - 1:
            # First and last row
            row = "*" * n
        else:
            # Inner rows
            row = "*" + " " * (n - 2) + "*"
        square.append(row)
    
    return square

# Example usage
n = int(input("Enter the size of the hollow square: "))
result = hollow_square(n)
for line in result:
    print(line)

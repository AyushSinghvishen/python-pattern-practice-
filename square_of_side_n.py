def square_pattern(n):
    # Create a list to store each row
    square = []
    for i in range(n):
        row = "*" * n     # Each row has n stars
        square.append(row)
    return square

# Example usage
n = int(input("Enter the size of the square: "))
result = square_pattern(n)
for line in result:
    print(line)


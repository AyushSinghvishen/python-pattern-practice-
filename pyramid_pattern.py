def pyramid_pattern(n):
    pyramid = []

    for i in range(1, n + 1):
        stars = "*" * (2 * i - 1)         # Number of stars in the row
        spaces = " " * (n - i)            # Leading spaces for centering
        row = spaces + stars + spaces
        pyramid.append(row)
    
    return pyramid

# Example usage
n = int(input("Enter the number of rows: "))
result = pyramid_pattern(n)
for line in result:
    print(line)


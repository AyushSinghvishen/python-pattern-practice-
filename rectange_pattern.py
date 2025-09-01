def rectangle_pattern(m, n):
    rectangle = []

    for i in range(m):
        row = "*" * n
        rectangle.append(row)
    
    return rectangle

# Example usage
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
result = rectangle_pattern(m, n)
for line in result:
    print(line)

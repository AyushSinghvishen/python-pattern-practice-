def right_angled_triangle(n):
    triangle = []

    for i in range(1, n + 1):
        row = "*" * i
        triangle.append(row)
    
    return triangle

# Example usage
n = int(input("Enter the number of rows: "))
result = right_angled_triangle(n)
for line in result:
    print(line)


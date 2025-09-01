def inverted_right_angled_triangle(n):
    triangle = []

    for i in range(n, 0, -1):
        row = "*" * i
        triangle.append(row)
    
    return triangle

# Example usage
n = int(input("Enter the number of rows: "))
result = inverted_right_angled_triangle(n)
for line in result:
    print(line)


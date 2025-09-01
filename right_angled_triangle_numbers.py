def right_angled_triangle_numbers(n):
    triangle = []

    for i in range(1, n + 1):
        row = "".join(str(j) for j in range(1, i + 1))
        triangle.append(row)
    
    return triangle

# Example usage
n = int(input("Enter the number of rows: "))
result = right_angled_triangle_numbers(n)
for line in result:
    print(line)

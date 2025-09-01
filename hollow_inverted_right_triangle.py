def hollow_inverted_right_triangle(n):
    triangle = []

    for i in range(n, 0, -1):  # rows from n down to 1
        row = ""
        for j in range(1, i + 1):  # columns
            # Print star at boundaries: first column, last column, or first row
            if j == 1 or j == i or i == n:
                row += "* "
            else:
                row += "  "
        triangle.append(row.rstrip())  # remove trailing spaces

    return triangle


# Example usage
n = int(input("Enter number of rows: "))
result = hollow_inverted_right_triangle(n)
for line in result:
    print(line)

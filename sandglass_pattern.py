def sandglass_pattern(n):
    pattern = []

    # Top half (inverted triangle)
    for i in range(n, 0, -1):
        row = " " * (n - i) + "* " * i
        pattern.append(row.rstrip())  # remove trailing space

    # Bottom half (normal triangle)
    for i in range(2, n + 1):
        row = " " * (n - i) + "* " * i
        pattern.append(row.rstrip())

    return pattern


# Example usage
n = int(input("Enter number of rows: "))
result = sandglass_pattern(n)
for line in result:
    print(line)


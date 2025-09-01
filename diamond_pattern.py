def diamond_pattern(n):
    diamond = []

    # Top half (including middle row)
    for i in range(1, n + 1):
        row = " " * (n - i) + "* " * i
        diamond.append(row.rstrip())  # remove trailing space

    # Bottom half (excluding middle row)
    for i in range(n - 1, 0, -1):
        row = " " * (n - i) + "* " * i
        diamond.append(row.rstrip())

    return diamond


# Example usage
n = int(input("Enter number of rows: "))
result = diamond_pattern(n)
for line in result:
    print(line)

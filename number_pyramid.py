def number_pyramid(n):
    triangle = []  # this list will store each row (as a string)

    for i in range(1, n + 1):   # outer loop: controls the rows
        # 1) Spaces to shift numbers to the center (pyramid shape)
        spaces = " " * (n - i)

        # 2) Build the numbers for the current row
        numbers = ""
        for j in range(1, i + 1):   # inner loop: numbers from 1 to i
            numbers += str(j) + " "

        # 3) Remove extra space at the end of numbers
        row = spaces + numbers.strip()

        # 4) Add this row to the list
        triangle.append(row)

    return triangle


# Example usage
n = int(input("Enter number of rows: "))
result = number_pyramid(n)
for line in result:
    print(line)

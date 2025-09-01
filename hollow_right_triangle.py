def hollow_right_triangle(n):
    for i in range(1, n + 1):  # rows
        for j in range(1, i + 1):  # columns
            # Print star only at the borders: 
            # first column, last column, or last row
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # move to next line


# Example usage
n = int(input("Enter number of rows: "))
hollow_right_triangle(n)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for j in range(len(grid[0])):  # Iterate through columns (from left to right)
    for i in range(len(grid) - 1, -1, -1):  # Iterate through rows in reverse order (bottom to top)
        print(grid[i][j], end=" ")
    print()  # New line after each column


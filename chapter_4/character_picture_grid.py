#!/usr/bin/python3


grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['x', '.', '.', '.', '.', 'x']]


for i in range(len(grid[0])): # vertical line
    for j in range(len(grid) -1, -1, -1): # horizontal line
        print(grid[j][i], end = " ")
    print() # print new line

# první loop -> změří délku vnořeného listu
# druhý loop, začne printovat první položku každého vnořeného listu od konce k začátku a vytvoří mezi sebou mezeru, poté se printne nová lajna

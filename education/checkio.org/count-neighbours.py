#!/usr/bin/python

grid_1 = (((1, 0, 0, 1, 0),
           (0, 1, 0, 0, 0),
           (0, 0, 1, 0, 1),
           (1, 0, 0, 0, 0),
           (0, 0, 1, 0, 0)), 3, 3)

grid_2 = (((1, 0, 0, 1, 0),
           (0, 1, 0, 0, 0),
           (0, 0, 1, 0, 1),
           (1, 0, 0, 0, 0),
           (0, 0, 1, 0, 0),), 2, 2)

grid_3 = (((1, 1, 1),
           (1, 1, 1),
           (1, 1, 1),), 0, 2)


def check_dot(grid, row, col):
    result = ()
    len_row = len(grid[0])
    x1 = col - 1
    x2 = col + 2

    if x1 < 0:
        x1 = 0
    if x2 > len_row:
        x2 = len_row

    if row - 1 >= 0:
        result += grid[row - 1][x1:x2]
    result += grid[row][x1:x2]
    if row + 1 < len(grid):
        result += grid[row + 1][x1:x2]

    print sum(result) - grid[row][col]


def main():
    i = 1
    for grid in grid_1, grid_2, grid_3:
        print i
        check_dot(grid[0], grid[1], grid[2])
        i += 1

main()

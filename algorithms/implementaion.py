import copy
import math
import os
import random
import re
import sys


#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
# https://www.hackerrank.com/challenges/bomber-man/


def bomber_man():
    # Write your code here
    n = 5
    grid = """
    .......
...O...
....O..
.......
OO.....
OO.....
    """
    grid = [item.strip() for item in grid.strip().split('\n')]

    # Solving
    if n < 2:
        return grid
    if n % 2 == 0:
        return ['O' * len(item) for item in grid]

    states = []

    # Exists two states
    for s in range(2):
        temp = ['O' * len(item) for item in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    temp[i] = temp[i][:j] + '.' + temp[i][j + 1:]
                    if i > 0:
                        temp[i - 1] = temp[i - 1][:j] + '.' + temp[i - 1][j + 1:]
                    if i < len(grid) - 1:
                        temp[i + 1] = temp[i + 1][:j] + '.' + temp[i + 1][j + 1:]
                    if j > 0:
                        temp[i] = temp[i][:j - 1] + '.' + temp[i][j:]
                    if j < len(grid[0]) - 1:
                        temp[i] = temp[i][:j + 1] + '.' + temp[i][j + 2:]
        # print(temp)
        grid = temp
        states.append(grid)

    if (n - 2) % 4 == 1:
        return states[0]
    if (n - 2) % 4 == 3:
        return states[1]
    return None


if __name__ == "__main__":
    print(bomber_man())

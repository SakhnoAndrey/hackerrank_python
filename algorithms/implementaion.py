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


#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray():
    # Write your code here
    a = [1, 6, 5, 2, 4, 3]

    invertions = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                invertions += 1

    # If the number of inversions is odd, the array cannot be sorted
    # If the number of inversions is even, the array can be sorted

    return 'NO' if invertions % 2 == 1 else 'YES'


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted():
    # Write your code here
    arr = "1 5 4 3 2 6"
    arr = "3 1 2"
    arr = list(map(int, arr.split(' ')))

    sorted_arr = sorted(arr)
    sort_type = None

    unsorted_id = [i for i, (x, y) in enumerate(zip(arr, sorted_arr)) if x != y]

    # Check swap two elements
    if len(unsorted_id) == 2:
        sort_type = 'swap'

    # Check reverse one sub-segment
    if sort_type is None and all([arr[i] > arr[i + 1] for i in unsorted_id[:-1]]):
        sort_type = 'reverse'

    result = f"yes\n{sort_type} {unsorted_id[0] + 1} {unsorted_id[-1] + 1}" if sort_type else 'no'
    print(result)
    return


if __name__ == "__main__":
    print(almostSorted())

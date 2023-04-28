import math
from itertools import combinations


def twoPluses():
    # Write your code here
    # https://www.hackerrank.com/challenges/two-pluses

    s = """
        6 6
    BGBBGB
    GGGGGG
    BGBBGB
    GGGGGG
    BGBBGB
    BGBBGB
        """
    s = s.strip()
    n, *grid = [item.strip() for item in s.split('\n')]
    n, m = n.split()

    possible_plusses = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 'B':
                max_plus_length = min(i, j, len(grid) - i - 1, len(grid[0]) - j - 1) + 1
                plus = set()
                plus.add((i, j))
                possible_plusses.append(plus)
                for k in range(1, max_plus_length):
                    if grid[i - k][j] == 'G' and \
                            grid[i + k][j] == 'G' and \
                            grid[i][j - k] == 'G' and \
                            grid[i][j + k] == 'G':
                        plus.add((i - k, j))
                        plus.add((i + k, j))
                        plus.add((i, j - k))
                        plus.add((i, j + k))
                    else:
                        break
                    sub_plus = plus.copy()
                    possible_plusses.append(sub_plus)

    max_area_product = 0
    for pi in possible_plusses:
        for pj in possible_plusses:
            if not pi.intersection(pj):
                max_area_product = max(max_area_product, len(pi) * len(pj))

    return max_area_product

def alternate():
    # Write your code here
    # https://www.hackerrank.com/challenges/two-characters/

    s = 'beabeefeab'

    symbols = set(s)
    temp = [symbols - set(item) for item in combinations(symbols, 2)]
    two_symbol_str = [s.translate({ord(c): None for c in item}) for item in temp]
    result = 0
    for item in two_symbol_str:
        if item[0] != item[1] and (item[:2] * math.ceil(len(item)/2))[:len(item)] == item and result < len(item):
            result = len(item)
    return result


if __name__ == '__main__':
    alternate()

import math
from email.charset import add_charset
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


def bigSorting():
    # Write your code here
    unsorted = ['1', '200', '150', '3']

    result = sorted(unsorted, key=lambda x: (len(x), x), reverse=False)
    return result
def superReducedString(s):
    result = ''
    while True:
        skip_idx = -1
        for i, char in enumerate(s):
            if skip_idx == i:
                skip_idx = -1
                continue
            if (i + 2 <= len(s)) and char == s[i+1]:
                skip_idx = i + 1
                continue
            result += char
        if result == s:
            break
        s, result = result, ''
    if result == '':
        result = 'Empty String'
    return result

def camelcase(s):
    return 1 + sum([1 for letter in s if str(letter).isupper()])


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    min_len = 6
    is_lower = False
    is_numbers = False
    is_upper = False
    is_special = False
    for letter in password:
        is_lower |= letter in lower_case
        is_upper |= letter in upper_case
        is_special |= letter in special_characters
        is_numbers |= letter in numbers
    add_char = sum(map(lambda x: not x, [is_upper, is_lower, is_special, is_numbers]))
    return min_len - n if n + add_char < min_len else add_char


def caesarCipher(s, k):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for c in s:
        is_upper = c.isupper()
        c = c.lower()
        pos = alphabet.find(c)
        if pos >= 0:
            pos += k % len(alphabet)
            pos = pos - len(alphabet) if pos >= len(alphabet) - 1 else pos
            c = alphabet[pos].upper() if is_upper else alphabet[pos]
        result += c
    return result


def marsExploration(s):
    # Write your code here
    right_signal = "SOS" * 33
    return sum([1 for i, j in zip(s, right_signal) if i != j])



if __name__ == '__main__':
    print(marsExploration("SOSSOSSOS"))

import math
from copy import copy
from email.charset import add_charset
from itertools import combinations

from typing import List

from helpers import str_to_list_of_int


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


def hackerrankInString(s):
    # Write your code here
    word = "hackerrank"
    pos = 0
    for letter in s:
        if letter == word[pos]:
            pos += 1
        if pos == len(word):
            return "YES"
    return "NO"

def quickSort(arr):
    # Write your code here
    left, equal, right = [], [arr[0]], []
    for item in arr[1:]:
        if item < arr[0]:
            left.append(item)
        elif item == arr[0]:
            equal.append(item)
        else:
            right.append(item)
    return left + equal + right


def pangrams(s):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.replace(" ", "").lower()
    return "pangram" if len(set(s)) == len(alphabet) else "not pangram"


def weightedUniformStrings(s, queries):
    # Write your code here
    arr = dict()
    mult = 1
    char_prev = ''
    for i, char in enumerate(s):
        if i != 0 and char == char_prev:
            mult += 1
            print(mult)
            arr[(ord(char) - 96) * mult] = True
        else:
            arr[(ord(char) - 96)] = True
            mult = 1
            char_prev = char
    return ["Yes" if item in arr else "No" for item in queries]


def separateNumbers(s):
    # Write your code here
    if len(s) == 1 or (len(s) == 2 and int(s[0]) != int(s[1]) + 1) and s[0] == '0':
        return print("NO")
    test_number = int(s[0])
    for i in range(1, (len(s) // 2) + 1):
        test_string = str(test_number)
        j = 1
        while len(s) > len(test_string):
            test_string += str(test_number + j)
            j += 1
            # print(test_string)
        if test_string == s:
            return print(f"YES {test_number}")
        if len(str(test_number)) < len(s):
            test_number = int(s[:i+1])
    return print("NO")


def funnyString(s):
    # Write your code here
    arr = [ord(letter) for letter in s]
    diff_arr = [abs(item - arr[i+1]) for i, item in enumerate(arr[:-1])]
    return "Funny" if all([i == j for i, j in zip(diff_arr, diff_arr[::-1])]) else "Not Funny"


def countingSort(arr):
    # Write your code here
    values = {i: 0 for i in range(100)}
    for i in arr:
        values[i] += 1
    return list(values.values())


def countingSort2(arr):
    # Write your code here
    values = {i: 0 for i in range(100)}
    for i in arr:
        values[i] += 1
    result = []
    for k, v in values.items():
        if v == 0:
            continue
        result.extend([k] * v)
    return result


def gemstones(arr: list):
    # Write your code here
    d = {k: 0 for k in range(1, 27)}
    data = [copy(d) for _ in range(len(arr))]
    for i, item in enumerate(arr):
        for ch in set(item):
            data[i][ord(ch) - 96] = 1
    return sum([all(elem) for elem in zip(*[list(item.values()) for item in data])])


def alternatingCharacters(s):
    # Write your code here
    switch = 0
    prev_letter = s[0]
    for ch in s[1:]:
        if ch != prev_letter:
            switch += 1
            prev_letter = ch
    return len(s) - 1 - switch

def countSort(arr):
    # Write your code here
    d = {}
    n = len(arr)
    for _ in range(n):
        i, v = arr[_]
        i = int(i)
        d.setdefault(i, [])
        d[i].append("-" if _ < n / 2 else v)
    d = sorted(d.items())
    for i in d:
        for j in i[1]:
            print(j, end=" ")


def beautifulBinaryString(b: str):
    # Write your code here
    b = [int(ch) for ch in b]
    n = len(b)
    count = 0
    for i in range(2, n):
        if b[i] == 0 and b[i - 1] == 1 and b[i - 2] == 0:
            b[i] = 1
            count += 1
    return count


def closestNumbers(arr):
    if not isinstance(arr, list):
        arr = str_to_list_of_int(arr)
    arr = sorted(arr)
    output = []
    it = iter(arr)
    item = next(it)
    next_item = next(it)
    diff_min = 10 ** 7
    while next_item:
        if diff_min > abs(next_item - item):
            diff_min = abs(next_item - item)
            output = [item, next_item]
        elif diff_min == abs(next_item - item):
            output += [item, next_item]
        item = next_item
        try:
            next_item = next(it)
        except StopIteration:
            break
    return output


def theLoveLetterMystery(s):
    # Write your code here
    arr = [ord(ch) for ch in s]
    len_arr = len(arr) // 2
    return sum([abs(x - y) for x, y in zip(arr[:len_arr], arr[-len_arr:][::-1])])


def findMedian(arr):
    # Write your code here
    return sorted(arr)[len(arr) // 2]


def dna_input():
    s = """
    a b c aa d b
    1 2 3 4 5 6
    3
    1 5 caaab
    0 4 xyz
    2 4 bcdybc
    """
    res = []
    s = s.strip('\n').split('\n')
    res.append(s[0].strip().split(' '))
    res.append(list(map(int, s[1].strip().split(' '))))
    for i in range(int(s[2].strip())):
        res.append(list(map(lambda x: int(x) if str(x).isnumeric() else x, s[i+3].strip().split(' '))))
    return res


def determiningDNAhealthV1(genes: list = None, health: list = None, s: int = 0,
                         first: int = 0, last: int = 0, d: str = None):

    strands = []
    if d is not None:
        strands = [[first, last, d]]

    if any(x is None for x in [genes, health]):
        arr = dna_input()
        genes = arr[0]
        health = arr[1]
        strands = arr[2:]

    import re

    min_res, max_res = 10**7, 0

    for first, last, d in strands:
        res_iter = 0
        for g, h in zip(genes[first:last+1], health[first:last+1]):
            matches = [m.group(1) for m in re.finditer(f'(?=({g}))', d)]
            res_iter += len(matches) * h
        min_res = min(res_iter, min_res)
        max_res = max(res_iter, max_res)
    print(f'{min_res} {max_res}')


from collections import deque, defaultdict
import bisect

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.outputs = []

def build_aho_corasick(unique_genes):
    root = Node()
    for gene in unique_genes:
        node = root
        for ch in gene:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.outputs.append(gene)

    # построение ссылок "fail"
    queue = deque()
    for node in root.children.values():
        node.fail = root
        queue.append(node)

    while queue:
        current = queue.popleft()
        for ch, child in current.children.items():
            queue.append(child)
            fail_node = current.fail
            while fail_node and ch not in fail_node.children:
                fail_node = fail_node.fail
            child.fail = fail_node.children[ch] if fail_node and ch in fail_node.children else root
            child.outputs += child.fail.outputs

    return root

def search_dna(dna, root, first, last, gene_map):
    node = root
    total = 0
    for ch in dna:
        while node and ch not in node.children:
            node = node.fail
        node = node.children[ch] if node and ch in node.children else root

        for gene in node.outputs:  # теперь output — gene name
            indices = gene_map[gene]
            left = bisect.bisect_left(indices, (first, -float('inf')))
            right = bisect.bisect_right(indices, (last, float('inf')))
            total += sum(h for i, h in indices[left:right])
    return total




def determiningDNAhealthV2(genes: list = None, health: list = None, s: int = 0, first: int = 0, last: int = 0, d: str = None):
    strands = []
    if d is not None:
        strands = [[first, last, d]]

    if any(x is None for x in [genes, health]):
        arr = dna_input()
        genes = arr[0]
        health = arr[1]
        strands = arr[2:]

    gene_map = defaultdict(list)  # gene -> list of (index, health)

    for i, g in enumerate(genes):
        gene_map[g].append((i, health[i]))

    root = build_aho_corasick(list(gene_map.keys()))
    min_score = 10**18
    max_score = -10**18

    for first, last, d in strands:
        score = search_dna(d, root, first, last, gene_map)
        min_score = min(min_score, score)
        max_score = max(max_score, score)

    print(f"{min_score} {max_score}")


from math import inf
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict



def getHealth(subs, gMap, seq, first, last, largest):
    h, ls = 0, len(seq)

    for f in range(ls):
        for j in range(1, largest+1):
            if f+j > ls:
                break
            sub = seq[f:f+j]
            if sub not in subs:
                break
            if sub not in gMap:
                continue
            ids, hs = gMap[sub]
            h += hs[bRight(ids, last)]-hs[bLeft(ids, first)]
    return h


def determiningDNAhealthV4(genes: list = None, health: list = None, s: int = 0, first: int = 0, last: int = 0, d: str = None):
    strands = []
    if d is not None:
        strands = [[first, last, d]]

    if any(x is None for x in [genes, health]):
        arr = dna_input()
        genes = arr[0]
        health = arr[1]
        strands = arr[2:]


    gMap = defaultdict(lambda: [[], [0]])
    subs = set()
    for i, gene in enumerate(genes):
        gMap[gene][0].append(i)
        for j in range(1, min(len(gene), 500)+1):
            subs.add(gene[:j])

    for v in gMap.values():
        for i, ix in enumerate(v[0]):
            v[1].append(v[1][i]+health[ix])

    largest = max(list(map(len, genes)))
    hMin, hMax = inf, 0

    for first, last, d in strands:
        h = getHealth(subs, gMap, d, first, last, largest)
        hMin, hMax = min(hMin, h), max(hMax, h)

    print(f"{hMin} {hMax}")




if __name__ == '__main__':
    result = determiningDNAhealthV4()
    print(result)

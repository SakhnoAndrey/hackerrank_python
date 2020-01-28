import re


def romanian_numerals():
    # Input
    numerals = input()

    # Function
    thousand = '(M{0,3})'
    hundred = '(CM|CD|D?C{0,3})'
    ten = '(XC|XL|L?X{0,3})'
    digit = '(IX|IV|V?I{0,3})'
    regex_pattern = r"^{0}{1}{2}{3}$".format(thousand, hundred, ten, digit)
    result = re.match(regex_pattern, numerals)
    print(str(bool(result)))


def floating_point_number():
    # Input
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())

    # Function
    for el in arr:
        regex_pattern = r"^[+-]?\d*[\.]{1}\d+$"
        result = re.match(regex_pattern, el)
        print(str(bool(result)))


def re_split():
    # Input
    number = input()

    # Function
    regex_pattern = r"[\.,]"
    print("\n".join(re.split(regex_pattern, number)))


def group_groups_groupdict():
    # Input
    s = input()

    # Function
    regex_pattern = r"([a-zA-Z0-9])\1+"
    m = re.search(regex_pattern, s)
    print(m.group(0)[0] if m else -1)


if __name__ == '__main__':
    group_groups_groupdict()

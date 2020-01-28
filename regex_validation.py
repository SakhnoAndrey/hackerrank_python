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


if __name__ == '__main__':
    floating_point_number()

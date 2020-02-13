from fractions import Fraction
from functools import reduce


def map_lambda():
    n = int(input().strip())
    cube = lambda x: x ** 3
    fibonacci = [0, 1]
    if n < 3:
        fibonacci = fibonacci[:n]
    else:
        for i in range(2, n):
            fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    print(list(map(cube, fibonacci)))


def fun(s):
    try:
        username, s = s.split("@", 1)
        websitename, extension = s.split(".", 1)
        if any([username == "", websitename == "", extension == ""]):
            return False
    except ValueError:
        return False
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    elif not websitename.isalnum():
        return False
    elif len(extension) > 3 or not extension.isalnum():
        return False
    else:
        return True


def filter_mail(emails):
    # Input
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = list(filter(fun, emails))
    filtered_emails.sort()
    print(filtered_emails)


def product():
    # Input
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*(map(int, input().split()))))
    # Function
    result = reduce(lambda x, y: x * y, fracs)
    print(result)


product()

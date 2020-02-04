import math
import os
import random
import sys


def hello_world():
    print("Hello, World!")


def if_else(n):
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n < 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


def arithmetic_operators(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


def division(a, b):
    print(a // b)
    print(a / b)


def loops():
    n = int(input())
    l = [i ** 2 for i in range(n)]
    for k in l:
        print(k)


def is_leap():
    year = int(input())
    leap = False
    # Write your logic here
    if 1900 <= year <= 10 ** 5:
        if year % 4 == 0:
            leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:
            leap = True
    else:
        leap = False
    #
    print(leap)
    return leap


def print_function():
    n = int(input())
    for i in range(1, n + 1):
        print(i, sep="", end="")


if __name__ == "__main__":
    print_function()

import os
import sys


def introduction():
    # Input
    n = int(input())
    array = list(map(int, input().rstrip().split()))
    # Function
    array = set(array)
    return sum(array) / len(array)


def symmetric_difference():
    # Input
    m = int(input())
    arr_m = set(map(int, input().rstrip().split()))
    n = int(input())
    arr_n = set(map(int, input().rstrip().split()))
    # Function
    difference_mn = list(arr_m.union(arr_n).difference(arr_m.intersection(arr_n)))
    difference_mn.sort()
    s = "\n".join(map(str, difference_mn))
    print(s)


def set_add():
    # Input
    n = int(input())
    stamps = []
    for _ in range(n):
        stamps.append(input())
    # Function
    size = len(set(stamps))
    print(size)


def discard_remove_pop():
    # Input
    n = int(input())
    s = set(map(int, input().strip().split()))
    c = int(input())
    # Function
    for _ in range(c):
        command, *args = input().rstrip().split()
        command += "({0})".format(','.join(args))
        eval("s." + command)
    print(sum(s))


def set_union():
    # Input
    ne = int(input())
    e = set(map(int, input().split()))
    nf = int(input())
    f = set(map(int, input().split()))
    # Function
    print(len(e | f))


def set_intersection():
    # Input
    ne = int(input())
    e = set(map(int, input().split()))
    nf = int(input())
    f = set(map(int, input().split()))
    # Function
    print(len(e & f))


def set_difference():
    # Input
    ne = int(input())
    e = set(map(int, input().split()))
    nf = int(input())
    f = set(map(int, input().split()))
    # Function
    print(len(e - f))


def set_symmetric_difference():
    # Input
    ne = int(input())
    e = set(map(int, input().split()))
    nf = int(input())
    f = set(map(int, input().split()))
    # Function
    print(len(e ^ f))


def set_mutations():
    # Input
    na = int(input())
    a = set(map(int, input().rstrip().split()))
    n = int(input())
    for _ in range(n):
        command, args = input().rstrip().split()
        command += "(n)"
        n = set(map(int, input().rstrip().split()))
        eval("a." + command)
    print(sum(a))

def captain_room():
    # Input
    k, arr = int(input()), list(map(int, input().split()))
    myset = set(arr)
    print(((sum(myset) * k) - (sum(arr))) // (k - 1))

def check_subset():
    # Input
    t = int(input())
    for _ in range(t):
        na = int(input())
        a = set(map(int, input().strip().split()))
        nb = int(input())
        b = set(map(int, input().strip().split()))
        # Function
        print(a <= b)

def check_strict_superset():
    # Input
    a = set(map(int, input().strip().split()))
    n = int(input())
    superset = True
    for _ in range(n):
        b = set(map(int, input().strip().split()))
        superset &= a > b
    print(superset)

def no_idea():
    # Input
    n, m = list(map(int, input().strip().split()))
    happy_set = list(map(int, input().strip().split()))
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))
    # Function
    count = sum([(x in a) - (x in b) for x in happy_set])
    print(count)


no_idea()

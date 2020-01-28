import os
import sys


def swap_case():
    # Input
    s = input()
    # Function
    s = s.swapcase()
    print(s)


def split_and_join():
    # Input
    line = input()
    # Function
    return "-".join(line.split(" "))


def whats_your_name():
    # Input
    a = input()
    b = input()
    # Function
    s = "Hello {0} {1}! You just delved into python.".format(a, b)
    print(s)


def mutations():
    # Input
    string = input()
    line = list(map(str, input().rstrip().split()))
    position = int(line[0])
    character = line[1]
    # Function
    string = string[:position] + character + string[position + 1:]
    return string


def find_string():
    # Input
    string = input().strip()
    sub_string = input().strip()
    # Function
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


def string_validators():
    # Input
    s = input()
    # Function
    # uses all 5 methods on each character and creates a list for each,
    # containing the results of each method used on the character.
    new_list = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]

    # rotates lists clockwise to get lists of each method instead
    rotated = list(zip(*new_list))

    # prints whether or not a True is present for each List
    print("\n".join([str(any(i)) for i in rotated]))


if __name__ == '__main__':
    string_validators()

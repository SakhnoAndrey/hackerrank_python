import os
import sys
import textwrap
import string


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
    string = string[:position] + character + string[position + 1 :]
    return string


def find_string():
    # Input
    string = input().strip()
    sub_string = input().strip()
    # Function
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    return count


def string_validators():
    # Input
    s = input()
    # Function
    # uses all 5 methods on each character and creates a list for each,
    # containing the results of each method used on the character.
    new_list = [
        [c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s
    ]

    # rotates lists clockwise to get lists of each method instead
    rotated = list(zip(*new_list))

    # prints whether or not a True is present for each List
    print("\n".join([str(any(i)) for i in rotated]))


def text_alignments():
    # Replace all ______ with rjust, ljust or center.

    thickness = int(input())  # This must be an odd number
    c = "H"

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
    for i in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

        # Bottom Cone
    for i in range(thickness):
        print(
            (
                (c * (thickness - i - 1)).rjust(thickness)
                + c
                + (c * (thickness - i - 1)).ljust(thickness)
            ).rjust(thickness * 6)
        )


def text_wrap():
    # Input
    string = input()
    max_width = int(input())
    # Function
    result = textwrap.fill(string, max_width)
    return result


def designer_door_mat():
    # Input
    n, m = map(int, input().rstrip().split())
    pattern = [(".|." * (1 + 2 * i)).center(m, "-") for i in range(n // 2)]
    print("\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1]))


def string_formatting():
    # Input
    n = int(input())
    # Function
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print(
            "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)
        )


def alphabet_rangoli():
    # Input
    n = int(input())
    # Function
    length = n * 4 - 3
    alphabet = string.ascii_lowercase
    arr = []
    for i in range(n):
        s = "-".join(alphabet[i:n])
        s = s[:0:-1] + s
        arr.append(s.center(length, "-"))
    arr = arr[:0:-1] + arr
    result = "\n".join(arr)
    print(result)


def capitalize():
    # Input
    s = input()
    # Function
    s = " ".join([word.capitalize() for word in s.split(" ")])
    return s


def minion_game():
    # Input
    s = input()
    # Function
    l = len(s)
    consonants_word = 0
    vowels_word = 0
    vowels_set = set("aeiou".upper())
    for i in range(l):
        if s[i] in vowels_set:
            vowels_word += l - i

        else:
            consonants_word += l - i
    if vowels_word > consonants_word:
        print("Kevin {0}".format(vowels_word))
    elif vowels_word < consonants_word:
        print("Stuart {0}".format(consonants_word))
    else:
        print("Draw")


def merge_tools():
    # Input
    s = input()
    k = int(input())
    # Function
    n = len(s)
    arr = []
    for i in range(0, n, k):
        substring = s[i : i + k]
        word = ""
        for char in substring:
            if char not in word:
                word += char
        arr.append(word)
    s = "\n".join(arr)
    print(s)


if __name__ == "__main__":
    merge_tools()

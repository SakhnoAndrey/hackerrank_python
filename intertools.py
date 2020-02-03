from itertools import product, permutations, combinations, combinations_with_replacement, groupby


def itertools_product():
    # Input
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    # Function
    print(*(product(a, b)))


def itertools_permutations():
    # Input
    s, n = input().rstrip().split()
    # Functions
    r = permutations(sorted(s), int(n))
    for elem in r:
        print("".join(elem))


def itertools_combinations():
    # Input
    s, n = input().strip().split()
    s = sorted(s)
    n = int(n)
    # Function
    for i in range(1, n + 1):
        print(*list(map("".join, combinations(s, i))), sep="\n")


def itertools_combinations_with_replacement():
    # Input
    s, n = input().strip().split()
    s = sorted(s)
    k = int(n)
    # Function
    print(*list(map("".join, combinations_with_replacement(s, k))), sep="\n")


def compress_the_string():
    # Input
    s = input().strip()
    # Function
    for i, g in groupby(s):
        print((len(list(g)), int(i)), end=" ")


def iterables_and_iterators():
    # Input
    n = int(input())
    arr = list(input().strip().split())
    k = int(input())
    # Function
    arr = list(combinations(arr, k))
    count = len([elem for elem in arr if 'a' in elem])
    probability = count / len(arr)
    print("{:.4f}".format(probability))


def maximize_it():
    # Input
    k, m = list(map(int, input().strip().split()))
    n = (list(map(int, input().split()))[1:] for _ in range(k))
    # Function
    results = [sum(el ** 2 for el in t) % m for t in list(product(*n))]
    print(max(results))


maximize_it()

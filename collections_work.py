from collections import Counter, defaultdict, namedtuple, OrderedDict, deque


def counter_lab():
    # Input
    n = int(input().strip())
    shoes = Counter(list(map(int, input().strip().split())))
    n = int(input().strip())
    money = 0
    for _ in range(n):
        size, price = map(int, input().strip().split())
        if shoes[size] != 0:
            money += price
            shoes[size] -= 1
    print(money)


def default_dict_tutorial():
    n, m = map(int, input().strip().split())
    d = defaultdict(list)
    for i in range(n):
        d[input()].append(i + 1)
    list_b = [input().strip() for _ in range(m)]
    for elem in list_b:
        print(" ".join(map(str, d[elem]))) if elem in d else print("-1")


def collections_namedtuple():
    # Input
    n = int(input().strip())
    col = ",".join(map(str, input().upper().strip().split()))
    Student = namedtuple("Student", col)
    # * - преобразует список в элементы namedtuple
    result = sum([int(Student(*input().strip().split()).MARKS) for _ in range(n)]) / n
    print("{:.2f}".format(result))


def ordered_dict():
    # Input
    n = int(input().strip())
    boughted_items = OrderedDict()
    for _ in range(n):
        name, space, price = input().rpartition(" ")
        boughted_items[name] = boughted_items.get(name, 0) + int(price)
    for item, price in boughted_items.items():
        print(item, price)


def word_order():
    # Input
    n = int(input().strip())
    word_dict = OrderedDict()
    for _ in range(n):
        name = input().strip()
        word_dict[name] = word_dict.get(name, 0) + 1
    print(len(word_dict))
    print(*word_dict.values())


def collections_deque():
    # Input
    n = int(input())
    arr_command = deque()
    for _ in range(n):
        command, *args = input().rstrip().split()
        command += "({0})".format(",".join(args))
        eval("arr_command." + command)
    print(*arr_command)


def company_logo():
    # Input
    # s = input().strip()
    # od = Counter(sorted(s)).most_common(3)
    # [print(*elem) for elem in od]
    [print(*elem) for elem in Counter(sorted(input().strip())).most_common(3)]


def piling_up():
    # Input
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        cubes = deque(list(map(int, input().strip().split())))
        pile = "Yes"
        for cube in reversed(sorted(cubes)):
            if cubes[0] == cube:
                cubes.popleft()
            elif cubes[-1] == cube:
                cubes.pop()
            else:
                pile = "No"
                break
        print(pile)





piling_up()

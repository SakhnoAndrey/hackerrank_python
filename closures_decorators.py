# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f(
            [
                "+91 "
                + elem[len(elem) - 10 : len(elem) - 5]
                + " "
                + elem[len(elem) - 5 :]
                for elem in l
            ]
        )

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


def input_list_phone():
    # Input
    l = [input() for _ in range(int(input()))]
    print(l)
    sort_phone(l)


# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


def input_person_list():
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")


input_person_list()

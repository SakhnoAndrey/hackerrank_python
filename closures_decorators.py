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


input_list_phone()

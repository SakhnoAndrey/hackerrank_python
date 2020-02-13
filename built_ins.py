def zipped():
    n, x = map(int, input().strip().split())
    exam = []
    exam += [map(float, input().strip().split()) for _ in range(x)]
    average_student = [sum(stud) / x for stud in zip(*exam)]
    print("\n".join(map(str, average_student)))


def func_input():
    x, k = map(int, input().strip().split())
    print(eval(input().replace("x", str(x))) == k)


def evaluation():
    eval(input())


def athlete_sort():
    n, m = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    k = int(input().strip())
    # NEED TO DONE IT
    [print(" ".join(map(str, row))) for row in sorted(arr, key=lambda r: r[k])]


def any_or_all():
    n, arr = int(input().strip()), list(map(int, input().strip().split()))
    print(
        any([str(el) == str(el)[::-1] for el in arr])
        if all([el >= 0 for el in arr])
        else False
    )


def ginortS():
    print(
        *(
            sorted(
                input(),
                key=lambda x: (
                    x.isdigit(),
                    x.isdigit() and int(x) % 2 == 0,
                    x.isupper(),
                    x.islower(),
                    x,
                ),
            )
        ),
        sep=""
    )


ginortS()

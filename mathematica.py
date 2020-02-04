import math, cmath


def polar_coordinates():
    z = complex(input())
    f = cmath.phase(z)
    r = abs(z)
    print("{0}\n{1}".format(r, f))


def find_angle_MBC():
    # Input
    ab = int(input().strip())
    bc = int(input().strip())
    # Function
    # Медиана к гипотенузе равна половине этой гипотенузы BM = MC
    # ba / 2 * tgO = bc /2
    # tgO = ab/bc
    # O = arctg(ab/bc)
    t = round(math.degrees(math.atan(ab / bc)))
    print("{0}°".format(t))


def triangle_quest_2():
    # Input
    # Function var 1
    for i in range(
        1, int(input()) + 1
    ):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(
            sum(
                ((j + 1) * (10 ** j) + (j + 1) * (10 ** (2 * i - j - 2)) * (j + 1 != i))
                for j in range(i)
            )
        )
    # Function var 2
    for i in range(
        1, int(input()) + 1
    ):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print((10 ** i // 9) ** 2)


def mod_dovmod():
    # Input
    a = int(input())
    b = int(input())
    # Function
    print(a // b)
    print(a % b)
    print(divmod(a, b))


def power_mod_power():
    # Input
    a = int(input())
    b = int(input())
    m = int(input())
    # Function
    print(pow(a, b))
    print(pow(a, b, m))


def integer_come_in_all_size():
    # Input
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    # Function
    print(a ** b + c ** d)


def triangle_quest():
    # Input
    # Function
    for i in range(
        1, int(input())
    ):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(i * 10 ** i // 9)


triangle_quest()

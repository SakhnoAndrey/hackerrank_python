import cmath


def polar_coordinates():
    z = complex(input())
    f = cmath.phase(z)
    r = abs(z)
    print("{0}\n{1}".format(r, f))


polar_coordinates()

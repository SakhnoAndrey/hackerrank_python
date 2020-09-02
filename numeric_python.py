import numpy


def enter_array(n):
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    return numpy.array(arr)


# Arrays
def arrays():
    # Input
    arr = input().rstrip().split(" ")

    # Function
    return numpy.array(arr[::-1], float)


# Shape and Reshape
def shape_reshape():
    # Input
    arr = list(map(int, input().rstrip().split()))

    # Function
    np_arr = numpy.array(arr)
    print(numpy.reshape(np_arr, (3, 3)))


# Transpose and Flatten
def transpose_flatten():
    # Input
    n, m = map(int, input().rstrip().split())

    # Function
    np_arr = enter_array(n)
    print(np_arr.transpose())
    print(np_arr.flatten())


# Concatenate
def concatenate_arrays():
    # Input
    n, m, p = map(int, input().rstrip().split())
    array_1 = []
    array_2 = []
    for i in range(n):
        array_1.append(list(map(int, input().rstrip().split())))
    for i in range(m):
        array_2.append(list(map(int, input().rstrip().split())))

    # Function
    np_arr_1 = enter_array(n)
    np_arr_2 = enter_array(m)
    print(numpy.concatenate((array_1, array_2), axis=0))


# Zeros and ones
def zeros_and_ones():
    # Input
    t = tuple(map(int, input().rstrip().split()))

    # Function
    print(numpy.zeros(t, dtype=numpy.int))
    print(numpy.ones(t, dtype=numpy.int))


# Eye and Identity
def eye_and_identity():
    # Input
    n, m = map(int, input().strip().split())

    # Function
    numpy.set_printoptions(sign=" ")
    print(numpy.eye(n, m, k=0))


# Arrays mathematics
def arrays_mathematics():
    # Input
    n, m = map(int, input().strip().split())

    # Function
    np_array_1 = enter_array(n)
    np_array_2 = enter_array(n)
    print(np_array_1 + np_array_2)
    print(np_array_1 - np_array_2)
    print(np_array_1 * np_array_2)
    print(np_array_1 // np_array_2)
    print(np_array_1 % np_array_2)
    print(np_array_1 ** np_array_2)


# Floor, Ceil and Rint
def floor_ceil_rint():
    # Input
    arr = numpy.array(list(map(float, input().strip().split())))

    # Function
    numpy.set_printoptions(sign=" ")
    print(numpy.floor(arr))
    print(numpy.ceil(arr))
    print(numpy.rint(arr))


# Sum and Prod
def sum_prod():
    # Input
    n, m = map(int, input().strip().split())
    arr = enter_array(n)

    # Function
    print(numpy.product(numpy.sum(arr, axis=0)))


sum_prod()

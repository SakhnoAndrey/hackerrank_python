import numpy


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


shape_reshape()

# Task 1

def task1():
    dict_old = {1: "value1", 2: "value2"}
    dict_new =dict()
    for key, value in dict_old.items():
        dict_new[value] = key
    print(dict_new)


def task2():
    a = [1, 2, 3]
    b = ['q', 'w', 'e']
    d = dict()
    for key, value in zip(a, b):
        d[key] = value
    print(d)


def task3():
    arr_old = [[1, 2, 3], [4, 5, 6]]
    arr_new = []
    for item in arr_old:
        arr_new.extend(item)
    print(arr_new)


def task4():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    c = list(set([item for item in a if item in b]))

    print(c)


def task6(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def task8():
    d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    value_sort_max = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(dict(value_sort_max))


if __name__ == "__main__":
    task8()

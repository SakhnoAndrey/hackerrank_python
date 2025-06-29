# Task 1
import os


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


def activityNotifications_input():
    def activityNotifications(expenditure: list, d: int):

        def get_median_value(count_array, d):
            counter = 0
            median_expenditure = []
            for j, _ in enumerate(count_array):
                if count_array[j] == 0:
                    continue

                counter += count_array[j]

                if counter >= d // 2 + d % 2 and not median_expenditure:
                    median_expenditure.append(j)

                    if counter >= d // 2 + d % 2 + 1 and quantity_expenditure == 2:
                        median_expenditure.append(j)
                        break
                    continue

                if median_expenditure and quantity_expenditure == 2:
                    median_expenditure.append(j)

            return sum(median_expenditure)/quantity_expenditure

        # Write your code here
        count = 0
        count_array = [0] * 201
        quantity_expenditure = 2 if d % 2 == 0 else 1

        for i in range(d):
            count_array[expenditure[i]] += 1

        for i in range(d, len(expenditure)):
            if expenditure[i] >= get_median_value(count_array, d) * 2:
                count += 1

            count_array[expenditure[i - d]] -= 1
            count_array[expenditure[i]] += 1
        return count

    # Write your code here
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    n = 9

    # d = int(first_multiple_input[1])
    d = 5

    # expenditure = list(map(int, input().rstrip().split()))
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

    result = activityNotifications(expenditure, d)

    print(result)


if __name__ == "__main__":
    activityNotifications_input()

from helpers import str_to_list_of_int


def introTutorial(V, arr):
    # Write your code here
    results = [i for i, item in enumerate(arr) if item == V]
    if results:
        return results[0]


def insertionSort1v1(n, arr):
    start_idx = 0
    finish_idx = len(arr) - 2
    found_idx = -1
    sorted_arr, last_item = arr[:-1], arr[-1]

    if sorted_arr[-1] < last_item:
        return arr

    while found_idx == -1:
        mid_idx = (finish_idx - start_idx) // 2
        if mid_idx == 0 and finish_idx - start_idx == 1:
            if sorted_arr[start_idx] < last_item:
                return sorted_arr[:start_idx + 1] + [last_item] + sorted_arr[start_idx + 1:]
            elif sorted_arr[finish_idx] > last_item:
                return sorted_arr[:finish_idx] + [last_item] + sorted_arr[finish_idx:]
            else:
                return sorted_arr[:start_idx + 1] + [last_item] + sorted_arr[start_idx + 1:]
        if sorted_arr[mid_idx] > last_item:
            finish_idx = mid_idx
        elif sorted_arr[mid_idx] < last_item:
            start_idx = mid_idx
        else:
            return sorted_arr[:mid_idx] + [last_item] + sorted_arr[mid_idx:]

def insertionSort1v2(n, arr):
    last_item_idx = len(arr) - 1
    while True:
        if arr[last_item_idx] < arr[last_item_idx - 1]:
            arr[last_item_idx], arr[last_item_idx - 1] = arr[last_item_idx - 1], arr[last_item_idx]
            last_item_idx -= 1
            print(' '.join(map(str, arr)))
            continue
        return

def insertionSort2(n, arr):
    i = 0
    for i in range(1, n):
        for j, item in enumerate(arr[:i]):
            if item  > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(' '.join(map(str, arr)))


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

def runningTime(l):
    total = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           total += 1
        l[j+1] = key
    return total



if __name__ == '__main__':
    insertion_sort(str_to_list_of_int('2 4 6 8 3'))
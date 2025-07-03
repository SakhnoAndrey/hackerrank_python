from helpers import str_to_list_of_int


def insertionSort1(n, arr):
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


if __name__ == '__main__':
    res = insertionSort1(5, str_to_list_of_int('2 4 6 8 3'))
    print(res)
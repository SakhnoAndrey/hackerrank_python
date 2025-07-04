from typing import List, Any


def str_to_list_of_int(s: str) -> list:
    return list(map(int, s.strip().split(' ')))

def two_dimensional_array_int_str(s) -> list[list[int | Any]]:
    return [
        [int(v) if i == 0 else v for i, v in enumerate(item.split(' '))]
        for item in s.strip("\n").strip().split('\n')
    ]
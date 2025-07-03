def str_to_list_of_int(s: str) -> list:
    return list(map(int, s.strip().split(' ')))
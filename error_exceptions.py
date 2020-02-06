import re

def exceptions_func():
    for _ in range(int(input().strip())):
        try:
            a, b = map(int, input().strip().split())
            print(a // b)
        except Exception as e:
            print("Error Code:", e)


def incorrect_regex():
    for _ in range(int(input())):
        s = input()
        ans = True
        try:
            re.compile(s)
        except re.error:
            ans = False
        print(ans)



incorrect_regex()

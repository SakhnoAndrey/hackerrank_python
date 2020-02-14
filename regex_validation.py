import re
import email.utils
from html.parser import HTMLParser


def floating_point_number():
    # Input
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())

    # Function
    for el in arr:
        regex_pattern = r"^[+-]?\d*[\.]{1}\d+$"
        result = re.match(regex_pattern, el)
        print(str(bool(result)))


def re_split():
    # Input
    number = input()

    # Function
    regex_pattern = r"[\.,]"
    print("\n".join(re.split(regex_pattern, number)))


def group_groups_groupdict():
    # Input
    s = input()

    # Function
    regex_pattern = r"([a-zA-Z0-9])\1+"
    m = re.search(regex_pattern, s)
    print(m.group(0)[0] if m else -1)


def findall_finditer():
    s = input()
    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"
    result = re.findall(
        r"(?<=[%s])([%s]{2,})(?=[%s])" % (consonants, vowels, consonants), s, flags=re.I
    )
    print("\n".join(result)) if result != [] else print(-1)


def start_end():
    s = input()
    k = input()
    pattern = re.compile(k, re.I)
    m = pattern.search(s)
    if not m:
        print("(-1, -1)")
    while m:
        print("({0}, {1})".format(m.start(), m.end() - 1))
        m = pattern.search(s, m.start() + 1)


def regex_sub():
    arr = []
    for _ in range(int(input())):
        arr.append(
            re.sub(
                r"(?<= )(&&|\|\|)(?= )",
                lambda x: "and" if x.group() == "&&" else "or",
                input(),
            )
        )
    print("\n".join(arr))


def romanian_numerals():
    # Input
    numerals = input()

    # Function
    thousand = "(M{0,3})"
    hundred = "(CM|CD|D?C{0,3})"
    ten = "(XC|XL|L?X{0,3})"
    digit = "(IX|IV|V?I{0,3})"
    regex_pattern = r"^{0}{1}{2}{3}$".format(thousand, hundred, ten, digit)
    result = re.match(regex_pattern, numerals)
    print(str(bool(result)))


def phone_numbers():
    arr = []
    for _ in range(int(input())):
        print("YES") if re.match(r"[789]\d{9}$", input()) else print("NO")


def email_address():
    n = int(input())
    arr = []
    for _ in range(n):
        addr = email.utils.parseaddr(input())
        m = re.match(r"[A-Za-z](\w|-|_|\.)+@[A-Za-z]+\.[A-Za-z]{1,3}$", addr[1])
        if m:
            arr.append((addr[0], m.group(0)))
    for elem in arr:
        print(email.utils.formataddr(elem))


def hex_color_code():
    arr = []
    for _ in range(int(input())):
        f = re.findall(r"[\s:](#[0-9a-f]{6}|#[0-9a-f]{3})", input(), re.I)
        arr += f
    print("\n".join(arr))


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.handler("Start", tag, attrs)

    def handle_endtag(self, tag):
        self.handler("End", tag)

    def handle_startendtag(self, tag, attrs):
        self.handler("Empty", tag, attrs)

    def handler(self, type_tag, tag, attrs=[]):
        print("{0:6}: {1}".format(type_tag, tag))
        if len(attrs) > 0:
            for a in attrs:
                print("-> {0} > {1}".format(a[0], a[1]))


def html_parser_1():
    arr = []
    for _ in range(int(input())):
        arr.append(input())
    parser = MyHTMLParser()
    parser.feed("\n".join(arr))


if __name__ == "__main__":
    html_parser_1()

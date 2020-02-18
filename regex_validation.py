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


class MyHTMLParser1(HTMLParser):
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


class MyHTMLParser2(HTMLParser):
    def handle_comment(self, data):
        type_comment = (
            "Single-line" if len(data.split("\n")) == 1 else "Multi-line"
        ) + " Comment"
        self.handler(type_comment, data)

    def handle_data(self, data):
        self.handler("Data", data)

    def handler(self, type_tag, data):
        if data.strip():
            print(">>> {0}".format(type_tag))
            print(data)


class MyDetectHTMLTagAttr(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.handler(tag, attrs)

    def handler(self, tag, attrs=[]):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> {0} > {1}".format(attr[0], attr[1]))


def html_parser_1():
    arr = []
    for _ in range(int(input())):
        arr.append(input())
    parser = MyHTMLParser1()
    parser.feed("\n".join(arr))
    parser.close()


def html_parser_2():
    html = ""
    for _ in range(int(input())):
        html += input().rstrip() + "\n"
    parser = MyHTMLParser2()
    parser.feed(html)
    parser.close()


def detect_html_tag():
    html = ""
    for _ in range(int(input())):
        html += input().rstrip() + "\n"
    parser = MyDetectHTMLTagAttr()
    parser.feed(html)
    parser.close()


def validating_uid():
    for _ in range(int(input())):
        s = input()
        print(
            "Valid"
            if all(
                [
                    re.search(r, s)
                    for r in [r"[A-Za-z0-9]{10}", r"([A-Z].*){2}", r"([0-9].*){3}"]
                ]
            )
            and not re.search(r".*(.).*\1", s)
            else "Invalid"
        )


def validating_credit_card():
    for _ in range(int(input())):
        s = input()
        if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(
            r"([\d])\1\1\1", s.replace("-", "")
        ):
            print("Valid")
        else:
            print("Invalid")


def validating_postal_codes():
    p = input()
    regex_integer_in_range = r"_________"  # Do not delete 'r'.
    regex_alternating_repetitive_digit_pair = r"_________"  # Do not delete 'r'.
    print(
        bool(re.match(regex_integer_in_range, p))
        and len(re.findall(regex_alternating_repetitive_digit_pair, p)) < 2
    )


if __name__ == "__main__":
    validating_credit_card()

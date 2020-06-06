import sys
import xml.etree.ElementTree as etree


def get_attr_number():
    # Input
    data = ""
    for _ in range(int(input())):
        data += input().strip()
    tree = etree.ElementTree(etree.fromstring(data))
    node = tree.getroot()

    # Function
    return sum(len(item.attrib) for item in node.iter())


print(get_attr_number())

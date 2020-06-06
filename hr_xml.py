import sys
import xml.etree.ElementTree as etree


# XML 1 - Find the Score
def get_attr_number():
    # Input
    data = ""
    for _ in range(int(input())):
        data += input().strip()
    tree = etree.ElementTree(etree.fromstring(data))
    node = tree.getroot()

    # Function
    return sum(len(item.attrib) for item in node.iter())


# XML2 - Find the Maximum Depth
maxdepth = 0


def input_xml():
    # Input
    global maxdepth
    n = int(input())
    data = ""
    for _ in range(n):
        data += input() + "\n"
    tree = etree.ElementTree(etree.fromstring(data))
    depth(tree.getroot(), -1)
    print(maxdepth)


def depth(elem, level):
    global maxdepth
    level += 1
    if maxdepth < level:
        maxdepth = level
    for item in elem:
        depth(item, level)


input_xml()

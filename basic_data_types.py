def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(
        [
            [i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if i + j + k != n
        ]
    )


def runner_up():
    # Values
    n = 2
    s = "2 3 6 6 5"
    arr = list(map(int, s.rstrip().split()))

    # Function
    print(arr)
    m = max(arr)
    runnerup = -100
    for elem in arr:
        if runnerup < elem < m:
            runnerup = elem
    print(runnerup)


def nested_lists():
    # Input
    students_list = []
    """for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name, score])"""
    students_list = [
        ["Harry", 37.21],
        ["Berry", 37.21],
        ["Tina", 37.2],
        ["Akriti", 41],
        ["Harsh", 39],
    ]
    print(students_list)

    # Function
    min_grade = students_list[0][1]
    max_grade = students_list[0][1]
    for stud in students_list:
        if stud[1] < min_grade:
            min_grade = stud[1]
        if stud[1] > max_grade:
            max_grade = stud[1]
    second_grade = max_grade
    for stud in students_list:
        if min_grade < stud[1] < second_grade:
            second_grade = stud[1]
    list_second_grade = []
    for stud in students_list:
        if stud[1] == second_grade:
            list_second_grade.append(stud[0])
    list_second_grade.sort()
    for item in list_second_grade:
        print(item)


def finding_percentage():
    # Input
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Function
    marks = student_marks[query_name]
    print("{0:.2f}".format(sum(marks) / len(marks)))


def list_commands():
    # Input
    n = int(input())

    # Function
    data = []
    for i in range(n):
        s = input()
        command, *args = s.rstrip().split()
        if command != "print":
            command += "(" + ",".join(args) + ")"
            eval("data." + command)
        else:
            print(data)


def func_tuple():
    # Input
    n = input()
    integer_list = map(int, input().strip().split())

    # Function
    t = tuple(integer_list)
    print(hash(t))


if __name__ == "__main__":
    func_tuple()

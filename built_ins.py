def zipped():
    n, x = map(int, input().strip().split())
    exam = []
    exam += [map(float, input().strip().split()) for _ in range(x)]
    average_student = [sum(stud) / x for stud in zip(*exam)]
    print("\n".join(map(str, average_student)))


zipped()

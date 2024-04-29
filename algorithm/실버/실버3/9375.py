import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    dict = {}

    for _ in range(n):
        item, case = sys.stdin.readline().rstrip().split()
        if case in dict:
            dict[case] += 1
        else:
            dict[case] = 1
    count = 1
    for num in dict.values():
        count *= num + 1
    print(count - 1)
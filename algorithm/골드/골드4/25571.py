T = int(input())

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))

    count = 0
    start = 0
    length = 1
    for i in range(1, N):
        if length == 1 and l[i] != l[start]:
            length += 1
        elif length == 1 and l[i] == l[start]:
            start = i
        elif l[i-2] < l[i-1] > l[i] or l[i-2] > l[i-1] < l[i]:
            length += 1
        else:
            count += (length - 1) * length // 2

            if l[i] != l[i-1]:
                start = i-1
                length = 2

            else:
                start = i
                length = 1

    count += (length - 1) * length // 2

    print(count)
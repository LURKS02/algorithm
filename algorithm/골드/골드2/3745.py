import bisect

while True:
    try:
        N = int(input())
        l = list(map(int, input().split()))

        lis = []
        for num in l:
            pos = bisect.bisect_left(lis, num)
            if len(lis) == 0 or (len(lis) > 0 and num > lis[-1]):
                lis.append(num)
            else:
                lis[pos] = num

        print(len(lis))

    except EOFError:
        break
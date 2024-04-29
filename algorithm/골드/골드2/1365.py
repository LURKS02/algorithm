from bisect import bisect_left

N = int(input())
lines = list(map(int, input().split()))

lis = []
for line in lines:
    pos = bisect_left(lis, line)

    if pos == len(lis):
        lis.append(line)
    else:
        lis[pos] = line

print(N - len(lis))

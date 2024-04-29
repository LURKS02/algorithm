N = int(input())
l = list(map(int, input().split()))

total = sum(l)

M = int(input())

if total <= M:
    print(max(l))
else:
    top = M
    bottom = 0

    while(bottom <= top):
        mid = (top + bottom) // 2
        if sum([min(k, mid) for k in l]) > M:
            top = mid - 1
        else:
            bottom = mid + 1

    print(top)
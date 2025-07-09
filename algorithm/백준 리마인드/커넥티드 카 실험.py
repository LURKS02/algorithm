N, S = map(int, input().split())
x = list(map(int, input().split()))
h = list(map(int, input().split()))

low, high = S-1, S-1
l, r = x[S-1] - h[S-1], x[S-1] + h[S-1]
min_, max_ = float('inf'), -float('inf')

while True:
    for i in range(low-1, -1, -1):
        if x[i] >= l:
            min_ = min(min_, x[i] - h[i])
            max_ = max(max_, x[i] + h[i])
            low = i
        else:
            break

    for i in range(high+1, N):
        if x[i] <= r:
            min_ = min(min_, x[i] - h[i])
            max_ = max(max_, x[i] + h[i])
            high = i
        else:
            break

    if l == min_ and r == max_:
        break

    l = min_
    r = max_

for i in range(low, high+1):
    print(i+1, end=" ")
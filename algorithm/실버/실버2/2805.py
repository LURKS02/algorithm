N, M = map(int, input().split())
l = list(map(int, input().split()))

bottom = 0
top = 1000000000

while(bottom < top):
    mid = (bottom + top) // 2
    count = 0
    for num in l:
        if num - mid > 0:
            count += num - mid
    if count >= M:
        bottom = mid + 1
    else:
        top = mid

mid = (bottom + top) // 2
count = 0

for num in l:
    if num - mid > 0:
        count += num - mid
if count >= M:
    print(mid)
else:
    print(mid - 1)
N = int(input())
l = list(map(int, input().split()))

left = 0
right = N-1

res = 0

while left + 1 < right:
    res = max(res, (right-left-1) * min(l[left], l[right]))
    if l[left] < l[right]:
        left += 1
    else:
        right -= 1

print(res)
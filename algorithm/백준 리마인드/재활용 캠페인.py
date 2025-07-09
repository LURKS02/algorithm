N, X = map(int, input().split())
C = list(map(int, input().split()))

C.sort()

ans = 0
end = len(C)-1

for i in range(len(C)-1, -1, -1):
    if C[i] == X:
        ans += 1
        end = i-1

start = 0

remainCount = 0

while start < end:
    if C[start] + C[end] >= X / 2:
        start += 1
        end -= 1
        ans += 1
    else:
        remainCount += 1
        start += 1

if start == end:
    remainCount += 1

print(ans + remainCount // 3)

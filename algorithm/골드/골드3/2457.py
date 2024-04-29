import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())

def makeCount(m, d):
    s = 0
    for i in range(1, m):
        if i == 4 or i == 6 or i == 9 or i == 11:
            s += 30
        elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            s += 31
        else:
            s += 28

    s += d
    return s

flowers = []

for _ in range(N):
    a, b, c, d = map(int, input().rstrip().split())
    flowers.append((makeCount(a, b), makeCount(c, d) - 1))

ans = 0
now = 31 + 28 + 1
end = 31 * 6 + 30 * 4 + 28
# print(end)

maxheap = []
flowers.sort(key=lambda x: (x[0], -x[1]))
# print(flowers)

i = 0
next = now
while now <= end:
    found = False
    while i < len(flowers) and flowers[i][0] <= now:
        next = max(next, flowers[i][1])
        found = True
        i += 1
    if not found:
        break
    ans += 1
    now = next + 1

if now <= end:
    print(0)
else:
    print(ans)

import sys

input = sys.stdin.readline

N = int(input().rstrip())

l = []

for _ in range(N):
    A, B = map(int, input().rstrip().split())
    l.append((A, B))

l.sort(key=lambda x: (x[1], x[0]))

last = l[-1][1]
end = 0

count = 1

while(True):
    m = end
    for k in range(end + 1, N):
        if l[end][1] <= l[k][0]:
            end = k
            count += 1
            break
    if end == m:
        break

print(count)
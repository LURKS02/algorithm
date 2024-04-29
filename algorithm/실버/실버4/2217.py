import sys

N = int(sys.stdin.readline().rstrip())

l = []

for _ in range(N):
    inputnum = int(sys.stdin.readline().rstrip())
    l.append(inputnum)

l.sort(reverse=True)

max = 0
for i in range(N):
    weight = (i + 1) * l[i]
    if max < weight:
        max = weight
print(max)

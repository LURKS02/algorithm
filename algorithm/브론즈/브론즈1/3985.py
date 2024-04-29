L = int(input())
N = int(input())

l = []

for i in range(N):
    a, b = map(int, input().split())
    l.append((a - 1,b - 1))

cake = [0] * L

max = 0
maxindex = -1
for i in range(len(l)):
    if l[i][1] - l[i][0] > max:
        max = l[i][1] - l[i][0]
        maxindex = i

dmax = 0
dmaxindex = -1

for i in range(len(l)):
    cakes = 0
    for j in range(l[i][0], l[i][1] + 1):
        if cake[j] == 0:
            cake[j] = 1
            cakes += 1

    if cakes > dmax:
        dmax = cakes
        dmaxindex = i

print(maxindex + 1)
print(dmaxindex + 1)

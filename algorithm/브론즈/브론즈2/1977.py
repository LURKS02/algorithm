import math

M = int(input())
N = int(input())

l = []
for i in range(math.ceil(math.sqrt(M)), math.floor(math.sqrt(N)) + 1):
    l.append(i)

if len(l) == 0:
    print(-1)
else:
    count = 0
    for le in l:
        count += pow(le, 2)
    print(count)
    print(pow(l[0], 2))
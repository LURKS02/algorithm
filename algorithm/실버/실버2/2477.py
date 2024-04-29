from collections import deque

K = int(input())

l = deque()
counter = {}

for _ in range(6):
    d, length = map(int, input().split())
    l.append((d, length))
    if d in counter:
        counter[d].append(length)
    else:
        counter[d] = [length]

ones = []
bigsquare = 1
for key in counter.keys():
    if len(counter[key]) == 1:
        bigsquare *= counter[key][0]
        ones.append(key)

#print(ones)

#print(l)
while l[0][0] not in ones:
    l.rotate(1)

#print(l)
smallsquare = 1
if l[0][0] in ones and l[1][0] in ones:
    smallsquare *= l[3][1]
    smallsquare *= l[4][1]
else:
    smallsquare *= l[2][1]
    smallsquare *= l[3][1]

print((bigsquare - smallsquare) * K)
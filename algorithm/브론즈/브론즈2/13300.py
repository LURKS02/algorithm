from collections import Counter

N, K = map(int, input().split())

ml = []
fml = []

for i in range(N):
    s, g = map(int, input().split())
    if s == 0:
        fml.append(g)
    else:
        ml.append(g)

cml = Counter(ml)
cfml = Counter(fml)

def rooms(num):
    if num % K == 0:
        return num // K
    else:
        return num // K + 1

mc = sum(rooms(n) for n in cml.values())
fmc = sum(rooms(n) for n in cfml.values())

print(mc + fmc)
from collections import Counter

N = int(input())

l = []
for i in range(N):
    l.append(input())

l = [c[0] for c in l]
l = Counter(l)
filtered = [item for item in l if l[item] >= 5]
filtered.sort()

if len(filtered) == 0:
    print("PREDAJA")
else :
    for c in filtered:
        print(c, end= '')
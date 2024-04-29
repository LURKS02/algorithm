from collections import Counter

l = []
for i in range(10):
    n = int(input())
    l.append(n)

print(sum(l) // 10)

l = Counter(l)
print(l.most_common(1)[0][0])
from collections import Counter

l = []

for i in range(5):
    l.append(int(input()))

counts = Counter(l)

remain = [item for item, count in counts.items() if count % 2 != 0]
print(remain[0])
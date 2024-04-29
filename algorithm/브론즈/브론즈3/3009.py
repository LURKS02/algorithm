from collections import Counter

A = []
B = []

for i in range(3):
    a, b = (map(int, input().split()))
    A.append(a)
    B.append(b)

countA = Counter(A)
countB = Counter(B)
myA = [item for item, count in countA.items() if count == 1]
myB = [item for item, count in countB.items() if count == 1]

print(myA[0], myB[0], end = ' ')
N, M = map(int, input().split())

setA = set()
for _ in range(N):
    setA.add(input())

setB = set()
for _ in range(M):
    setB.add(input())

newSet = setA & setB
newlist = sorted(newSet)

print(len(newSet))
for num in newlist:
    print(num)
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
presents = []

for _ in range(N):
    P, V = map(int, input().split())
    presents.append((P, V))

presents.sort()

idx = []
maxValue = presents[0][1]
s = maxValue
left = 0

for i in range(1, N):
    s += presents[i][1]
    while presents[i][0] - presents[left][0] >= D:
        s -= presents[left][1]
        left += 1
    maxValue = max(maxValue, s)

print(maxValue)
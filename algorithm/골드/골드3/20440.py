import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input().rstrip())
mosquito = defaultdict(int)

for _ in range(N):
    E, X = map(int, input().rstrip().split())
    mosquito[E] += 1
    mosquito[X] -= 1

acc = [0]
maxValue = 0
start, end = 0, 0
flag = False

# print(mosquito)

keyList = sorted(mosquito.keys())
# print(keyList)
for i in range(len(keyList)):
    acc.append(acc[i]+mosquito[keyList[i]])
    if maxValue < acc[i+1]:
        maxValue = acc[i+1]
        start = keyList[i]
        flag = True
    if flag and acc[i+1] < maxValue:
        end = keyList[i]
        flag = False

print(maxValue)
print(start, end)
from collections import defaultdict

N, M = map(int, input().split())

dict = defaultdict(int)

for _ in range(N):
    line = input()
    dict[line] += 1

K = int(input())

answer = 0
for key in dict.keys():
    numberOfZero = 0
    l = list(map(int, list(key)))
    for num in l:
        if num == 0:
            numberOfZero += 1

    if numberOfZero <= K and (K - numberOfZero) % 2 == 0:
        answer = max(answer, dict[key])

print(answer)
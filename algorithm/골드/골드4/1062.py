from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0
res = set(chr(i) for i in range(97, 123)) - {'a','n','t','i','c'}
data = []

for _ in range(N):
    word = str(input().rstrip('\n'))
    data.append(word[4:-4])

def solve(data, learned):
    cnt = 0
    for word in data:
        canRead = True
        for w in word:
            if learned[ord(w)] == 0:
                canRead = False
                break
        if canRead:
            cnt += 1
    return cnt

if K >= 5:
    learned = [0] * 123
    for x in {'a', 'n', 't', 'i', 'c'}:
        learned[ord(x)] = 1

    for teach in list(combinations(res, K-5)):
        for t in teach:
            learned[ord(t)] = 1
        cnt = solve(data, learned)
        if cnt > answer:
            answer = cnt
        for t in teach:
            learned[ord(t)] = 0
    print(answer)
else:
    print(0)
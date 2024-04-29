N = int(input())

l = []

for _ in range(N):
    new = list(map(int, input().split()))
    l.append(new)

minScore = int(1e9)

start = set()

def getScore(s):

    setList = list(s)

    score = 0
    for i in setList:
        for j in setList:
            score += l[i][j]
    return score

def backtracking(index):
    global minScore

    if index > N:
        return

    if len(start) == N // 2:
        value = abs(getScore(start) - getScore(set(k for k in range(N) if k not in start)))
        # print(start)
        # print(getScore(start))
        # print(getScore(set(k for k in range(N) if k not in start)))
        if value < minScore:
            minScore = value
        return

    start.add(index)

    backtracking(index + 1)

    start.remove(index)

    backtracking(index + 1)

backtracking(0)

print(minScore)
N = int(input())

S = []
W = []

for _ in range(N):
    s, w = map(int, input().split())
    S.append(s)
    W.append(w)

maxBrokenEggs = 0
def backtracking(currentIndex, breakPoint):
    global maxBrokenEggs

    if currentIndex == N:
        maxBrokenEggs = max(maxBrokenEggs, breakPoint)
        return

    # 계란이 깨져있는 경우
    if S[currentIndex] <= 0:
        backtracking(currentIndex+1, breakPoint)
        return

    hitFlag = False
    for i in range(N):
        if currentIndex != i and S[i] > 0:
            hitFlag = True
            S[i] -= W[currentIndex]
            S[currentIndex] -= W[i]

            brokenCount = breakPoint
            if S[i] <= 0:
                brokenCount += 1
            if S[currentIndex] <= 0:
                brokenCount += 1

            backtracking(currentIndex+1, brokenCount)

            S[i] += W[currentIndex]
            S[currentIndex] += W[i]

    if not hitFlag:
        backtracking(currentIndex+1, breakPoint)

backtracking(0, 0)

print(maxBrokenEggs)
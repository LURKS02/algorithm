import sys
input = sys.stdin.readline

# N = 밀키트의 재료 수 (200,000)
# G = 세균 수의 합 제한 (1,000,000,000)
# K = 빼는 재료의 수 (200,000)
N, G, K = map(int, input().rstrip().split())

importantGradients = []
unimportantGradients = []

for i in range(N):
    # S = 부패 속도 (1,000,000,000)
    # L = 유통기한 (1,000,000,000)
    # O = 중요한 재료인지 여부 (1 = 중요 x)
    S, L, O = map(int, input().rstrip().split())
    if O == 0:
        importantGradients.append((S, L))
    else:
        unimportantGradients.append((S, L))

start = 0
end = 2000000001
ans = 0

def canEatAfterDays(x):
    totalVirus = 0
    additionalViruses = []

    for s, l in importantGradients:
        totalVirus += s * max(1, x-l)

    for s, l in unimportantGradients:
        additionalViruses.append(s * max(1, x-l))

    additionalViruses.sort(reverse=True)
    totalVirus += sum(additionalViruses[K:])

    return totalVirus <= G

while start <= end:
    mid = (start + end) // 2

    if canEatAfterDays(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
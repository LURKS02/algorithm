# N = 도시의 수 (100000)
# M = 여행하는 날짜 (100000)
# P = 여행 일정
N, M = map(int, input().split())
P = list(map(int, input().split()))
ways = []
count = [0] * (N+1)

for _ in range(N-1):
    A, B, C = map(int, input().split())
    ways.append((A, B, C))

for i in range(M-1):
    if P[i] < P[i+1]:
        count[P[i]] += 1
        count[P[i+1]] -= 1
    else:
        count[P[i+1]] += 1
        count[P[i]] -= 1

for i in range(1, N+1):
    count[i] += count[i-1]

# print(count)

result = 0

for i in range(1, N):
    if count[i]:
        result += min(ways[i-1][2] + count[i] * ways[i-1][1], ways[i-1][0] * count[i])
print(result)

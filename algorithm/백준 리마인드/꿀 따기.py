N = int(input())
honey = list(map(int, input().split()))

fs = [0] * (N+1)
for i in range(1, N+1):
    fs[i] = fs[i-1] + honey[i-1]

maxHoney = 0

# 1. 양쪽에서 접근하는 경우
for i in range(N):
    maxHoney = max(maxHoney, fs[N] - honey[0] - honey[-1] + honey[i])

# 2. 왼쪽에서 모두 접근하는 경우
for i in range(1, N-1):
    maxHoney = max(maxHoney, fs[N] - honey[0] - honey[i] + fs[N] - fs[i+1])

# 3. 오른쪽에서 모두 접근하는 경우
for i in range(1, N-1):
    maxHoney = max(maxHoney, fs[N-1] - honey[i] + fs[i])

print(maxHoney)

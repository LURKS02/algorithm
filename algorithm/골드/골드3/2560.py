import sys
input = sys.stdin.readline
DIV = 1000

# a = 성체가 되는 날
# b = 개체를 만들어내지 않는 날
# d = 죽는 날
# N = 벌레 수를 알고 싶은 날
a, b, d, N = map(int, input().split())

dp = [0] * (N+1)
dp[0] = 1

prefixSum = 0

for i in range(1, N+1):
    prefixSum = (prefixSum + dp[i-a] - dp[i-b] + DIV) % DIV
    dp[i] = prefixSum

sm = 0
for i in range(max(0, N-d+1), N+1):
    sm = (sm + dp[i]) % DIV
print(sm)
# print(dp)
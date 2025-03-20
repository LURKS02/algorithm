N, M = map(int, input().split())

MOD = 1000000007

def solve(a, b):
    if b == 1:
        return a % MOD

    result = solve(a, b // 2)
    if b % 2:
        return (result * result * a) % MOD
    else:
        return (result * result) % MOD

a = 1
for n in range(N - M + 1, N+1):
    a *= n
    a %= MOD

b = 1
for m in range(1, M+1):
    b *= m
    b %= MOD

result = (a * solve(b, MOD - 2)) % MOD
print(result)
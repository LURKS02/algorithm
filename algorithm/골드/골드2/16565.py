import sys
input = sys.stdin.readline
MOD = 10007

def cal(x, n):
    if n == 1:
        return x
    cal2 = cal(x, n//2)
    if n % 2:
        return cal2 * cal2 * x
    return cal2 * cal2

def div(x, y):
    return x*cal(y, MOD-2) % MOD
def combination(n, k):
    numor = 1
    denom = 1

    for i in range(k):
        numor = numor * (n-i) % MOD
        denom = denom * (i+1) % MOD

    return div(numor, denom)
def NCard(N):
    result = 0
    for i in range(1, N//4+1):
        result += combination(52-i*4, N-i*4) * combination(13, i) * ((-1) ** (i-1))
        result %= MOD
    return result

print(NCard(int(input())))
N, M, K = map(int, input().split())

if M > K:
    val = M - K
else:
    val = K - M

print(N - val)
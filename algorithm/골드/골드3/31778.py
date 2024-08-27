N, K = map(int, input().split())
S = list(input())

start = 0
end = N-1

while K > 0 and start < end:
    while start < N and S[start] == "P":
        start += 1
    while end > 0 and S[end] == "C":
        end -= 1
    if start < end:
        K -= 1
        S[start] = "P"
        S[end] = "C"

a = 0
b = 0
c = 0

for position in S:
    if position == "P":
        b += a
        a += 1
    else:
        c += b

print(c)
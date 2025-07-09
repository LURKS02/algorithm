N, K, T = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) % K != 0:
    print("NO")
    exit(0)

haveToMake = sum(A) // K
made = 0

A.sort(reverse=True)

start = 0
end = len(A)-1

while start < end:
    needToIncrease = K - A[start]
    canMove = min(A[end], needToIncrease)

    if T < canMove:
        break

    T -= canMove
    A[end] -= canMove
    A[start] += canMove

    if A[end] == 0:
        end -= 1

    if A[start] == K:
        start += 1
        made += 1

if made == haveToMake:
    print("YES")
else:
    print("NO")

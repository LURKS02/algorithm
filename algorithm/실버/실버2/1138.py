N = int(input())

l = list(map(int, input().split()))

new = [-1 for _ in range(N)]

for i in range(N):
    count = 0
    start = 0
    while count != l[i]:
        if new[start] == -1:
            count += 1
            start += 1
        else:
            start += 1
    while new[start] != -1:
        start += 1
    new[start] = i+1

print(*new)
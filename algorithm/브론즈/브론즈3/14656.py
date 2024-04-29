N = int(input())

patta = list(map(int, input().split()))

sum = 0
for i in range(N):
    if i + 1 != patta[i]:
        sum += 1

print(sum)
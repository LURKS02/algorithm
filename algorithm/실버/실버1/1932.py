import sys

input = sys.stdin.readline

n = int(input().rstrip())

l = []

for _ in range(n):
    new = list(map(int, input().rstrip().split()))
    l.append(new)

for i in range(1, n):
    for j in range(i+1):
        value = l[i][j]
        if j == 0:
            l[i][j] = l[i-1][0] + value
        elif j == i:
            l[i][j] = l[i-1][j-1] + value
        else:
            l[i][j] = max(l[i-1][j-1] + value, l[i-1][j] + value)

print(max(l[-1]))
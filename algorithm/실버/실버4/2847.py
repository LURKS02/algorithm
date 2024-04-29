N = int(input())

l = []

for _ in range(N):
    l.append(int(input()))

count = 0
for i in range(N-1, 0, -1):
    if l[i] <= l[i-1]:
        count += l[i-1] - l[i] + 1
        newnum = l[i] - 1
        l[i-1] = newnum
print(count)
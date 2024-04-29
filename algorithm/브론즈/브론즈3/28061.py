N = int(input())

l = list(map(int, input().split()))

newl = []

for i in range(len(l)):
    newl.append(l[i] - (N - i))
print(max(newl))
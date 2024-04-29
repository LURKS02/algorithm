N = int(input())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)

sum = 0
for i in range(N):
    sum += listA[i] * listB[i]

print(sum)
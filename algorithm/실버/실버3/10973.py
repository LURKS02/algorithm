N = int(input())

l = list(map(int, input().split()))

index = -1
for i in range(len(l)-1, 0, -1):
    if l[i] < l[i-1]:
        index = i-1
        break

if index == -1:
    print(-1)
else:
    max = 0
    ind = -1
    for i in range(index + 1, len(l)):
        if l[i] < l[index] and l[i] > max:
            max = l[i]
            ind = i
    l[index], l[ind] = l[ind], l[index]

    first = l[:index + 1]
    second = sorted(l[index + 1:], reverse=True)

    for num in first:
        print(num, end=' ')
    for num in second:
        print(num, end=' ')
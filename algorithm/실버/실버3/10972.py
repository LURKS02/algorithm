N = int(input())
l = list(map(int, input().split()))

index = -1
for i in range(len(l) - 1, 0, -1):
    if l[i] > l[i-1]:
        index = i-1
        break

if index == -1:
    print(-1)
else:
    newindex = -1
    for j in range(len(l) - 1, index, -1):
        if l[j] > l[index]:
            newindex = j
            break

    temp = l[index]
    l[index] = l[newindex]
    l[newindex] = temp

    sortl = sorted(l[index + 1:])
    newl = l[:index + 1] + sortl
    print(' '.join(map(str, newl)))

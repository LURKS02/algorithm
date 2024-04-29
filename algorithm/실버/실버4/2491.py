N = int(input())

l = list(map(int, input().split()))

def findMax(l):
    count = 1
    maxcount = 1
    for i in range(1, len(l)):
        if l[i] >= l[i-1]:
            count += 1
        else:
            if maxcount < count:
                maxcount = count
            count = 1
    if maxcount < count:
        maxcount = count
    return maxcount

def findMin(l):
    count = 1
    maxcount = 1
    for i in range(1, len(l)):
        if l[i] <= l[i-1]:
            count += 1
        else:
            if maxcount < count:
                maxcount = count
            count = 1
    if maxcount < count:
        maxcount = count
    return maxcount

print(max(findMax(l), findMin(l)))

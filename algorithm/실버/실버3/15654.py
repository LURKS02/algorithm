N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()


s = []
def printNums():
    if len(s) == M:
        for num in s:
            print(num, end=' ')
        print()
        return
    else:
        for i in range(N):
            if l[i] not in s:
                s.append(l[i])
                printNums()
                s.pop()
printNums()
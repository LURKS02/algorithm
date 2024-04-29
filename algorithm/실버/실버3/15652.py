
l = []
def getNum(start, end, M):
    if len(l) == M:
        for num in l:
            print(num, end=' ')
        print()

    else:
        for i in range(start, end + 1):
            l.append(i)
            getNum(i, end, M)
            l.pop()

N, M = map(int, input().split())
getNum(1, N, M)
N, M = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

s = []
def getNums(start):
    if len(s) == M:
        for num in s:
            print(num, end= ' ')
        print()

    else:
        for i in range(start, N):
            s.append(l[i])
            getNums(i)
            s.pop()

getNums(0)
N, M = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

s = []

def getNums(start):
    if len(s) == M:
        print(' '.join(map(str, s)))

    else:
        for i in range(start, N):
            s.append(l[i])
            getNums(i + 1)
            s.pop()

getNums(0)
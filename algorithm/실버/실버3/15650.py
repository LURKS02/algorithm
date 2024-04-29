N, M = map(int, input().split())

l = []

def backtracking(l, start, end, M):
    if len(l) == M:
        for num in l:
            print(num, end=' ')
        print()
        return
    else:
        for i in range(start, end + 1):
            if i not in l:
                l.append(i)
                backtracking(l, i + 1, end, M)
                l.pop()

backtracking(l, 1, N, M)
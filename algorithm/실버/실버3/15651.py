N, M = map(int, input().split())

l = []

def backtracking(l, N, M):
    if len(l) == M:
        for num in l:
            print(num, end=' ')
        print()
        return
    else:
        for i in range(1, N + 1):
            l.append(i)
            backtracking(l, N, M)
            l.pop()

backtracking(l, N, M)
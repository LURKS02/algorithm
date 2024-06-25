import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

paper = [list(map(int, input().split())) for _ in range(10)]
remain = [0, 5, 5, 5, 5, 5]
total = 25

def check(x, y, offset):
    for i in range(x, x+offset):
        for j in range(y, y+offset):
            if paper[i][j] != 1: return False
    return True

def backtracking(x, y, c):
    global remain, total

    if x >= 10:
        total = min(total, c)
        return

    if y >= 10:
        backtracking(x+1, 0, c)
        return

    if paper[x][y] == 1:
        for size in range(1, 6):
            if remain[size] == 0: continue
            if x+size-1 >= 10 or y+size-1 >= 10: continue

            if not check(x, y, size): break

            for i in range(x, x+size):
                for j in range(y, y+size):
                    paper[i][j] = 0
            remain[size] -= 1
            backtracking(x, y+size, c+1)
            remain[size] += 1
            for i in range(x, x+size):
                for j in range(y, y+size):
                    paper[i][j] = 1
    else:
        backtracking(x, y+1, c)

backtracking(0, 0, 0)
print(-1 if total == 25 else total)
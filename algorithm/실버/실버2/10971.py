N = int(input())

l = []
for _ in range(N):
    newl = list(map(int, input().split()))
    l.append(newl)

visited = [False] * N
cost = float('inf')

def backtracking(city, c, count):
    global cost
    if count == N and l[city][0]:
        cost = min(cost, c + l[city][0])
        return

    for i in range(N):
        if not visited[i] and l[city][i]:
            visited[i] = True
            backtracking(i, c + l[city][i], count + 1)
            visited[i] = False

visited[0] = True
backtracking(0, 0, 1)
print(cost)
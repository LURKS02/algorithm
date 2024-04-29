n = int(input())

A, B = map(int, input().split())

dict = {k : [] for k in range(1, n + 1)}

for _ in range(int(input())):
    x, y = map(int, input().split())
    dict[x].append(y)
    dict[y].append(x)

visited = [False for _ in range(n + 1)]

result = False

def dfs(n, count):
    if not visited[n]:
        visited[n] = True
        count += 1
        if B in dict[n]:
            print(count)
            global result
            result = True
        else:
            for k in dict[n]:
                dfs(k, count)

dfs(A, 0)

if not result:
    print(-1)

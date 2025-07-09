import bisect
from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    select = list(map(int, input().split()))

    notSelected = set()
    selected = set()

    def dfs(start):
        vs = dict()
        visited = [start]
        index = 1

        deq = deque()
        deq.append(start)
        vs[start] = 0

        while deq:
            node = deq.popleft()

            if select[node - 1] in selected or select[node - 1] in notSelected:
                for k in range(len(visited)):
                    notSelected.add(visited[k])
                return

            if select[node-1] not in vs:
                visited.append(select[node - 1])
                vs[select[node-1]] = index
                index += 1
                deq.append(select[node - 1])

            else:
                idx = vs[select[node-1]]

                for k in range(idx):
                    notSelected.add(visited[k])

                for k in range(idx, len(visited)):
                    selected.add(visited[k])

                return

        for k in range(len(visited)):
            notSelected.add(visited[k])


    for i in range(1, N+1):
        if i not in selected and i not in notSelected:
            dfs(i)

    print(N - len(selected))

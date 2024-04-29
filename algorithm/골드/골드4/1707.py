import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input().rstrip())

def dfs(graph, start, dp):
    deq = deque()
    deq.append(start)
    dp[start] = 1

    while(deq):
        currentNode = deq.pop()

        if currentNode in graph:
            for node in graph[currentNode]:
                if dp[node] != -1:
                    if dp[currentNode] ^ dp[node] == 0:
                        return False
                else:
                    dp[node] = ~dp[currentNode]
                    deq.append(node)

    return True

for _ in range(testcase):
    V, E = map(int, input().rstrip().split())
    dict = {}

    for _ in range(E):
        u, v = map(int, input().rstrip().split())

        if u in dict:
            dict[u].append(v)
        else:
            dict[u] = [v]

        if v in dict:
            dict[v].append(u)
        else:
            dict[v] = [u]

    # print(dict)

    dp = [-1 for _ in range(V + 1)]

    result = True

    for i in range(1, V + 1):
        if dp[i] == -1:
            result = result & dfs(dict, i, dp)

    if result:
        print('YES')
    else:
        print('NO')

answer = 0
def solution(n, lighthouse):
    graph = [set() for _ in range(n + 1)]

    for node1, node2 in lighthouse:
        graph[node1].add(node2)
        graph[node2].add(node1)
    solve(n, graph)

    return answer

def solve(n, graph):
    lightedSet = set()
    for key in range(1, n + 1):
        # leaf
        if len(graph[key]) == 1:
            # parent
            parent = graph[key].pop()
            lightedSet.add(parent)
            graph[parent].remove(key)

    if len(lightedSet) == 0:
        return
    for lighted in list(lightedSet):
        while graph[lighted]:
            neighbor = graph[lighted].pop()
            for cous in graph[neighbor]:
                if cous != lighted:
                    graph[cous].remove(neighbor)
            graph[neighbor] = set()

    global answer
    answer += len(lightedSet)

    return solve(n, graph)

print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
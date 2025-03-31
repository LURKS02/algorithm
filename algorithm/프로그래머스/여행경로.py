from collections import defaultdict
def solution(tickets):
    graph = dict()

    for t1, t2 in tickets:
        if t1 not in graph:
            graph[t1] = defaultdict(int)
        graph[t1][t2] += 1

    answer = []

    def dfs(current, arr, count):
        nonlocal answer
        if count == len(tickets):
            if answer == []:
                answer = arr[:]
            else:
                isChanged = False
                for i in range(len(tickets) + 1):
                    if answer[i] > arr[i]:
                        isChanged = True
                        break
                    elif answer[i] < arr[i]:
                        isChanged = False
                        break
                if isChanged:
                    answer = arr[:]
            return

        if current in graph:
            for neighbor in graph[current].keys():
                if graph[current][neighbor] > 0:
                    graph[current][neighbor] -= 1
                    arr.append(neighbor)
                    dfs(neighbor, arr, count+1)
                    arr.pop()
                    graph[current][neighbor] += 1

    dfs("ICN", ["ICN"], 0)

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

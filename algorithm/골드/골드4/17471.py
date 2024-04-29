from itertools import combinations
from collections import deque

def check_connected(area, adj):
    queue = deque([area[0]])
    visited = {area[0]}
    while queue:
        current = queue.popleft()
        for neighbor in adj[current]:
            if neighbor in area and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return len(visited) == len(area)

def calculate_difference(area1, area2, populations):
    population1 = sum(populations[i-1] for i in area1)
    population2 = sum(populations[i-1] for i in area2)
    return abs(population1 - population2)

def min_population_difference(N, populations, adj):
    min_diff = float('inf')
    for i in range(1, N//2 + 1):
        for area1 in combinations(range(1, N+1), i):
            area2 = [j for j in range(1, N+1) if j not in area1]
            if check_connected(area1, adj) and check_connected(area2, adj):
                diff = calculate_difference(area1, area2, populations)
                min_diff = min(min_diff, diff)
    return min_diff if min_diff != float('inf') else -1

N = int(input())
populations = list(map(int, input().split()))
adj = {i: [] for i in range(1, N+1)}

for i in range(1, N+1):
    info = list(map(int, input().split()))
    adj[i] = info[1:]

result = min_population_difference(N, populations, adj)
print(result)
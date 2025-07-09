from collections import deque, defaultdict
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

N = int(input())
graph = defaultdict(list)

price = [1] * N

for _ in range(N-1):
    a, b, p, q = map(int, input().split())
    A, B = price[a], price[b]
    minp, minq = p // (math.gcd(p, q)), q // (math.gcd(p, q))

    l = lcm(A, B)
    newA, newB = l * minp, l * minq

    price[a] = newA
    price[b] = newB

    graph[a].append(b)
    graph[b].append(a)

    deq = deque()

    deq.append((a, A))
    deq.append((b, B))
    visited = set()
    visited.add(a)
    visited.add(b)

    while deq:
        n, prev = deq.popleft()

        haveToMultiply = price[n] // prev
        for neighbor in graph[n]:
            if neighbor not in visited:
                visited.add(neighbor)
                origin = price[neighbor]
                price[neighbor] = price[neighbor] * haveToMultiply
                deq.append((neighbor, origin))

g = price[0]
for i in range(1, len(price)):
    g = math.gcd(g, price[i])

for i in range(len(price)):
    price[i] = price[i] // g

print(*price)
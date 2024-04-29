import heapq

N, M = map(int, input().split())

up = {}
down = {}

for _ in range(N):
    x, y = map(int, input().split())
    up[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    down[u] = v

# print(up)
# print(down)
deq = [(0, 1)]
visited = [False for _ in range(101)]
visited[1] = True

while deq:
    count, current = heapq.heappop(deq)

    if current == 100:
        print(count)
        break

    elif current in up:
        heapq.heappush(deq, (count, up[current]))

    elif current in down:
        heapq.heappush(deq, (count, down[current]))

    else:
        for i in range(1, 7):
            newPosition = current + i
            if newPosition <= 100 and not visited[newPosition]:
                if newPosition not in up and newPosition not in down:
                    visited[newPosition] = True
                heapq.heappush(deq, (count + 1, newPosition))
    # print(deq)
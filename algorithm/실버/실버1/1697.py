from collections import deque

N, K = map(int, input().split())

visited = set()


def bfs(start):
    deq = deque()
    deq.append((start, 0))

    while(deq):
        item = deq.popleft()
        position = item[0]
        c = item[1]

        if position == K:
            print(c)
            break

        if position not in visited:
            visited.add(position)

            if position-1 >= 0:
                deq.append((position-1, c+1))
            if position+1 <= 100000:
                deq.append((position+1, c+1))
            if position*2 <= 100000:
                deq.append((position*2, c+1))

bfs(N)



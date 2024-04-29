from collections import deque

F, S, G, U, D = map(int, input().split())

visited = set()

def bfs(start, visited):
    deq = deque()
    deq.append((start, 0))

    ans = -1

    while(deq):
        currentPosition, count = deq.popleft()

        if currentPosition == G:
            ans = count
            break

        if currentPosition not in visited and currentPosition > 0 and currentPosition <= F:
            visited.add(currentPosition)
            deq.append((currentPosition + U, count + 1))
            deq.append((currentPosition - D, count + 1))

    if ans != -1:
        print(ans)
    else:
        print('use the stairs')


bfs(S, visited)
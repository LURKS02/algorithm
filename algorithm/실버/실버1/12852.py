from collections import deque

N = int(input())

def bfs(start):
    deq = deque()
    deq.append((start, [start]))

    visited = set()

    while(deq):
        num, queue = deq.popleft()
        if num == 1:
            return queue

        visited.add(num)

        if num % 3 == 0 and (num // 3) not in visited:
            deq.append((num // 3, queue + [num // 3]))
        if num % 2 == 0 and (num // 2) not in visited:
            deq.append((num // 2, queue + [num // 2]))
        if num > 1 and (num-1) not in visited:
            deq.append((num - 1, queue + [num - 1]))

ans = bfs(N)
print(len(ans) - 1)
print(*ans)

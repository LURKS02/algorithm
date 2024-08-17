from collections import deque

N, K = map(int, input().split())
l = list(map(int, input().split()))

answer = ''.join(map(str, sorted(l)))

initial = ''.join(map(str, l))

visited = set()

deq = deque()
deq.append((initial, 0))
visited.add(initial)

while deq:
    state, count = deq.popleft()

    if state == answer:
        print(count)
        exit(0)

    for i in range(N - K + 1):
        stateReversedString = state[:i] + state[i:i+K][::-1] + state[i+K:]
        if stateReversedString not in visited:
            visited.add(stateReversedString)
            deq.append((stateReversedString, count + 1))

print(-1)


import collections

arr = [input()[2:] for _ in range(3)]
visited = collections.defaultdict(int)
deq = collections.deque()

deq.append((arr[0], arr[1], arr[2], 0))

while deq:
    A, B, C, count = deq.popleft()
    contStr = A + "/" + B + "/" + C

    if 'B' not in A and 'C' not in A:
        if 'A' not in B and 'C' not in B:
            if 'A' not in C and 'B' not in C:
                print(count)
                exit(0)

    if not visited[contStr]:
        visited[contStr] += 1

        if len(A) > 0:
            deq.append((A[:-1], B + A[-1], C, count + 1))
            deq.append((A[:-1], B, C + A[-1], count + 1))
        if len(B) > 0:
            deq.append((A, B[:-1], C + B[-1], count + 1))
            deq.append((A + B[-1], B[:-1], C, count + 1))
        if len(C) > 0:
            deq.append((A, B + C[-1], C[:-1], count + 1))
            deq.append((A + C[-1], B, C[:-1], count + 1))

print(-1)
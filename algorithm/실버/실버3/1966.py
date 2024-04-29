from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))

    deq = deque(l)
    indexq = deque(range(N))

    count = 0
    while(deq):
        if deq[0] == max(deq):
            count += 1
            if indexq[0] == M:
                print(count)
                break
            else:
                deq.popleft()
                indexq.popleft()
        else:
            d = deq.popleft()
            deq.append(d)
            i = indexq.popleft()
            indexq.append(i)
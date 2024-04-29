from collections import deque

N = int(input())
l = list(map(int, input().split()))

poplist = deque([i for i in range(1, N + 1)])

while(poplist):
    index = poplist.popleft()
    print(index, end=' ')
    if l[index - 1] > 0:
        poplist.rotate(-l[index - 1] + 1)
    else:
        poplist.rotate(-l[index - 1])


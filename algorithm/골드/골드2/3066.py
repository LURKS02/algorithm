import sys
import bisect

input = sys.stdin.readline

def max_signals(N, ports):
    lis = []
    for port in ports:
        pos = bisect.bisect_left(lis, port)
        if pos == len(lis):
            lis.append(port)
        else:
            lis[pos] = port
        print(lis)
    return len(lis)

T = int(input())
for _ in range(T):
    N = int(input())
    ports = []
    for _ in range(N):
        ports.append(int(input()))
    print(max_signals(N, ports))
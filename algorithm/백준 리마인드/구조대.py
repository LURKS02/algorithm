from collections import defaultdict

N, M = map(int, input().split())

dic = defaultdict()

for _ in range(N):
    l, r, c = map(int, input().split())
    
    dic[c].append((l, r))


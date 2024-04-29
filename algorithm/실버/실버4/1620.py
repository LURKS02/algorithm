import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
pokemon = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    pokemon[i + 1] = name
    pokemon[name] = i + 1

for i in range(M):
    query = sys.stdin.readline().rstrip()
    if query.isdigit():
        query = int(query)
        print(pokemon[query])
    else:
        print(pokemon[query])


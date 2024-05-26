import sys
input = sys.stdin.readline

k = int(input())
totalNode = pow(2, k + 1)
edges = [0] + list(map(int, input().split()))
edgeSum = sum(edges)

nowStart = totalNode // 2 - 1
nowEnd = totalNode - 1

# print(nowStart, nowEnd)

while nowEnd:
    for i in range((nowEnd - nowStart) // 2):
        childEdge = nowStart + (2*i)
        nextNode = childEdge // 2

        edges[nextNode] += max(edges[childEdge],edges[childEdge + 1])
        edgeSum += abs(edges[childEdge] - edges[childEdge + 1])

    nowEnd = nowStart
    nowStart = nowStart // 2

print(edgeSum)
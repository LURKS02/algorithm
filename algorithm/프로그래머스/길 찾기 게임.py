import sys
sys.setrecursionlimit(10**9)

def findMaxYIndex(nodes, startIndex, endIndex):
    maxValue = -1
    maxIndex = -1
    for i in range(startIndex, endIndex):
        if nodes[i][2] > maxValue:
            maxValue = nodes[i][2]
            maxIndex = i

    return maxIndex

def preorder(nodes, startIndex, endIndex):
    if startIndex == endIndex:
        return []

    if startIndex + 1 == endIndex:
        return [nodes[startIndex][0]]

    maxYIndex = findMaxYIndex(nodes, startIndex, endIndex)

    leftSubtree = preorder(nodes, startIndex, maxYIndex)
    rightSubtree = preorder(nodes, maxYIndex+1, endIndex)
    return [nodes[maxYIndex][0]] + leftSubtree + rightSubtree

def postorder(nodes, startIndex, endIndex):
    if startIndex == endIndex:
        return []
    if startIndex + 1 == endIndex:
        return [nodes[startIndex][0]]

    maxYIndex = findMaxYIndex(nodes, startIndex, endIndex)

    leftSubtree = postorder(nodes, startIndex, maxYIndex)
    rightSubtree = postorder(nodes, maxYIndex+1, endIndex)
    return leftSubtree + rightSubtree + [nodes[maxYIndex][0]]

def solution(nodeinfo):
    indexedArray = [(index+1, x, y) for index, (x, y) in enumerate(nodeinfo)]
    indexedArray.sort(key=lambda x: x[1])
    return [preorder(indexedArray, 0, len(nodeinfo)), postorder(indexedArray, 0, len(nodeinfo))]

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
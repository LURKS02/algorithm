import sys
input = sys.stdin.readline

n = int(input())
tree = [0]*(4 * 10**6)

def findCandy(left, right, node, B):
    tree[node] -= 1
    if left == right:
        return left

    mid = (left + right) // 2
    if tree[node*2] >= B:
        return findCandy(left, mid, node*2, B)
    else:
        return findCandy(mid+1, right, node*2+1, B-tree[node*2])

def putCandy(left, right, node, B, C):
    tree[node] += C
    if left == right:
        return

    mid = (left + right) // 2
    if B <= mid:
        putCandy(left, mid, node*2, B, C)
    else:
        putCandy(mid+1, right, node*2+1, B, C)


for _ in range(n):
    line = list(map(int, input().split()))
    if len(line) == 2:
        B = line[1]
        print(findCandy(1, 10**6, 1, B))
    else:
        _, B, C = line
        putCandy(1, 10**6, 1, B, C)


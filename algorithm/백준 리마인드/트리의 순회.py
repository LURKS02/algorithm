import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents, end=' ')

    left = position[parents] - in_start

    preorder(in_start, position[parents]-1, post_start, post_start + left - 1)
    preorder(position[parents]+1, in_end, post_start+left, post_end-1)

N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (N+1)
for i in range(N):
    position[inorder[i]] = i

preorder(0, N-1, 0, N-1)
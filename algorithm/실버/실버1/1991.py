class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node, result):
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)

def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)

n = int(input())
tree = {}

for _ in range(n):
    node, left, right = input().split()
    if node not in tree:
        tree[node] = TreeNode(node)
    if left != '.':
        tree[node].left = TreeNode(left)
        tree[left] = tree[node].left
    if right != '.':
        tree[node].right = TreeNode(right)
        tree[right] = tree[node].right

preorder_result = []
inorder_result = []
postorder_result = []

preorder(tree['A'], preorder_result)
inorder(tree['A'], inorder_result)
postorder(tree['A'], postorder_result)

print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))
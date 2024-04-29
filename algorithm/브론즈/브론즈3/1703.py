def cutTree(tree, split, cut):
    return tree * split - cut

while(1):
    tree = input()
    if tree == '0':
        break
    trees = list(map(int, (tree.split())))
    N = trees[0]
    mytree = trees[1:]
    treeTuple = [(mytree[i], mytree[i + 1]) for i in range(0, len(mytree) - 1, 2)]
    result = 1
    for tuple in treeTuple:
        result = cutTree(result, tuple[0], tuple[1])

    print(result)




def scale(depth, left, right):
    weight = abs(left - right)
    if weight not in possible:
        possible.append(weight)
    if depth == weightNum:
        return
    if not ans[depth][weight]:
        scale(depth + 1, left + weights[depth], right)
        scale(depth + 1, left, right + weights[depth])
        scale(depth + 1, left, right)

        ans[depth][weight] = True


weightNum = int(input())
weights = list(map(int, input().split()))
marbleNum = int(input())
marbles = list(map(int, input().split()))

possible = []
ans = [[False] * 15001 for i in range(weightNum + 1)]

scale(0, 0, 0)

for m in marbles:
    if m in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')


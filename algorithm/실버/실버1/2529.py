def check(x, y, operation):
    if operation == '<':
        return x < y
    if operation == '>':
        return x > y
    return False

def backtracking(index, value):
    global minstr, maxstr, minValue, maxValue

    if index == k + 1:
        if minValue > int(value):
            minValue = int(value)
            minstr = value
        if maxValue < int(value):
            maxValue = int(value)
            maxstr = value

        return

    for i in range(10):
        if not visited[i] and (index == 0 or check(value[-1], str(i), signs[index-1])):
            visited[i] = True
            backtracking(index + 1, value + str(i))
            visited[i] = False



k = int(input())
signs = input().split()
visited = [False] * 10
minValue, maxValue = float('inf'), 0
minstr, maxstr = None, None

backtracking(0, '')
print(maxstr)
print(minstr)
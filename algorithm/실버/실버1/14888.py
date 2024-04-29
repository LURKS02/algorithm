N = int(input())

l = list(map(int, input().split()))

s, m, p, d = map(int, input().split())

maxValue = -int(1e9)
minValue = int(1e9)

def backtracking(count, currentValue, s, m, p, d):
    global maxValue, minValue
    if s < 0 or m < 0 or p < 0 or d < 0:
        return

    if count == N:
        if currentValue > maxValue:
            maxValue = currentValue
        if currentValue < minValue:
            minValue = currentValue
        return

    backtracking(count+1, currentValue + l[count], s-1, m, p, d)
    backtracking(count+1, currentValue - l[count], s, m-1, p, d)
    backtracking(count+1, currentValue * l[count], s, m, p-1, d)
    if currentValue < 0:
        backtracking(count+1, abs(currentValue) // l[count] * -1, s, m, p, d-1)
    else:
        backtracking(count+1, currentValue // l[count], s, m, p, d-1)

backtracking(1, l[0], s, m, p, d)

print(maxValue)
print(minValue)
N, K = map(int, input().split())

left = 0
right = N//2

while left <= right:
    rowCut = (left + right) // 2
    colCut = N - rowCut

    pieces = (rowCut + 1) * (colCut + 1)

    if pieces == K:
        print("YES")
        exit(0)

    if K > pieces:
        left = rowCut + 1

    else:
        right = rowCut - 1

print("NO")
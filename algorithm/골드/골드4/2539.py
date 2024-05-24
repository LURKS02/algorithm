# row = 행 (1,000,000)
# col = 열 (1,000,000)
row, col = map(int, input().split())

# paper = 사용할 색종이 장 수 (100)
paper = int(input())

# missPoint = 잘못 칠해진 칸의 수 (1,000)
missPoint = int(input())

left = 0
right = 1000000

# points = 잘못 칠해진 칸의 위치
points = []
for _ in range(missPoint):
    rowNumber, colNumber = map(int, input().split())
    left = max(left, rowNumber)
    points.append((rowNumber, colNumber))

points.sort(key=lambda x: x[1])

ans = 0

while left <= right:
    mid = (left + right) // 2

    # 색종이가 시작하는 칸
    idx = 0
    # 현재까지 붙인 색종이 수
    cnt = 0

    while idx < missPoint:
        cnt += 1
        startX = points[idx][1]
        startY = 1
        i = idx

        while i < missPoint and startX <= points[i][1] < startX + mid and startY <= points[i][0] < startY + mid:
            i += 1

        idx = i

    if cnt <= paper:
        right = mid - 1
        ans = mid

    else:
        left = mid + 1

print(ans)
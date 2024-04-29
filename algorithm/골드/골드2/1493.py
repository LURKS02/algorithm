import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())
total = length * width * height
N = int(input())
cube = [tuple(map(int, input().split())) for _ in range(N)]
cube.sort(reverse=True)

# print(cube)

answer, totalNow = 0, 0
for idx, cnt in cube:
    totalNow *= 8
    cubeLength = 2 ** idx

    cubeLimit = (length // cubeLength) * (width // cubeLength) * (height // cubeLength) - totalNow
    cubeLimit = min(cnt, cubeLimit)

    answer += cubeLimit
    totalNow += cubeLimit

if totalNow == total:
    print(answer)
else:
    print(-1)
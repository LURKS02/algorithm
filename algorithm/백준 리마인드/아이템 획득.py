import sys
from collections import defaultdict
import bisect

NMAX = 200001

# 입력
N, Q = map(int, sys.stdin.readline().split())

# 데이터 저장
val = [defaultdict(list) for _ in range(NMAX)]

for _ in range(N):
    x, y, w = map(int, sys.stdin.readline().split())

    val[x][0].append((y, w))
    val[y][1].append((x, w))

# 정렬 및 누적합 계산
for i in range(NMAX):
    for j in range(2):
        if val[i][j]:
            val[i][j].sort()  # (좌표, 값) 기준 정렬
            for k in range(1, len(val[i][j])):
                val[i][j][k] = (val[i][j][k][0], val[i][j][k][1] + val[i][j][k-1][1])

# 이진 탐색 함수
def b_search(idx, sw, s):
    if idx >= len(val) or idx < 0 or sw not in val[idx] or not val[idx][sw]:
        return 0

    arr = val[idx][sw]
    index = bisect.bisect_right(arr, (s, float('inf'))) - 1

    if index < 0:
        return 0
    return arr[index][1]

# 이동 및 결과 계산
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pos = (1, 1)
ans = 0

for _ in range(Q):
    d, v = map(int, sys.stdin.readline().split())

    if d == 0:
        ans += b_search(pos[1], 1, pos[0] + v) - b_search(pos[1], 1, pos[0])
    elif d == 1:
        ans += b_search(pos[0], 0, pos[1] + v) - b_search(pos[0], 0, pos[1])
    elif d == 2:
        ans += b_search(pos[1], 1, pos[0] - 1) - b_search(pos[1], 1, pos[0] - v - 1)
    else:
        ans += b_search(pos[0], 0, pos[1] - 1) - b_search(pos[0], 0, pos[1] - v - 1)

    pos = (pos[0] + dx[d] * v, pos[1] + dy[d] * v)

# 결과 출력
print(ans)
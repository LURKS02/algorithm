import sys
import bisect

input = sys.stdin.readline

# N = 마을의 수 (200,000)
# Q = 후보 수 (200,000)
N, Q = map(int, input().rstrip().split())

# towns = 마을 정보 목록 (마을 위치, 거주 인원 수) (200,000)
towns = []

for _ in range(N):
    # a = 거주 인원 수
    # x = 마을의 위치
    a, x = map(int, input().rstrip().split())
    towns.append((x, a))

towns.sort()
cnt = [-sum(towns[i][1] for i in range(N))]

for i in range(N):
    cnt.append(cnt[-1] + towns[i][1]*2)

prefix = [sum((towns[i][0] - towns[0][0]) * towns[i][1] for i in range(N))]

for i in range(N-1):
    prefix.append(prefix[-1] + (towns[i+1][0] - towns[i][0]) * cnt[i+1])

for _ in range(Q):
    q = int(input().rstrip())
    i = bisect.bisect(towns, (q+1, 0))
    print(prefix[i-1] + (q - towns[i-1][0]) * cnt[i] if i else prefix[0] + (q-towns[0][0]) * cnt[0])
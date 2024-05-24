import sys
input = sys.stdin.readline

# N = 상자의 개수 (1,000,000)
# K = 규칙의 개수 (10,000)
# D = 도토리의 개수 (1,000,000,000)
N, K, D = map(int, input().split())

rules = []

for _ in range(K):
    # A번 상자부터 B번 상자까지 C개 간격으로 도토리를 넣는다.
    A, B, C = map(int, input().split())
    rules.append((A, B, C))

left = 1
right = N

while left <= right:
    # mid = 마지막 도토리가 담긴 상자 번호
    mid = (left + right) // 2

    cnt = 0
    for start, end, step in rules:
        # 기준보다 시작점 값이 큰 경우 (고려 대상 X)
        if start > mid:
            continue

        # 기준이 마지막 값보다 큰 경우 (고려 대상 O)
        if mid > end:
            cnt += (end - start) // step + 1

        # 기준이 마지막 값보다 작은 경우 (고려 대상 O)
        else:
            cnt += (mid - start) // step + 1

        if cnt >= D:
            right = mid - 1
            answer = mid
            break

    else:
        left = mid + 1

print(answer)


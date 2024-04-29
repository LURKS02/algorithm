import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushi = [int(input().rstrip()) for _ in range(N)]

def max_sushi_types(N, d, k, c, sushi):
    type_count = {c: 1}  # 쿠폰으로 먹을 수 있는 초밥 포함
    max_types = 0

    # 초기 윈도우 설정
    for i in range(k):
        type_count[sushi[i]] = type_count.get(sushi[i], 0) + 1

    max_types = len(type_count)  # 초기 윈도우에서의 종류 수

    # 슬라이딩 윈도우 이동
    for i in range(N):
        # 이전 초밥 제거
        prev_sushi = sushi[i % N]
        type_count[prev_sushi] -= 1
        if type_count[prev_sushi] == 0:
            del type_count[prev_sushi]

        # 새 초밥 추가
        new_sushi = sushi[(i + k) % N]
        type_count[new_sushi] = type_count.get(new_sushi, 0) + 1

        # 최대 종류 수 갱신
        max_types = max(max_types, len(type_count))

    return max_types


# 최댓값 계산
print(max_sushi_types(N, d, k, c, sushi))

import heapq
from collections import defaultdict

# 입력받기
n, m = map(int, input().split())  # n은 학생 수, m은 간선(점수) 수
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))  # 간선 정보를 (가중치, a, b) 형식으로 저장

# 간선들을 가중치 내림차순으로 정렬
edges.sort(reverse=True, key=lambda x: x[0])

# 학생 그룹에서 4명을 고르기 위한 세트
selected_students = set()

max_score = 0

# 탐욕적으로 상위 가중치 간선부터 선택
for c, a, b in edges:
    if len(selected_students) >= 4:
        break

    # 선택된 학생이 아니면 추가
    if a not in selected_students:
        selected_students.add(a)
    if b not in selected_students:
        selected_students.add(b)

    # 점수 합산
    max_score += c

    # 4명을 모두 선택한 경우 종료
    if len(selected_students) == 4:
        break

print(f"최대 점수: {max_score}")
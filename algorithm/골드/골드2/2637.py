N = int(input()) # 완제품의 번호
M = int(input())

relationships = []

for _ in range(M):
    X, Y, K = map(int, input().split())
    relationships.append((X, Y, K))

def calculate_parts(N, M, relationships):
    from collections import defaultdict, deque
    import sys
    sys.setrecursionlimit(10000)

    graph = defaultdict(list)
    basic_parts = set(range(1, N))
    for x, y, k in relationships:
        graph[x].append((y, k))
        if x in basic_parts:
            basic_parts.remove(x)

    def dfs(part):
        # 이미 계산된 경우 바로 반환
        if part in needed_parts:
            return needed_parts[part]

        # 현재 부품의 구성 정보를 담는 딕셔너리
        result = defaultdict(int)
        for subpart, count in graph[part]:
            subpart_needed = dfs(subpart)
            for key, val in subpart_needed.items():
                result[key] += val * count

        needed_parts[part] = result
        return result

    needed_parts = {}
    for part in basic_parts:
        needed_parts[part] = defaultdict(int, {part: 1})

    # 최종 제품의 필요 부품 계산
    final_needed_parts = dfs(N)

    # 결과 출력 형식에 맞게 정렬하여 반환
    result = sorted(final_needed_parts.items())
    return result

result = calculate_parts(N, M, relationships)

for r, c in result:
    print(r, c)
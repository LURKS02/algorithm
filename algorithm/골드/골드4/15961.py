import sys
input = sys.stdin.readline

def max_sushi_types(N, d, k, c, sushi):
    sushi_counter = {}
    # 무료로 먹을 수 있는 초밥
    sushi_counter[c] = 1
    types = 1

    for i in range(k):
        if sushi[i] in sushi_counter:
            sushi_counter[sushi[i]] += 1
        else:
            sushi_counter[sushi[i]] = 1
            types += 1

    max_types = types

    for i in range(N):
        remove_sushi = sushi[i]
        sushi_counter[remove_sushi] -= 1
        if sushi_counter[remove_sushi] == 0:
            del sushi_counter[remove_sushi]
            types -= 1

        add_sushi = sushi[(i + k) % N]
        if add_sushi in sushi_counter:
            sushi_counter[add_sushi] += 1

        else:
            sushi_counter[add_sushi] = 1
            types += 1

        max_types = max(max_types, types)

    return max_types

N, d, k, c = map(int, input().rstrip().split())
sushi = [int(input().rstrip()) for _ in range(N)]

print(max_sushi_types(N, d, k, c, sushi))
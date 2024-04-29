from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

def count_subsequences_with_sum(arr, target_sum):
    count = 0
    for subset in powerset(arr):
        if sum(subset) == target_sum:
            count += 1
    return count

# 입력 받기
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 부분수열의 합이 S가 되는 경우의 수 계산
result = count_subsequences_with_sum(numbers, S)

# 결과 출력
print(result)
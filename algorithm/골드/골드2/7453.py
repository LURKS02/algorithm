from collections import defaultdict

import sys
input = sys.stdin.readline

N = int(input().rstrip())

A, B, C, D = [], [], [], []

def count_zero_sums(A, B, C, D):
    ABsum = {}
    count = 0

    # A와 B에서 가능한 모든 합의 빈도 계산
    for a in A:
        for b in B:
            sum_ab = a + b
            if sum_ab in ABsum:
                ABsum[sum_ab] += 1
            else:
                ABsum[sum_ab] = 1

    # C와 D에서 가능한 모든 합이 ABsum의 반대값과 일치하는지 확인
    for c in C:
        for d in D:
            sum_cd = -(c + d)  # 합이 0이 되려면 이 값이 ABsum에 있어야 함
            if sum_cd in ABsum:
                count += ABsum[sum_cd]

    return count

for _ in range(N):
    a, b, c, d = map(int, input().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

print(count_zero_sums(A, B, C, D))
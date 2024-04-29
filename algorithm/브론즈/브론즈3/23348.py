A, B, C = map(int, input().split())

N = int(input())
maxSum = 0

for i in range(N):
    sum = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        grade = a*A + b*B + c*C
        sum += grade

    if sum > maxSum:
        maxSum = sum

print(maxSum)
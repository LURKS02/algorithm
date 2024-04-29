A1, A0 = map(int, input().split())
c = int(input())
n0 = int(input())

# A1 = c인 경우, a0가 0이거나 음수일 때 성립
if A1 == c and A0 <= 0:
    print(1)
# A1 < c인 경우, 부등식을 확인
elif A1 < c:
    # 계산된 n0
    calculated_n0 = -A0 / (A1 - c)
    # calculated_n0이 음수인 경우는 모든 n0에 대해 성립
    if calculated_n0 < 0 or n0 >= calculated_n0:
        print(1)
    else:
        print(0)
# 그 외의 경우 부등식이 성립하지 않음
else:
    print(0)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    for i in range(len(buildings)):
        bh = buildings[i]

        if bh == 0:
            continue

        l1, l2 = buildings[i - 2], buildings[i - 1]
        r1, r2 = buildings[i + 1], buildings[i + 2]

        if l1 >= bh or l2 >= bh or r1 >= bh or r2 >= bh:
            continue

        answer += bh - max(l1, l2, r1, r2)

    print("#" + strtest_case, answer)
from collections import deque

T = int(input())

for _ in range(T):
    deq = deque(list(input()))

    ans = 0

    if len(deq) % 2 == 1:
        ans += int(deq.popleft())

    while deq:
        firstNum = deq.popleft()
        secondNum = deq.popleft()

        num = int(firstNum) * 10 + int(secondNum)

        bestCase = float('inf')

        coin = num // 25

        for k in range(coin + 1):
            case = 0
            case += k
            remainingCoins = num - k * 25
            for c in str(remainingCoins):
                case += int(c)
            bestCase = min(bestCase, case)

        ans += bestCase

    print(ans)
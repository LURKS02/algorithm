N = int(input())

tasks = [(0, 0)]

for _ in range(N):
    T, P = map(int, input().split())
    tasks.append((T, P))

def getMaxProfit(day):
    if day > N:
        return 0

    profit = 0
    for i in range(day, N + 1):
        T, P = tasks[i]
        if i + T <= N + 1:
            profit = max(profit, P + getMaxProfit(i + T))

    return profit

print(getMaxProfit(1))
def countSum(N):
    start = end = 1
    sum = 1
    count = 0

    while end <= N:
        if sum < N:
            end += 1
            sum += end
        elif sum > N:
            sum -= start
            start += 1
        else:
            count += 1
            sum -= start
            start += 1

    return count

N = int(input())

print(countSum(N))
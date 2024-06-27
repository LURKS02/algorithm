N = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))
men.sort()
women.sort()

answer = 0

start = 0
end = N-1

while start < N and 0 <= end:
    if men[start] < 0 and women[end] > 0 and abs(men[start]) > women[end]:
        answer += 1
        start += 1
        end -= 1
    elif men[start] < 0 and women[end] > 0 and abs(men[start]) <= women[end]:
        end -= 1
    elif men[start] > 0 and women[end] < 0 and men[start] < abs(women[end]):
        answer += 1
        start += 1
        end -= 1
    elif men[start] > 0 and women[end] < 0 and men[start] >= abs(women[end]):
        end -= 1
    elif men[start] < 0 and women[end] < 0:
        start += 1
    elif men[start] > 0 and women[end] > 0:
        end -= 1

print(answer)
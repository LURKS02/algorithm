import sys

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
fixed = [int(input().rstrip()) for _ in range(M)]

sum = 1

if M == 0:
    print(fibonacci(N + 1))

else:
    for i in range(len(fixed)):
        if i == 0:
            sum *= fibonacci(fixed[i])
        else:
            sum *= fibonacci(fixed[i] - fixed[i-1])

        # print(sum)


    sum *= fibonacci(N - fixed[-1] + 1)

    print(sum)
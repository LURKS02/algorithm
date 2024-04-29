import math

def prime(num):
    if num == 1:
        return False

    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

N = int(input())
l = list(map(int, input().split()))

count = 0
for number in l:
    if prime(number):
        count += 1

print(count)
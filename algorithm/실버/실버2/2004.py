
n, m = map(int, input().split())

def getfactnum(n, factor):
    count = 0
    while(n):
        n //= factor
        count += n
    return count

count2 = getfactnum(n, 2) - getfactnum(m, 2) - getfactnum(n-m, 2)
count5 = getfactnum(n, 5) - getfactnum(m, 5) - getfactnum(n-m,5)

print(min(count2, count5))

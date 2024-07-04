import sys
input = sys.stdin.readline

try:
    while True:
        x = int(input().rstrip())*10000000
        n = int(input().rstrip())
        legos = [int(input().rstrip()) for _ in range(n)]

        temp = 0
        if x % 2 == 0 and legos.count(x//2) >= 2:
            temp = x // 2

        legoSet = set(legos)
        for lego in sorted(legos):
            if x - lego in legoSet and lego*2 != x:
                print("yes", lego, x-lego); break

        else:
            if temp: print("yes", temp, temp)
            else: print("danger")

except:pass
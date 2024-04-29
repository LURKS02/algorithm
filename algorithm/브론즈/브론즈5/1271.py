import sys

total, money = map(int, sys.stdin.readline().split())

print(total // money)
print(total % money)
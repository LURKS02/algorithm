count = -1

def recursion(s, l, r):
    global count
    if l >= r:
        count += 1
        return 1
    elif s[l] != s[r]:
        count += 1
        return 0
    else:
        count += 1
        return recursion(s, l+1, r-1)

def isPalindrome(st):
    global count
    count = 0
    return recursion(st, 0, len(st) - 1)

N = int(input())

for i in range(N):
    str = input()
    print(isPalindrome(str), count, end= ' ')
    print()
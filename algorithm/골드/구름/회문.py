def isPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

T = int(input())

for _ in range(T):
    string = input()
    left = 0
    right = len(string)-1

    resulted = False

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            if isPalindrome(string, left+1, right) or isPalindrome(string, left, right-1):
                print(1)
            else:
                print(2)
            resulted = True
            break

    if not resulted:
        print(0)

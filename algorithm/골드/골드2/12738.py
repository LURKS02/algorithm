import sys
import bisect

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

def lengthOfLis(nums):
    lis = []
    for num in nums:
        pos = bisect.bisect_left(lis, num)
        if pos < len(lis):
            lis[pos] = num
        else:
            lis.append(num)
    return len(lis)

print(lengthOfLis(A))
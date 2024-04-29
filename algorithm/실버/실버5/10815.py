N = int(input())
myl = list(map(int, input().split()))
M = int(input())
yourl = list(map(int, input().split()))

myl.sort()

def binarySearch(N, left, right):
    if left > right:
        return False

    mid = (left + right) // 2
    if N == myl[mid]:
        return True
    if N < myl[mid]:
        return binarySearch(N, left, mid - 1)
    elif N > myl[mid]:
        return binarySearch(N, mid + 1, right)

for l in yourl:
    if binarySearch(l, 0, len(myl) - 1):
        print('1', end=' ')
    else:
        print('0', end=' ')
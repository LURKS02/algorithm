N, M = map(int, input().split())
lectures = list(map(int, input().split()))

def countBlurays(lectures, size):
    count, sum = 0, 0
    for lecture in lectures:
        if sum + lecture > size:
            count += 1
            sum = 0
        sum += lecture
    return count + 1

def binarySearch(lectures):
    low, high = max(lectures), sum(lectures)

    while low < high:
        mid = (low + high) // 2
        if countBlurays(lectures, mid) <= M:
            high = mid
        else:
            low = mid + 1
    return low

print(binarySearch(lectures))


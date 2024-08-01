import sys
import bisect

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

data = []

for _ in range(N):
    key, value = map(int, input().rstrip().split())
    bisect.insort(data, [key, value])

for _ in range(M):
    inputs = list(map(int, input().rstrip().split()))
    if len(inputs) == 2:
        key = inputs[1]

        if len(data) == 0:
            print(-1)
            continue

        index = bisect.bisect_left(data, [key, -1])
        leftIndex = index - 1
        rightIndex = index

        # 맨 처음에 들어가는 경우
        if leftIndex == -1:
            rightKey = data[rightIndex][0]
            if rightKey - key > K:
                print(-1)
                continue
            else:
                print(data[rightIndex][1])
                continue

        # 맨 나중에 들어가는 경우
        elif rightIndex == len(data):
            leftKey = data[leftIndex][0]
            if key - leftKey > K:
                print(-1)
                continue
            else:
                print(data[leftIndex][1])
                continue

        else:
            leftKey = data[leftIndex][0]
            rightKey = data[rightIndex][0]

            if key - leftKey <= K and rightKey - key <= K and key - leftKey == rightKey - key:
                print("?")
                continue

            elif key - leftKey <= K and rightKey - key <= K and key - leftKey != rightKey - key:
                if key - leftKey < rightKey - key:
                    print(data[leftIndex][1])
                    continue
                else:
                    print(data[rightIndex][1])
                    continue

            elif key - leftKey > K and rightKey - key <= K:
                print(data[rightIndex][1])
                continue

            elif rightKey - key > K and key - leftKey <= K:
                print(data[leftIndex][1])
                continue

            else:
                print(-1)

    else:
        key = inputs[1]
        value = inputs[2]

        if inputs[0] == 1:
            bisect.insort(data, [key, value])
        else:
            index = bisect.bisect_left(data, [key, -1])
            leftIndex = index - 1
            rightIndex = index

            # 맨 처음에 들어가는 경우
            if leftIndex == -1:
                rightKey = data[rightIndex][0]
                if rightKey - key > K:
                    continue
                else:
                    data[rightIndex][1] = value
                    continue

            # 맨 나중에 들어가는 경우
            elif rightIndex == len(data):
                leftKey = data[leftIndex][0]
                if key - leftKey > K:
                    continue
                else:
                    data[leftIndex][1] = value
                    continue

            else:
                leftKey = data[leftIndex][0]
                rightKey = data[rightIndex][0]

                if key - leftKey <= K and rightKey - key <= K and key - leftKey == rightKey - key:
                    continue

                elif key - leftKey <= K and rightKey - key <= K and key - leftKey != rightKey - key:
                    if key - leftKey < rightKey - key:
                        data[leftIndex][1] = value
                        continue
                    else:
                        data[rightIndex][1] = value
                        continue

                elif key - leftKey > K and rightKey - key <= K:
                    data[rightIndex][1] = value
                    continue

                elif rightKey - key > K and key - leftKey <= K:
                    data[leftIndex][1] = value
                    continue

                else:
                    continue
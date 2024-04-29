from collections import deque

S = int(input())

def bfs(s):
    deq = deque([(1, 0, 0)])
    dp = [[-1 for _ in range(1001)] for _ in range(1001)]
    dp[1][0] = 0

    while deq:
        string, count, copy = deq.popleft()

        if string == s:
            return count

        # if dp[string][copy] == -1:
        #     dp[string][copy] = count

        if dp[string][string] == -1:
            dp[string][string] = count + 1
            deq.append((string, count + 1, string))

        # if string < S:
        if copy > 0 and string + copy <= 1000 and dp[string + copy][copy] == -1:
            dp[string + copy][copy] = count + 1
            deq.append((string + copy, count + 1, copy))
        # else:
        if string > 0 and dp[string - 1][copy] == -1:
            dp[string-1][copy] = count + 1
            deq.append((string - 1, count + 1, copy))

        # print(deq)

print(bfs(S))

maxNum = -float('inf')
answer = []

def solution(n, info):
    def cal(appeach, lion):
        appeachScore = 0
        lionScore = 0

        for i in range(11):
            if appeach[i] >= lion[i] and appeach[i] > 0:
                appeachScore += 10 - i
            elif lion[i] > appeach[i]:
                lionScore += 10 - i
        return lionScore - appeachScore

    def dfs(lion, idx):
        global maxNum
        global answer

        if idx == 11:
            if sum(lion) > n:
                return
            if sum(lion) < n:
                lion[-1] += (n - sum(lion))
            score = cal(info, lion)

            if score > 0:
                if maxNum < score:
                    maxNum = score
                    answer = [lion[:]]
                elif maxNum == score:
                    answer.append(lion[:])
            return

        lion.append(info[idx]+1)
        dfs(lion, idx + 1)
        lion.pop()

        lion.append(0)
        dfs(lion, idx + 1)
        lion.pop()

    dfs([], 0)
    if not answer: return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)
    # answer.sort()
    return answer[0]

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
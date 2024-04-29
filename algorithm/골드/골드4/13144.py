N = int(input())
l = list(map(int, input().split()))

start = 0
end = 0
answer = 0

visited = [False] * 100001

while start <= end and end < N:
    if not visited[l[end]]:
        visited[l[end]] = True
        end += 1
        answer += end - start

    else:
        while visited[l[end]]:
            visited[l[start]] = False
            start += 1

    # print(visited)
print(answer)
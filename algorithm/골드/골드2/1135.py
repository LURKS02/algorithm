N = int(input())
arr = list(map(int, input().split()))
tree = [[]for _ in range(N)]
for i in range(1,N):
    tree[arr[i]].append(i)
dp = [0]*(N)
# 여기까진 첫 코드와 동일

def treedp(x):
    if tree[x]:
        under_tree = sorted([treedp(i) for i in tree[x]], reverse=True) # 자식 노드의 비용을 내림차순으로 정렬
        dp[x] = max([i+1+under_tree[i] for i in range(0, len(tree[x]))]) # 정렬된 순서 + 비용 값 중 가장 큰 값이 부모 노드의 비용
    else:
        return dp[x] # 자식 노드가 없을 경우 현재 노드의 비용 반환
    return dp[x] # 모두 계산이 끝났을 경우 노드의 비용 반환

treedp(0) # 가장 꼭대기부터 출발
print(max(dp))
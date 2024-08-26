N, K = map(int, input().split())
a = list(map(int, input().split()))

minSN = float('inf')
minNS = float('inf')
ans = -float('inf')

energy = [0] + a
reversedEnergy = [0] + list(reversed(a))

# print(energy, reversedEnergy)

for i in range(1, N):
    minSN = min(minSN, energy[i] - K * i)
    minNS = min(minNS, reversedEnergy[i] - K * i)

    ans = max(ans, energy[i+1] - K * (i+1) - minSN, reversedEnergy[i+1] - K * (i+1) - minNS)

print(ans)
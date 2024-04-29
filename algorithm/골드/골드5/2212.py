N = int(input())
K = int(input())

sensors = list(map(int, input().split()))

sensors.sort()

distances = []

for i in range(1, N):
    distances.append(sensors[i] - sensors[i-1])

distances.sort(reverse=True)

print(sum(distances[K-1:]) if K < N else 0)
from collections import deque

def calculate_time_to_cross_bridge(n, w, L, trucks):
    time = 0
    bridge = deque([0] * w)  # 다리의 상태를 나타내는 큐
    bridge_weight = 0  # 다리 위의 현재 무게

    for truck in trucks:
        while True:
            if not bridge:  # 다리가 비어있는 경우
                bridge.append(truck)
                bridge_weight += truck
                time += 1
                break
            elif len(bridge) == w:  # 다리가 꽉 차 있는 경우
                bridge_weight -= bridge.popleft()
            else:
                # 새로운 트럭이 다리에 올라갈 수 있는 경우
                if bridge_weight + truck <= L:
                    bridge.append(truck)
                    bridge_weight += truck
                    time += 1
                    break
                # 다리에 올라갈 수 없는 경우, 다리를 하나 이동시킨다
                else:
                    bridge.append(0)
                    time += 1

    return time + w  # 마지막 트럭이 다리를 건너는 시간 포함

# 예제 입력
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 최단 시간 계산
min_time = calculate_time_to_cross_bridge(n, w, L, trucks)
print(min_time)
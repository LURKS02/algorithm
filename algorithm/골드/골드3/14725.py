import sys
input = sys.stdin.readline

N = int(input().rstrip())

cave = {}

def print_ant_cave(cave, depth = 0):
    keys = sorted(cave.keys())

    for key in keys:
        print('--' * depth + key)
        print_ant_cave(cave[key], depth + 1)

for _ in range(N):
    l = list(input().rstrip().split())
    K = int(l[0])
    path = l[1:]

    current_level = cave
    for food in path:
        if food not in current_level:
            current_level[food] = {}
        current_level = current_level[food]

print_ant_cave(cave)
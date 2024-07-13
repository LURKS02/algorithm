from bisect import bisect_left

N = int(input())
ports = list(map(int, input().split()))
link = []
for port in ports:
    if not link or link[-1] < port:
        link.append(port)
    else:
        link[bisect_left(link, port)] = port

print(len(link))
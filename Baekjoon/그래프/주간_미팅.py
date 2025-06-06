# N, V, E = map(int, input().split())
# A, B = map(int, int().split())
# H = [int(input()) for _ in range(N)]
# for _ in range(E):
    # a, b, l = 

import sys
input = sys.stdin.readline
import heapq

n, v, e = map(int, input().split())
a, b = map(int, input().split())
house = list(map(int, input().split()))
arr = [[] for i in range(v + 1)]

distance_a = [int(1e9)] * (v + 1)
distance_b = [int(1e9)] * (v + 1)

for _ in range(e):
    x, y, l = map(int, input().split())
    arr[x].append((y, l))
    arr[y].append((x, l))

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(a, distance_a)
dijkstra(b, distance_b)

result = 0
for i in house:
    if distance_a[i] == int(1e9):
        distance_a[i] = -1
    if distance_b[i] == int(1e9):
        distance_b[i] = -1

    result += distance_a[i] + distance_b[i]

print(result)
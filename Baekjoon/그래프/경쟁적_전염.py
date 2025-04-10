# 1. 낮은 번호의 바이러스가 높은 번호의 바이러스보다 먼저 전염
# 2. 각 초가 지날 때마다 현재 존재하는 바이러스들이 인접한 빈 칸에 퍼짐
# 3. 바이러스가 전염될 때 BFS를 이용하고 낮은 번호의 바이러스부터 퍼지도록 최소힙 사용

import heapq

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] != 0:
            heapq.heappush(virus, (0, row[j], i, j))  
            # (시간, 바이러스 번호, x좌표, y좌표)

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while virus:
    time, vnum, vx, vy = heapq.heappop(virus)

    if time == s:
        break

    for d in range(4):
        nx = vx + dx[d]
        ny = vy + dy[d]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = vnum
            heapq.heappush(virus, (time + 1, vnum, nx, ny))

print(graph[x - 1][y - 1])

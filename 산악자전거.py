import sys; input = sys.stdin.readline
import heapq
from math import inf

V, R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2차원 다익스트라
# 각 칸마다 제일 빠르게 도착하는 시간을 저장하면서 진행
distance = [[inf] * C for _ in range(R)]
queue = [[0, 0, 0, V]] # 거리, r, c, 속도
distance[0][0] = 0

while queue:
    d, r, c, v = heapq.heappop(queue)
    if distance[r][c] < d:
        continue
    
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]

        if (0 <= x < R) and (0 <= y < C) and (distance[x][y] > distance[r][c] + 1 / v):
            distance[x][y] = distance[r][c] + 1 / v
            heapq.heappush(queue, [distance[x][y], x, y, v * 2 ** (graph[r][c] - graph[x][y])])

print(f"{distance[R - 1][C - 1]:.2f}")
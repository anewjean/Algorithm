from collections import deque

N, M = map(int, input().split())
vilage = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_points):
    dist = [[-1] * M for _ in range(N)]
    q = deque()
    for x, y in start_points:
        dist[x][y] = 0
        q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

start = end = None
fishes = []
for i in range(N):
    for j in range(M):
        if vilage[i][j] == 'S':
            start = (i, j)
        elif vilage[i][j] == 'H':
            end = (i, j)
        elif vilage[i][j] == 'F':
            fishes.append((i, j))

dist_s = bfs([start])
dist_h = bfs([end])

answer = float('inf')
for fx, fy in fishes:
    if dist_s[fx][fy] != -1 and dist_h[fx][fy] != -1:
        answer = min(answer, dist_s[fx][fy] + dist_h[fx][fy])

print(answer if answer != float('inf') else -1)



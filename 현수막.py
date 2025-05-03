from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0  # 방문 처리

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < M) and (0 <= ny < N) and (graph[nx][ny] == 1):
                graph[nx][ny] = 0  # 방문 처리
                q.append((nx, ny))

count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            count += 1

print(count)
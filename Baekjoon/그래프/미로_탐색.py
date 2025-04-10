from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if not ((0 <= nx < N) and (0 <= ny < M)):
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[a][b] + 1

dfs(0, 0)

print(graph[N-1][M-1])
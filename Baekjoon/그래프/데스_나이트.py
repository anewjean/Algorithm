from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

graph = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        if (x, y) == (r2, c2):
            return graph[x][y]

        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1 # 방문 횟수 추가
                q.append((nx, ny))

    return -1

print(bfs(r1, c1))

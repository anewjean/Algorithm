# 단지를 세는 기준: q가 빌 때마다 + 1
# q 가 비더라도 (n-1, n-1)까지 가는 방법은? => 무조건 큐에 넣기

from collections import deque

N = int(input())
graph = [list(map(int, (list(input())))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def bfs(x: int, y: int, town_count: int) -> None:
    q = deque()
    q.append((x, y))
    visited[x][y] = town_count
    house_count = 1

    while q:
        cx, cy = q.popleft()

        for dir_idx in range(4):
            nx = cx + dx[dir_idx]
            ny = cy + dy[dir_idx]

            if (0 <= nx < N) and (0 <= ny < N):
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = town_count
                    house_count += 1
                    q.append((nx, ny))

    return house_count

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

town = []
count = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count += 1
            houses = bfs(i, j, count)
            town.append(houses)

print(count)
for val in sorted(town):
    print(val)
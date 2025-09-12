from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())  # m=행, n=열
grid = [list(map(int, input().strip())) for _ in range(m)]

dxy = [(1,0),(-1,0),(0,1),(0,-1)]
inside = lambda y,x: 0 <= y < m and 0 <= x < n

def bfs(y, x):
    visited[y][x] = True
    q = deque([(y, x)])
    while q:
        cy, cx = q.popleft()
        for dy, dx in dxy:
            ny, nx = cy+dy, cx+dx
            if inside(ny, nx) and not visited[ny][nx] and grid[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

def count_clusters():
    cnt = 0
    for y in range(m):
        for x in range(n):
            if grid[y][x] and not visited[y][x]:
                bfs(y, x)
                cnt += 1
    return cnt

def spread():
    next_grid = [[0] * n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            speed = grid[y][x]
            if speed:
                for ny in range(y-speed, y+speed+1):
                    for nx in range(x-speed, x+speed+1):
                        if inside(ny, nx):
                            next_grid[ny][nx] = max(next_grid[ny][nx], speed) # 속도가 더 빠른 곰팡이가 현재 칸 차지
    return next_grid

day = 0
visited = [[False] * n for _ in range(m)]
clusters = count_clusters()
while clusters > 1:
    day += 1
    grid = spread()
    visited = [[False] * n for _ in range(m)] # visited 초기화
    clusters = count_clusters()

print(day)

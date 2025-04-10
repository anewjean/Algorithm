# 1. 아직 방문하지 않은 타일을 만나면 그 위치부터 DFS 탐색 시작
# 2. -는 오른쪽으로 이동, |는 아래로 이동하며 체크
# 3. DFS가 한 번 끝날 때마다 타일 하나씩 카운트
# 4. 모든 타일 탐색 후 총 타일 개수 출력

import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True

    # - 만나면 오른쪽으로 
    if floor[x][y] == '-':
        ny = y + 1
        if ny < m and floor[x][ny] == '-' and not visited[x][ny]:
            dfs(x, ny)

    # | 만나면 아래쪽으로
    if floor[x][y] == '|':
        nx = x + 1
        if nx < n and floor[nx][y] == '|' and not visited[nx][y]:
            dfs(nx, y)

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            count += 1 # dfs 한 번 호출될 때마다 하나의 판자를 발견한 것

print(count)
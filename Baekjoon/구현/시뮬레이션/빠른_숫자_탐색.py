from collections import deque
import sys 

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
sr, sc = map(int, sys.stdin.readline().split()) 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r: int, c: int) -> int:
    visited = [[False] * 5 for _ in range(5)]
    q = deque([(r, c, 0)]) 
    visited[r][c] = True

    while q:
        x, y, dist = q.popleft()

        if board[x][y] == 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:  
                if not visited[nx][ny] and board[nx][ny] != -1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

    return -1

print(bfs(sr, sc))
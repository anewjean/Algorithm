from collections import deque

board = [list(map(int, input().split())) for_ in range(19)]

# 상, 하, 좌, 우, 대각선들
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(cx, cy, color):
    count = 0
    q = deque()
    q.append((cx, cy))
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < 19) and (0 <= ny < 19) and board[nx][ny] == color:
                count += 1
            
            if count != 5:
                continue

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            winbfs(i, j, board[i][j])

winner, x, y = find_winner()

if winner:
    print(winner)
    print(x, y)
else:
    print(0)


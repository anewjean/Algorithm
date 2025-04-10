from collections import deque

# N = int(input())
# K = int(input())

# board = [[0] * N for _ in range(N)]
# for _ in range(K):
#     x, y = map(int, input().split())
#     board[x-1][y-1] = 1

# directions = {}
# L = int(input())
# for _ in range(L):
#     t, d = input().split()
#     directions[int(t)] = d

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# dir_idx = 0
# x, y = 0, 0 # 시작 좌표

# snake = deque()
# snake.append((0, 0))
# time = 0
# while True:
#     time += 1
#     nx = x + dx[dir_idx]
#     ny = y + dy[dir_idx]

#     # 벽에 부딪히면 게임 종료
#     if not ((0 <= nx < N) and (0 <= ny < N)): 
#         break
#     # 자신의 몸에 부딪히면 게임 종료
#     if (nx, ny) in snake:
#         break

#     # 이동
#     if board[nx][ny] == 1:
#         board[nx][ny] = 0
#         snake.append((nx, ny))
    
#     else:
#         snake.append((nx, ny))
#         snake.popleft()

#     # 방향 전환 확인
#     if time in directions:
#         if directions[time] == 'D':
#             dir_idx = (dir_idx + 1) % 4
#         else:
#             dir_idx = (dir_idx - 1) % 4

#     x, y = nx, ny

# print(time)







N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
 
L = int(input())
directions = {int(t): d for _ in range(L) for t, d in [input().split()]}

time = 0
x, y = 0, 0
snake = deque()
snake.append((x, y))

dir_idx = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    time += 1
    nx = x + dx[dir_idx]
    ny = y + dx[dir_idx]
    
    # 벽이랑 부딪히면 게임 종료
    if not ((0 <= nx < N) and (0 <= ny < N)):
        break

    # 자기 자신과 부딪히면 게임 종료
    if (nx, ny) in snake:
        break

    # 이동
    if board[nx][ny] == 1:
        board[nx][ny] = 0
        snake.append((nx, ny))
    else:
        snake.append((nx, ny))
        snake.popleft()
    
    # 방향 전환
    if time in directions:
        if directions[time] == 'D':
            dir_idx = (dir_idx + 1) % 4 # 오른쪽으로 회전
        else:
            dir_idx = (dir_idx - 1) % 4 # 왼쪽으로 회전 

    x, y = nx, ny

print(time)
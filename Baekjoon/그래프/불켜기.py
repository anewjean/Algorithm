import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def bfs():
    visited[1][1] = True
    light_on[1][1] = True
    q = deque([(1, 1)])
    while q:  
        si, sj = q.popleft()
        # 불 켤 수 있는 곳 켜주기
        for ni, nj in turn_on[(si, sj)]:
            if not light_on[ni][nj]:
                light_on[ni][nj] = True
                # 새로 불 켠 곳 4방향 중 방문한 적이 있다면 재탐색 대상  
                for d in range(4):
                    li, lj = ni+di[d], nj+ dj[d]
                    if visited[li][lj]:
                        q.append((li, lj))

        # 불을 켠 방 기준으로 4방향에 불 켜진 곳이 있는데 방문한 적이 없다면 재탐색 대상  
        for d in range(4):
            li, lj = si + di[d], sj + dj[d]
            if not visited[li][lj] and light_on[li][lj]:
                q.append((li, lj))
                visited[li][lj] = True

N, M = map(int, input().split())
turn_on = defaultdict(list)
visited = [[False] * (N*2) for _ in range(N*2)]
light_on = [[False] * (N*2) for _ in range(N*2)]
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(M):
    x, y, a, b = map(int, input().split())
    turn_on[(x, y)].append((a, b))

bfs()
result = 0
for i in light_on:
    result += i.count(True)

print(result)
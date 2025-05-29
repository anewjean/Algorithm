import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[row][col][dir] : dir 방향으로 (↙:0, ↓:1, ↘:2) 왔을 때 최소 비용
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

# 첫 줄 초기화: 첫 줄은 이전 방향이 없으므로 그냥 직접 설정
for j in range(M):
    for d in range(3):
        dp[0][j][d] = graph[0][j]

# 다음 줄부터 계산
for i in range(1, N):
    for j in range(M):
        for d in range(3):  # 현재 도착 방향
            for prev_d in range(3):  # 이전에서 온 방향
                if d == prev_d:
                    continue  # 같은 방향 연속 x
                nj = j + [-1, 0, 1][d]  # 현재 방향에 따른 이전 열 위치
                if 0 <= nj < M:
                    dp[i][j][d] = min(dp[i][j][d], dp[i-1][nj][prev_d] + graph[i][j])

# 마지막 행에서의 최소값
result = float('inf')
for j in range(M):
    for d in range(3):
        result = min(result, dp[N-1][j][d])

print(result)
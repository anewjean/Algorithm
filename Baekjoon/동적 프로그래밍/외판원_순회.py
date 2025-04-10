import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')

# dp[city][visited] = 비용
dp = [[INF] * (1 << N) for _ in range(N)]
dp[0][1] = 0  # 시작 도시 0번, 0번만 방문한 상태

for visited in range(1 << N):
    for cur in range(N):
        if not (visited & (1 << cur)):  # 현재 상태에 cur 도시가 포함되지 않았으면 무시
            continue
        for nxt in range(N):
            if visited & (1 << nxt):  # 이미 방문한 도시면 스킵
                continue
            if W[cur][nxt] == 0:  # 경로 없으면 스킵
                continue
            next_visited = visited | (1 << nxt)
            dp[nxt][next_visited] = min(dp[nxt][next_visited], dp[cur][visited] + W[cur][nxt])

# 모든 도시 방문 후 시작점(0)으로 돌아가는 최소 비용 계산
answer = INF
for i in range(1, N):
    if W[i][0] == 0:
        continue
    answer = min(answer, dp[i][(1 << N) - 1] + W[i][0])

print(answer)

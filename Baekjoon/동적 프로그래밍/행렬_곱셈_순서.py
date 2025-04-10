N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for times in range(2, N+1):
    for i in range(N - times + 1):
        j  = times + i - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1] # 점화식
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][N-1])
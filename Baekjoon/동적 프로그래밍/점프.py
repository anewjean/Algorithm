n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if maps[i][j] == 0 or dp[i][j] == 0:
            continue

        walk = maps[i][j]

        if walk +j < n:
            dp[i][j + walk] = dp[i][j+walk] + dp[i][j]

        if walk +i < n:
            dp[i+ walk][j] = dp[i+walk][j] + dp[i][j]
print(dp[n-1][n-1])
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    coins = list(map(int, input().split()))
    M = int(input().strip())

    # dp = [0] * (M + 1)
    # dp[0] = 1

    # for coin in coins:
    #     for j in range(coin, M + 1):
    #         dp[j] += dp[j - coin]

    # print(dp[M])

    coins.insert(0, 0)
    dp = [[0] * (M + 1) for i in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(1, N + 1):
        for j in range(1, M + 1):
            dp[j][j] = dp[j-1][i]
            if i - coins[j] >= 0:
                dp[j][i] += dp[j][i-coins[j]]
print(dp[N][M])
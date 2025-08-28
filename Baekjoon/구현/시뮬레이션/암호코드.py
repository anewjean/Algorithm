from sys import stdin

input = stdin.readline
password = list(map(int, input().split()))
n = len(password)

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

if password == 0:
    print(0)
else:
    for i in range(1, n):
        k = i + 1
        if password[i] > 0:
            dp[k] += dp[k-1]
        if 10 <= password[i] + password[i-1] * 10 <= 26:
            dp[k] += dp[k-2]
    print(dp[n] % 1000000)

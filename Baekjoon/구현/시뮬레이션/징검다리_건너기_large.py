import sys
input = sys.stdin.readline

N = int(input().strip())
stones = list(map(int, input().strip().split()))

INF = float('inf')
dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    curr = stones[i]
    best = INF
    for j in range(i):
        dist = abs(curr - stones[j])
        cost = (i - j) * (1 + dist)
        best = min(best, max(dp[j], cost))
    dp[i] = best

print(dp[-1])
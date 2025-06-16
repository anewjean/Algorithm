n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(n):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
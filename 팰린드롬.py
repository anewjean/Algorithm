import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for _ in range(N)]

# 길이 1: 무조건 palindrome
for i in range(N):
    dp[i][i] = 1

# 길이 2: 시작과 끝이 같으면 palindrome
for i in range(N - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i+1] = 1

# 길이 3 이상: 시작과 끝이 같고, dp
for length in range(3, N + 1):
    for start in range(N-length + 1):
        end = start + length - 1
        if nums[start] == nums[end] and dp[start + 1][end-1]:
            dp[start][end] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])

def solution(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in i:
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i]  = dp[j] + 1

    return max(dp)
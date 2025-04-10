# def knapsack_2d(weights, values, max_weight):
#     n = len(weights)
#     dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for w in range(max_weight + 1):
#             if weights[i - 1] > w:
#                 dp[i][w] = dp[i - 1][w]
#             else:
#                 dp[i][w] = max(dp[i - 1][w],
#                                dp[i - 1][w - weights[i - 1]] + values[i - 1])
#     return dp[n][max_weight]


def knapsack_2d(weights: list, values: list, max_weight: int):
    n = len(weights)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_weight + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][max_weight]
    


N, K = map(int, input().split())

weights = []
values = []

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

print(knapsack_2d(weights, values, K))















































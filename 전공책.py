from itertools import combinations

def calc_min_cost():
    min_cost = float('inf')

    for r in range(1, len(prices) + 1):
        for case in combinations(prices.keys(), r):
            combined = ''.join(case)
            if all(combined.count(char) >= T.count(char) for char in T):
                total_cost = sum(prices[title] for title in case)
                min_cost = min(min_cost, total_cost)

    print(-1 if min_cost == float('inf') else min_cost)

T = input()
N = int(input())
prices = dict()
for _ in range(N):
    C, W = input().split()
    prices[W] = int(C)

calc_min_cost()


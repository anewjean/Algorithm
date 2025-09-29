import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]

best_a, best_b = -1, -1
min_rss = float("inf")

for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for x, y in data:
            diff = y - (a * x + b)
            rss += diff * diff
        if rss < min_rss:
            min_rss = rss
            best_a, best_b = a, b

print(best_a, best_b)

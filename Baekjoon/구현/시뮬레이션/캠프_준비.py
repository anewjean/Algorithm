# from itertools import combinations

# N, L, R, X = map(int, input().split())
# difficulties = [int(input()) for _ in range(N)]

# 조합했을 때 조건에 만족하는 경우의 수 세기

import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
levels = list(map(int, input().split()))

ans = 0
# 1 << N 까지의 모든 부분집합
for mask in range(1, 1 << N):
    chosen = []
    total = 0
    for i in range(N):
        if mask & (1 << i):
            chosen.append(levels[i])
            total += levels[i]
    if len(chosen) < 2:
        continue
    mn, mx = min(chosen), max(chosen)
    if L <= total <= R and (mx - mn) >= X:
        ans += 1

print(ans)
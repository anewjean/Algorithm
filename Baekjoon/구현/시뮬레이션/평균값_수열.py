# 가능한 s1 개수 찾기
import sys
input = sys.stdin.readline

n = int(input().strip())
m = [int(input().strip()) for _ in range(n)]

upper = m[0]              # 상한 초기값
lower = 2*m[0] - m[1]     # 하한 초기값
accum = lower             # 누적

for idx in range(2, n):
    avg_diff = m[idx-1] - m[idx]
    if (idx + 1) % 2 == 1:   # 홀수(0-based 이므로 idx+1) → 상한 갱신
        accum -= avg_diff
        upper = min(upper, accum)
    else:                   # 짝수 → 하한 갱신
        accum += avg_diff
        lower = max(lower, accum)

print(max(0, upper - lower + 1))
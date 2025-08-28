import sys
input = sys.stdin.readline

N = int(input().strip())
scores = list(int(input().strip()) for _ in range(N))[::-1] # 순서 거꾸로

ans = 0
before = scores[0]

for idx in range(1, N):
    if scores[idx] >= before:
        curr = before - 1
        ans += (scores[idx] - curr)
        before = curr
    else:
        before = scores[idx]
print(ans) 
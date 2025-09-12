std = dict()

n, m = map(int, input().split())
cnt = 0
for _ in range(n):
    a, b = input().split()
    std[a] = float(b) * 1.05
for _ in range(m):
    c, d = input().split()
    if std[c] < float(d):
        cnt += 1

print(cnt)
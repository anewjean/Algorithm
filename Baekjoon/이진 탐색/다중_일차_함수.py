import sys
from bisect import bisect_right

input = sys.stdin.readline

n = int(input().strip())
xs, ys = [], []
for _ in range(n):
    x, y = map(float, input().split())
    xs.append(x)
    ys.append(y)

slopes = []
for i in range(n - 1):
    slope = ys[i + 1] - ys[i] # x는 무조건 증가하므로 부호는 dy만으로 판단 가능
    if slope > 0:
        slopes.append(1)
    elif slope < 0:
        slopes.append(-1)
    else:
        slopes.append(0)
        
q = int(input().strip())
for _ in range(q):
    k = float(input().strip())
    i = bisect_right(xs, k) - 1
    print(slopes[i])
import sys
import bisect

N = int(sys.stdin.readline())
ns = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))

answer = []
for m in ms:
    if bisect.bisect_left(ns, m) != bisect.bisect_right(ns, m):
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
import heapq
import sys

N = int(sys.stdin.readline())
arr = []
result = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(arr, -num)
    elif num == 0:
        if arr:
            result.append(-heapq.heappop(arr))
        else:
            result.append(0)

print("\n".join(map(str, result)))
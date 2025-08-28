# import sys
# from bisect import bisect_left
# input = sys.stdin.readline

# N, M = map(int, input().strip().split())
# A = list(int(input().strip()) for _ in range(N))
# B = sorted(A)

# answer = []
# for i in range(M):
#     d = int(input().rstrip())
#     i = bisect_left(B, d)
#     answer.append(str(i if i < N and B[i] == d else -1))

# print("\n".join(answer))

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = list(int(input().strip()) for _ in range(N))
B = sorted(A)

pos = {}
for idx, val in enumerate(B):
    if val not in pos:
        pos[val] = idx

answer = []
for _ in range(M):
    d = int(input().rstrip())
    answer.append(str(pos.get(d, -1)))

print("\n".join(answer))
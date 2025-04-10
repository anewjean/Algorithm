from collections import Counter

N = int(input())
tree = []
# coordinates = []
# stack = []
# area = 1

# 배열로 트리 구현
for _ in range(N):
    x, r = map(int, input().split())
    left = x - r
    right = x + r
    tree.append((left, r))
    tree.append((right, r))


# arr.sort(key=lambda x: (x[0], x[1]))

# for idx, tup in enumerate(arr):
#     if tup[1] == "L":
#         stack.append(tup)
#     else:
#         if left[0] == tup[0]:
#             area += 1
#         # if arr[idx-1][0] == tup[0] and arr[idx-1][1] == "L":
#         #     area += 1
#         area += 1

# print(area)


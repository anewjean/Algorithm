import bisect

N = int(input())
ns = sorted(map(int, input().split()))
M = int(input())
ms = map(int, input().split())

for val in ms:
    left_idx = bisect.bisect_left(ns, val)
    if left_idx < N and ns[left_idx] == val:
        right_idx = bisect.bisect(ns, val) 
        print(right_idx - left_idx, end = " ")
    else:
        print(0, end = " ")
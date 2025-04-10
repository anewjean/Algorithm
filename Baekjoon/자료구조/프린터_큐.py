import heapq
from collections import deque
from collections import Counter

def find_print_order(idx: int, weighted_vals: deque) -> int:
    count = 0
    while True:
        # max 가중치가 0번째 인덱스에 위치하지 않은 경우
        if weighted_vals[0] < max(weighted_vals):
            if idx == 0:
                idx = len(weighted_vals) -1
            else:
                idx -= 1
            weighted_vals.rotate(-1)

        # max 가중치가 0번째 인덱스에 위치한 경우
        else: 
            weighted_vals.popleft()
            count += 1
            if idx == 0:
                return count
            else:
                idx -= 1

N = int(input())

for _ in range(N):
    n, idx = map(int, input().split())
    weighted_vals = deque(map(int, input().split()))
    print(find_print_order(idx, weighted_vals))
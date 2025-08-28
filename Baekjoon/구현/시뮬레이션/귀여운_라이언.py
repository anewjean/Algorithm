import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
ryan_count = 0
min_length = float('inf')

for right in range(N):
    if dolls[right] == 1:
        ryan_count += 1
    
    while ryan_count >= K:
        min_length = min(min_length, right - left + 1)
        if dolls[left] == 1:
            ryan_count -= 1
        left += 1

print(min_length if min_length != float('inf') else -1)
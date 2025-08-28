from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
dnas = [input().strip() for _ in range(N)]

ans = []
hamming_dist = 0 

for col in zip(*dnas):
    cnt = Counter(col)
    max_cnt = max(cnt[chr] for chr in 'ACGT')
    ans.append(next(chr for chr in 'ACGT' if cnt[chr] == max_cnt))
    hamming_dist += N - max_cnt

print("".join(ans))
print(hamming_dist)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

yns = []
for _ in range(N):
    _, yn = input().split()
    yn = yn.replace('Y', '1').replace('N', '0')
    yns.append(int(yn, 2))

song_available_cnt = -1
available_guitar_cnt = N+1

for mask in range(1, 1 << N):
    union_mask = 0
    guitar_cnt = 0

    for idx in range(N):
        if mask & (1 << idx):
            # union_mask |= yns[idx]
            guitar_cnt += 1

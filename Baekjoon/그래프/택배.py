import sys
input = sys.stdin.readline

INF = float('inf')

N, M = map(int, input().split())
dist = [[INF]*(N+1) for _ in range(N+1)]
nxt  = [[0]*(N+1)   for _ in range(N+1)]

for i in range(1, N+1):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:           # 다중 간선 대비
        dist[a][b] = dist[b][a] = c
        nxt[a][b] = b
        nxt[b][a] = a

# 플로이드 워셜
for k in range(1, N+1):
    dk = dist[k]
    for i in range(1, N+1):
        di = dist[i]
        dik = di[k]
        if dik == INF: 
            continue
        for j in range(1, N+1):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd
                nxt[i][j] = nxt[i][k]   # 첫 경유지는 i->k로 가는 첫 hop

# 출력
out_lines = []
for i in range(1, N+1):
    row = []
    for j in range(1, N+1):
        if i == j:
            row.append('-')
        else:
            row.append(str(nxt[i][j]))
    out_lines.append(' '.join(row))
print('\n'.join(out_lines))
import sys
import heapq

input = sys.stdin.readline
N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)] # adj: 양방향 그래프
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

followers = list(map(int, input().split()))
INF = float('inf')

# 1) 출발점 1에서 단일 출발 다익스트라
dist1 = [INF] * (N+1)
dist1[1] = 0
hq = [(0, 1)]
while hq:
    d, u = heapq.heappop(hq)
    if d > dist1[u]:
        continue
    for v, w in adj[u]:
        nd = d + w
        if nd < dist1[v]:
            dist1[v] = nd
            heapq.heappush(hq, (nd, v))

# 2) 멀티소스 다익스트라: 추종자들
dist2 = [INF] * (N+1)

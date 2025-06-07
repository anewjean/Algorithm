import sys

def dfs(pos, cnt, cost):
    if cnt == N:
        return cost

    min_cost = int(1e9)
    for next in range(N):
        if not visit[next]:
            visit[next] = True
            new_cost = dfs(next, cnt + 1, cost + graph[pos][next])
            min_cost = min(new_cost, min_cost)
            visit[next] = False # 백트래킹

    return min_cost

N, K = map(int, sys.stdin.readline().split())
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]

# 플로이드 워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visit = [False] * N
visit[K] = True

print(dfs(K, 1, 0))
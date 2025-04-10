import heapq

n = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

q = []
heapq.heappush(q, (0, 0))
INF = float('inf')
costs = [[INF] * n for _ in range(n)]
costs[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = heapq.heappop(q)
    
    for dir_idx in range(4):
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        if 0 <= nx < n and 0 <= ny < n:
            cost = 1 if graph[x][y] == 0 else 0
            if costs[nx][ny] > costs[x][y] + cost:
                costs[nx][ny] = costs[x][y] + cost
                heapq.heappush(q, (nx, ny)) 

print(costs[n-1][n-1])
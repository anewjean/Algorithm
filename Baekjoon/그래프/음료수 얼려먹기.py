n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m or graph[x][y] == 1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
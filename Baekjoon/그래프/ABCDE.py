# import sys
# sys.setrecursionlimit(10000)

n, m = map(int, input().split())
relations = [[] for _ in range(n)]
visited = [False] * n
is_fifth = False

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

def dfs(friend, depth):
    global is_fifth
    if depth == 5:
        is_fifth = True
        return
    visited[friend] = True
    for neighbor in relations[friend]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
    visited[friend] = False

for i in range(n):
    dfs(i, 1)
    if is_fifth:
        break

print(1 if is_fifth else 0)

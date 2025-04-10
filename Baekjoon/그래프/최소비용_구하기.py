import heapq
# 다익스트라
# 그리디로 연결된 모든 정점 확인해서 항상 최소 비용 갱신
# 처음 시작점은 비용 0, 나머지는 무한으로 설정
# 정점에서 연결된 모든 정점들의 비용을 확인
# heapq 사용!

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

def dijkstra(s: int):
    inf = float('inf')
    costs = [inf] * (N + 1) # 최소 비용
    prev = [-1] * (N + 1) # 경로 추적용 이전 노드

    costs[s] = 0
    q = []
    heapq.heappush(q, (0, s)) # 누적 비용, 현재 노드

    while q:
        curr_cost, curr = heapq.heappop(q)

        # 이미 더 짧은 경로로 방문한 적 있으면 무시
        if curr_cost > costs[curr]:
            continue

        # 현재 노드에서 갈 수 있는 모든 간선 탐색
        for neighbor_cost, neighbor in graph[curr]:
            # 더 짧은 경로 발견 시 거리 갱신(RELAX)
            if costs[neighbor] > curr_cost + neighbor_cost:
                costs[neighbor] = curr_cost + neighbor_cost
                heapq.heappush(q, (costs[neighbor], neighbor))
                prev[neighbor] = curr

    return costs, prev

def get_path(prev, end):
    path = []
    while end != -1:
        path.append(end)
        end = prev[end]
    return path[::-1]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

start, end = map(int, input().split())
result, prev = dijkstra(start)
print(result[end])

path = get_path(prev, end)
print(" ".join(map(str, path)))

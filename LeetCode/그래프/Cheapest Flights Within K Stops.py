import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # (가격, 노드, 남은 이동 횟수)
        q = [(0, src, k + 1)]
        # dist[node][남은이동] = 최소 비용
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][k+1] = 0

        while q:
            price, node, stops = heapq.heappop(q)

            if node == dst:
                return price

            if stops > 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < dist[v][stops-1]:
                        dist[v][stops-1] = alt
                        heapq.heappush(q, (alt, v, stops-1))

        return -1

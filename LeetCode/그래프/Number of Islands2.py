class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        # 육지인 모든 노드 parent 초기화
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    parent[(i, j)] = (i, j)
        
        # 인접한 육지끼리 union
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for dx, dy in directions:
                        nx, ny = i+dx, j+dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            union((i,j), (nx,ny))
        
        # root가 자기 자신인 개수(섬의 개수) find
        roots = { find(node) for node in parent }
        return len(roots)

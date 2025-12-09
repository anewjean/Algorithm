class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 중복 제거하면서 인덱스 매핑
        unique = list(set(nums))
        n = len(unique)

        union_find = UnionFind(n)
        index = {num: i for i, num in enumerate(unique)}

        for num in unique:
            i = index[num]
            if num - 1 in index:
                union_find.union(i, index[num - 1])
            if num + 1 in index:
                union_find.union(i, index[num + 1])

        return max(union_find.size)

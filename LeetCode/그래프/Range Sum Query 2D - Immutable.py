class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # prefix 배열 -> 1-based index
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.prefix[r][c] = (
                    matrix[r-1][c-1]
                    + self.prefix[r-1][c]
                    + self.prefix[r][c-1]
                    - self.prefix[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 쿼리 영역 -> 1-based index
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1
        
        return (
            self.prefix[r2][c2]
            - self.prefix[r1 - 1][c2]
            - self.prefix[r2][c1 - 1]
            + self.prefix[r1 - 1][c1 - 1]
        )

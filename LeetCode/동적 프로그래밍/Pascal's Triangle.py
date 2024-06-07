# https://leetcode.com/problems/pascals-triangle/description/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            row = [1 for _ in range(row_num + 1)]  # 현재 행의 모든 요소를 1로 초기화
            
            # 현재 행의 가운데 숫자 계산
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j] # 이전 행의 j-1번째 요소와 j번째 요소를 더함
            
            triangle.append(row)
        
        return triangle
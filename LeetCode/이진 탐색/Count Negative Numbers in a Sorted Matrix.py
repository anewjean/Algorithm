# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid) # 행의 개수
        n = len(grid[0]) # 첫 번째 행에 대한 열의 개수 (= 모든 행에 대한 열의 개수)
        answer = 0
        row = m - 1 # 행의 인덱스를 맨 마지막으로 초기화
        col = 0 # 열의 인덱스를 맨 첫 번째로 초기화
        
        while col < n and row >= 0: 
            if grid[row][col] < 0: # 현재 행에 대한 현재 열의 위치가 음수라면
                answer += (m - col) # 정답에 '전체 열의 갯수에서 현재 열의 인덱스를 빼준 만큼' 더함
                row -= 1 # 행을 한 칸 위로 이동
            else: # 음수가 나올 때까지 한 칸 오른쪽으로 이동
                col += 1  
        
        return answer
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr, opened_cnt, closed_cnt):
            # 완성된 경우
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # 여는 괄호 추가 가능한 경우
            if opened_cnt < n:
                backtrack(curr + "(", opened_cnt + 1, closed_cnt)
            
            # 닫는 괄호 추가 가능한 경우
            if closed_cnt < opened_cnt:
                backtrack(curr + ")", opened_cnt, closed_cnt + 1)
            
        backtrack("", 0, 0)
        return result
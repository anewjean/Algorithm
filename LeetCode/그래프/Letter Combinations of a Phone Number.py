class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(idx, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in digits_2_letters[digits[i]]:
                    dfs(i + 1, path + j) 
                    
        # 예외 처리
        if not digits:
            return []
        
        digits_2_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        dfs(0, "")

        return result
class Solution:
    def restoreString(self, s: str, indicies: List[int]) -> str:
        
        # 정렬된 결과를 반환할 리스트
        sorted_strings = [""] * len(s)

        # 올바른 idx에 letter를 저장
        for idx, letter in zip(indicies, s):
            sorted_strings[idx] = letter

        # sorted_strings를 구성하는 요소들을 합친 문자열을 반환
        return "".join(sorted_strings)


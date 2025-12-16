class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1          # 현재 수열의 첫 번째 값
        step = 1          # 인접한 두 수 사이 간격
        remaining = n     # 남아 있는 숫자 개수
        dir_to_right = True  # 현재 방향: 왼→오

        while remaining > 1:
            # 왼 -> 오로 제거 시 무조건 첫 번째 숫자가 사라짐
            # 오 -> 왼으로 제거 시 남은 개수가 홀수면 첫 번째 숫자가 사라짐
            if dir or remaining % 2 == 1:
                head += step

            # 매 제거 시마다
            remaining //= 2   # 절반만 살아남음
            step *= 2         # 인접 간격은 두 배
            dir_to_right = not dir_to_right  # 방향 반전

        return head

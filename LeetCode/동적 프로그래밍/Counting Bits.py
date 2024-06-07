# https://leetcode.com/problems/counting-bits/description/
def count_bits(self, n: int):
    answer = []
    for i in range(n + 1):
        answer.append(bin(i).count('1'))

    return answer
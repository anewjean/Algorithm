# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)  # numbers를 구성하는 문자열 하나하나를 저장하는 리스트
    all_permutations = set()  # 중복을 피하기 위해 set 사용
    answer = 0  # answer 초기화

    for i in range(1, len(nums) + 1):
        for perm in permutations(nums, i):
            all_permutations.add(int(''.join(perm)))

    for num in all_permutations:
        if is_prime(num):
            answer += 1

    return answer
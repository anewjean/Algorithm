# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    sorted_sizes = [sorted(size) for size in sizes]
    max_w = max([size[0] for size in sorted_sizes])
    max_h = max([size[1] for size in sorted_sizes])
    return max_w * max_h
from typing import MutableSequence

def partition(a: MutableSequence, left: int, right: int) -> None:
    """배열을 나누어 출력"""
    n = len(a)
    pl = left 
    pr = right 
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        print(a)
        print("x: ", x)

    if left < pr: partition(a, left, pr)
    print(a)
    if pl < right: partition(a, pl, right)
    print(a)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    partition(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x, 0, len(x)-1) # 배열 x를 나누어서 출력

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

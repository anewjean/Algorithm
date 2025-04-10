import sys

def binary_search(val):
    start = 0
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == val:
            return 1
        if arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(binary_search(num))
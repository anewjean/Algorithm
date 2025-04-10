import sys

def find_max_area(n: int, arr: list) -> int:
    stack = []
    max_area = 0
    arr.append(0) # TODO: 왜?

    for i in range(n+1):
        while stack and arr[stack[-1]] > arr[i]:
            h = arr[stack.pop()]
            w = i if not stack else i - stack[-1] -1
            max_area = max(max_area, w * h)
        stack.append(i)
    return max_area

while True:
    line = input()
    if line == '0':
        break
    N, *heights = map(int, line.split())
    print(find_max_area(N, heights))

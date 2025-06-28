def next_permutation(arr):
    i = len(arr) - 1
    # Step 1: 피크 지점 찾기
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i == 0:
        return False  # 이미 마지막 순열

    # Step 2: arr[i-1]보다 큰 값 중 가장 작은 것 찾기
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1

    # Step 3: swap
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Step 4: 뒤쪽 오름차순 정렬
    arr[i:] = reversed(arr[i:])
    return True

num = list(input().strip())
if next_permutation(num):
    print("".join(num))
else:
    print(0)
def binary_search(arr: list, val: int) -> bool:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return True
        if arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
    return False

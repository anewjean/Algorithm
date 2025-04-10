N = int(input())
solutions = sorted(list(map(int, input().split())))

left = 0
right = N - 1
best_sum = int(1e9) # 충분히 큰 수
best_pair = (0, 0)

while left < right:
    current_sum = solutions[left] + solutions[right]
    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        best_pair = (solutions[left], solutions[right]) 

    if current_sum < 0:
        left += 1
    else:
        right -= 1

print(best_pair[0], best_pair[1])


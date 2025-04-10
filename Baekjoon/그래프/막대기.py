N = int(input())
poles = [int(input()) for _ in range(N)]
stack = []

for i in range(N):
    while stack and poles[i] >= poles[stack[-1]]:
        stack.pop()

    stack.append(i)

print(len(stack))
n = int(input())

def fib(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]

memo = [-1] * (n + 1)
print(fib(n, memo))
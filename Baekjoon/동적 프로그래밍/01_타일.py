import sys
sys.setrecursionlimit(1000000)

N = int(input())

memo = [False] * (N + 1)

def fib(n, memo):
    if n in (1, 2):
        return n
    else:
        if memo[n]:
            return memo[n]
        memo[n] = (fib(n-1, memo) + fib(n-2, memo)) % 15746

        return memo[n]

print(fib(N, memo))
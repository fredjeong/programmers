import sys

input = sys.stdin.readline

N = int(input())

dp = [i for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i):
        if j**2 > i:
            break
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
print(dp[N])
def solution(n):
    dp = [0 for i in range(n+1)]
    
    if n >= 2:
        dp[2] = 3
        dp[4] = 11
        for i in range(6, n+1, 2):
            dp[i] = dp[i-2] * 3 + 2
            for j in range(i-4, -1, -2):
                dp[i] += dp[j] * 2
            dp[i] = dp[i] % 1000000007
    
    return dp[n]
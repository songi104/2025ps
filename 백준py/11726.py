n = int(input())
dp = [1]*(n+1)
for i in range(2, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2]) %10007

print(dp[n])


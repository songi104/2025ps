"""
2차원 배열 N+1 * 10을 만든다
dp[0] = 0
dp[1] = [0,1,1,1,1,1,1,1,...]
마지막 자리가 0이면 다음은 1이 되고
2면 1또는3이되고..
이걸 이용해서 빡구현
"""

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0] + [1]*9

for i in range(2, len(dp)):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if j + 1 <= 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= 1000000000


print(sum(dp[N]) % 1000000000)

# for i in range(N+1):
#     print(f"{i}: {dp[i]}")
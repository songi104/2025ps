"""
2156. 포도주 시식
lst에는 포도주를 저장한다. lst = [0] +...
dp[i]는 i번째 포도주까지 탐색했을 때 최댓값을 저장한거다.

i번째 포도주를 마시거나, 마시지 않을 수 있다.

1. i번째 포도주를 마신다
이제 i-1이 중요해진다.
i-1을 마실거라면 i-2는 마실 수 없으므로
dp[i-3] + lst[i-1] + lst[i]

i-1을 마시지 않을거라면 i-2부터는 상관없으니
dp[i-2] + lst[i]

2. i번째 포도주를 마시지않는다
그러면 그냥 dp[i-1]을 쓰면 된다

?? 궁금한점
이게 모든 케이스를 다 다룰 수 있는지
??

중요한 점은
dp[i]가 i번째 잔까지 "탐색"했을 때의 최댓값이라는것
"""

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
dp = [0]*(N+1)
for i in range(1, len(lst)):
    # i, i-1 마시는 경우
    a = lst[i-1] + lst[i]
    if i-3 >= 0:
        a += dp[i-3]


    # i 마시고 i-1 안 마심
    b =  lst[i]
    if i-2 >= 0:
        b += dp[i-2]

    # i 안 마심
    c = dp[i-1]

    dp[i] = max(a,b,c)
print(dp[N])
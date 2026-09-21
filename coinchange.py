V, N = map(int, input().split())
coins = list(map(int, input().split()))
INF = V + 1
dp = [INF] * (V + 1)
parent = [-1] * (V + 1)
dp[0] = 0
for i in range(1, V + 1):
    for coin in coins:
        if coin <= i and dp[i - coin] != INF:
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
if dp[V] == INF:
    print(-1)
else:
    ans = []
    x = V
    while x > 0:
        coin = parent[x]
        ans.append(coin)
        x -= coin
    print(dp[V])

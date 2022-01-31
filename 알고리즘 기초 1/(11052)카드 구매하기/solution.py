num = int(input())

cost = [0] + list(map(int, input().split()))
dp = [0] * (num + 1)

dp[1] = cost[1]
dp[2] = max(cost[1]*2, cost[2])

for i in range(3, num+1):
    dp[i] = cost[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])

print(dp[num])

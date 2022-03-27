num = int(input())
dp = [[0] * 10 for i in range(num+1)]
dp[1] = [1] * 10
for i in range(2, num+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
        dp[i][j] %= 10007
res = sum(dp[num])
res %= 10007
print(res)

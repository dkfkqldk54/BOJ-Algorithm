num = int(input())
dp = [[0] * 3 for i in range(num+1)]
for i in range(3):
    dp[1][i] = 1
for i in range(2, num+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
res = sum(dp[num])
res %= 9901
print(res)

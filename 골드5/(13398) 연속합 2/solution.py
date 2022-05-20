n = int(input())
arr = list(map(int, input().split()))
dp = [[0]*n for i in range(2)]
for i in range(2):
  dp[i][0] = arr[0]
for i in range(1, n):
  dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
  dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
res = max(max(dp[0]), max(dp[1]))
print(res)

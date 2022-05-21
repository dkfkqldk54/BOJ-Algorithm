n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

inf = 10**10
res = 10**10

for i in range(3):
  dp = [[inf, inf, inf] for i in range(n)]
  dp[0][i] = arr[0][i]
  for j in range(1, n):
    dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
    dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
    dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + arr[j][2]
  
  for j in range(3):
    if i != j:
      res = min(res, dp[n-1][j])

print(res)

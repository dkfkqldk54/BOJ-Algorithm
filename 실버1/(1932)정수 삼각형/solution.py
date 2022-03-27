turn = int(input())
dp = []
for i in range(turn):
  tri_line = list(map(int, input().split()))
  dp.append(tri_line)
if turn == 1:
  print(dp[turn-1][0])
else:
  for i in range(1, turn):
    for j in range(i+1):
      if j == 0:
        dp[i][j] = dp[i-1][0] + dp[i][j]
      elif j == i:
        dp[i][j] = dp[i-1][j-1] + dp[i][j]
      else:
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
  print(max(dp[turn-1]))

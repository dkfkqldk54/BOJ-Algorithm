turn = int(input())

dp = []
dp.append([0, 0, 0, 0])
dp.append([3, 0, 0, 0])
dp.append([5, 2, 0, 0])
dp.append([7, 8, 2, 0])
dp.append([9, 18, 12, 2])

if turn >= 5:
  for i in range(turn-4):
    dp.append([0, 0, 0, 0])
  for i in range(5, turn+1):
    dp[i][0] = 2 * i + 1
    dp[i][0] %= 9901
    dp[i][1] = 4 * i - 6 + dp[i-1][1]
    dp[i][1] %= 9901
    dp[i][2] = 2 * dp[i-1][1] - 4 * i + 10 + dp[i-1][2]
    dp[i][2] %= 9901
    dp[i][3] = dp[i-1][2] + dp[i-1][3]
    dp[i][3] %= 9901

res = sum(dp[turn])
res %= 9901
print(res)

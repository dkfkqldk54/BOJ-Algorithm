turn = int(input())

if turn < 3:
  res = 0
  for i in range(turn):
    num = int(input())
    res += num
  print(res)
else:
  dp = [0 for i in range(6)]
  a = int(input())
  b = int(input())
  c = int(input())
  dp[0] = a + c
  dp[1] = b + c
  dp[2] = c
  dp[3] = a
  dp[4] = b
  dp[5] = a + b
  cal = [0 for i in range(6)]
  for i in range(turn-3):
    num = int(input())
    cal[0] = max(dp[4], dp[5]) + num
    cal[1] = max(dp[0], dp[2]) + num
    cal[2] = dp[3] + num
    cal[3] = max(dp[4], dp[5])
    cal[4] = max(dp[0], dp[2])
    cal[5] = dp[1]
    for j in range(6):
      dp[j] = cal[j]
  res = max(dp)
  print(res)

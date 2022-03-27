turn = int(input())

dp = [ [0] * 4 for i in range(100001)]

dp[1] = [0, 1, 0 ,0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

quo = 1000000009

for i in range(4, 100001):
    dp[i][1] = dp[i-1][2] + dp[i-1][3]
    dp[i][1] %= quo
    dp[i][2] = dp[i-2][1] + dp[i-2][3]
    dp[i][2] %= quo
    dp[i][3] = dp[i-3][1] + dp[i-3][2]
    dp[i][3] %= quo

for _ in range(turn):
    num = int(input())
    res = dp[num][1] + dp[num][2] + dp[num][3]
    res %= quo
    print(res)

turn = int(input())

def sticker(num):
    num_list = []
    for i in range(2):
        num_list.append(list(map(int, input().split())))
    dp = [[0] * num for i in range(3)]
    for i in range(2):
        dp[i][0] = num_list[i][0]
    for i in range(1, num):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + num_list[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + num_list[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])
    res = max(dp[0][num-1], dp[1][num-1])
    return res

for i in range(turn):
    n = int(input())
    print(sticker(n))

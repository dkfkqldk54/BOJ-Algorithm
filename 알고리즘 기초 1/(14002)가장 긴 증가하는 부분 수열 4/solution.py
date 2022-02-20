turn = int(input())
num_list = list(map(int, input().split()))
dp = [1]*turn

for i in range(turn):
    for j in range(i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
max_num = max(dp)
print(max_num)

order = max_num
res = []

for i in range(turn-1, -1, -1):
    if dp[i] == order:
        res.append(num_list[i])
        order -= 1
res.reverse()

for i in res:
    print(i, end=' ')

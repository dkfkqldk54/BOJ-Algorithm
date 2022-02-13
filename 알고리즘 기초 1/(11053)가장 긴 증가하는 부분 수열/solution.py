turn = int(input())
num_list = list(map(int, input().split()))
dp = [1] * turn

for i in range(turn):
    for j in range(i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

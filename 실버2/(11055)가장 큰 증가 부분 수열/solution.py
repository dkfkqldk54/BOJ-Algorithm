turn = int(input())
num_list = list(map(int, input().split()))
dp = [i for i in num_list]

for i in range(1, turn):
  for j in range(i):
    if num_list[i] > num_list[j]:
      dp[i] = max(dp[i], dp[j]+num_list[i])

print(max(dp))

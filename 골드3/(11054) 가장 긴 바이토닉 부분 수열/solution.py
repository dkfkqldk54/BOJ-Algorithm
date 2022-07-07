n = int(input())
num_list = list(map(int, input().split()))
up_dp = [1] * n

for i in range(n):
  for j in range(i):
    if num_list[i] > num_list[j]:
      up_dp[i] = max(up_dp[i], up_dp[j] + 1)

num_list.reverse()
down_dp = [1] * n

for i in range(n):
  for j in range(i):
    if num_list[i] > num_list[j]:
      down_dp[i] = max(down_dp[i], down_dp[j] + 1)

down_dp.reverse()

res = [0] * n

for i in range(n):
  res[i] = up_dp[i] + down_dp[i]

print(max(res) - 1)

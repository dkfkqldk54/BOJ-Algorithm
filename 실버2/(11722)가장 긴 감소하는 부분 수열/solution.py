turn = int(input())
num_list = list(map(int, input().split()))
rev_list = []
for i in range(turn):
  rev_list.append(num_list.pop(-1))
dp = [1 for i in range(turn)]

for i in range(1, turn):
  for j in range(i):
    if rev_list[i] > rev_list[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

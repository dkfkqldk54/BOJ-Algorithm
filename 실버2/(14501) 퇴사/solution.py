n = int(input())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

for i in range(n):
  if arr[i][0] + i > n:
    arr[i][1] = 0

for i in range(n):
  before_max = 0
  for j in range(i):
    if arr[j][0] <= min(i-j, 5):
      before_max = max(before_max, arr[j][1])
  arr[i][1] += before_max

res = 0
for i in range(n):
  res = max(res, arr[i][1])
print(res)

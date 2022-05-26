height, width = map(int, input().split())
map = [list(map(int, input().split())) for i in range(height)]
res = 0

#길쭉이
for i in range(height):
  for j in range(width-3):
    sum = map[i][j] + map[i][j+1] + map[i][j+2] + map[i][j+3]
    res = max(res, sum)

for i in range(height-3):
  for j in range(width):
    sum = map[i][j] + map[i+1][j] + map[i+2][j] + map[i+3][j]
    res = max(res, sum)

#네모
for i in range(height-1):
  for j in range(width-1):
    sum = map[i][j] + map[i+1][j] + map[i][j+1] + map[i+1][j+1]
    res = max(res, sum)

#기역
for i in range(height-2):
  for j in range(width-1):
    sum = map[i][j] + map[i+1][j] + map[i+2][j] + map[i+2][j+1]
    res = max(res, sum)

for i in range(height-2):
  for j in range(width-1):
    sum = map[i][j] + map[i][j+1] + map[i+1][j] + map[i+2][j]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i][j] + map[i+1][j] + map[i+1][j+1] + map[i+1][j+2]
    res = max(res, sum)

for i in range(height-2):
  for j in range(width-1):
    sum = map[i][j+1] + map[i+1][j+1] + map[i+2][j+1] + map[i][j]
    res = max(res, sum)

for i in range(height-2):
  for j in range(width-1):
    sum = map[i][j+1] + map[i+1][j+1] + map[i+2][j+1] + map[i+2][j]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i+1][j] + map[i+1][j+1] + map[i+1][j+2] + map[i][j+2]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j+2]
    res = max(res, sum)

#ㄴ에 혹달린 애

for i in range(height-2):
  for j in range(width-1):
    sum = map[i][j] + map[i+1][j] + map[i+1][j+1] + map[i+2][j+1]
    res = max(res, sum)

for i in range(height-2):
  for j in range(width-1):
    sum = map[i][j+1] + map[i+1][j] + map[i+1][j+1] + map[i+2][j]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i+1][j] + map[i+1][j+1] + map[i][j+1] + map[i][j+2]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i+1][j+1] + map[i+1][j+2] + map[i][j] + map[i][j+1]
    res = max(res, sum)

#ㅜ ㅓ ㅗ ㅏ

for i in range(height-1):
  for j in range(width-2):
    sum = map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j+1]
    res = max(res, sum)

for i in range(height-1):
  for j in range(width-2):
    sum = map[i+1][j] + map[i+1][j+1] + map[i+1][j+2] + map[i][j+1]
    res = max(res, sum)

for i in range(height-2):
  for j in range(width-1):
    sum = map[i+1][j] + map[i][j+1] + map[i+1][j+1] + map[i+2][j+1]
    res = max(res, sum)

for i in range(height-2):
  for j in range(width-1):
    sum = map[i+1][j+1] + map[i][j] + map[i+1][j] + map[i+2][j]
    res = max(res, sum)

print(res)

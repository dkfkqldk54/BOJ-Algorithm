n = int(input())
arr = [list(input()) for i in range(n)]
max_candle = 0

def width_max():
  global max_candle
  for i in range(n):
    stack = 0
    for j in range(n-1):
      if arr[i][j] == arr[i][j+1]:
        stack += 1
        max_candle = max(max_candle, stack)
      else:
        stack = 0

def height_max():
  global max_candle
  for i in range(n):
    stack = 0
    for j in range(n-1):
      if arr[j][i] == arr[j+1][i]:
        stack += 1
        max_candle = max(max_candle, stack)
      else:
        stack = 0

for i in range(n):
  for j in range(n-1):
    if arr[i][j] != arr[i][j+1]:
      arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
      width_max()
      height_max()
      arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

    if arr[j][i] != arr[j+1][i]:
      arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
      width_max()
      height_max()
      arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

max_candle += 1

print(max_candle)

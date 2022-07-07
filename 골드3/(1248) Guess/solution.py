n = int(input())

all_sign = list(input())
sign = [[0] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if j >= i:
      str_sign = all_sign.pop(0)
      if str_sign == '+':
        sign[i][j] = 1
      elif str_sign == '-':
        sign[i][j] = -1

def check_ack(depth):
  summation = 0
  for i in range(depth, -1, -1):
    summation += arr[i]
    if summation == 0 and sign[i][depth] != 0:
      return False
    elif summation < 0 and sign[i][depth] >= 0:
      return False
    elif summation > 0 and sign[i][depth] <= 0:
      return False
  return True

end = False

def rec(depth):
  global end
  if depth == n:
    print(' '.join(map(str, arr)))
    end = True
    return

  for i in range(0, 11):
    arr[depth] = i * sign[depth][depth]
    if check_ack(depth):
      rec(depth+1)
      if end:
        return

arr = [0] * n
rec(0)

num = int(input())

for i in range(num):
  m, n, x, y = map(int, input().split())
  maximum = m * n

  cal = x-y
  while cal <= maximum:
    if cal % n == 0:
      res = cal + y
      print(res)
      break
    cal += m
  
  if cal > maximum:
    print(-1)

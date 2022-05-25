channel = [str(i) for i in range(500001)]
target = input()
n = int(input())

if n == 0:
  if target == '100':
    print(0)
  else:
    print(len(target))

else:
  ban = list(input().split())

  if target == '100':
    print(0)
  else:
    for i in range(n):
      for j in range(500001):
        if channel[j].find(ban[i]) >= 0:
          channel[j] = 'X'

    if target in channel:
      print(len(target))

    else:
      channel[100] = '100'

      target = int(target)
      up_target = target
      down_target = target
      up = 0
      down = 0

      while up_target < 500000:
        up_target += 1
        if channel[up_target] != 'X':
          up = up_target - target
          break

      while down_target >= 0:
        down_target -= 1
        if channel[down_target] != 'X':
          down = target - down_target
          break
    
      if up == 0 and down != 0:
        res = len(channel[down_target])
        res += down
      elif down == 0 and up != 0:
        res = len(channel[up_target])
        res += up
      else:
        if up >= down:
          res = len(channel[down_target])
          res += down
        else:
          res = len(channel[up_target])
          res += up

      print(res)

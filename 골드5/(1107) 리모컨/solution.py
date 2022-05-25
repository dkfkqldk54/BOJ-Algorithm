channel = [str(i) for i in range(1000001)]
target = int(input())
target_str = str(target)
n = int(input())
diff_100 = abs(target-100)

if n == 0:
  res = min(len(target_str), diff_100)
  print(res)

else:
  ban = list(input().split())
  for i in ban:
    for j in range(1000001):
      if i in channel[j]:
        channel[j] = 'X'

  if target_str in channel:
    res = min(len(target_str), diff_100)
    print(res)
  
  else:
    up, down = 0, 0
    up_change, down_change = False, False
    while target+up < 1000000:
      up += 1
      if channel[target+up] != 'X':
        up_change = True
        break
    while target-down > 0:
      down += 1
      if channel[target-down] != 'X':
        down_change = True
        break
    
    if up_change == False and down_change == True:
      res = min(len(channel[target-down]) + down, diff_100)
      print(res)
    elif up_change == True and down_change == False:
      res = min(len(channel[target+up]) + up, diff_100)
      print(res)
    elif up_change == True and down_change == True:
      res = min(len(channel[target-down])+ down, len(channel[target+up]) + up, diff_100)
      print(res)
    else:
      print(diff_100)

def cal(scal, num):
    cnt = 0
    for i in range(scal + 1):
        cnt += i * (10 ** i - 10 **(i-1))
    cnt += (scal + 1) * (num- (10 ** scal) + 1)
    cnt = int(cnt)
    return cnt

num = int(input())

if num < 10:
  print(num)

else:
  if num == 10**8:
    scal = 8
  elif num >= 10**7:
    scal = 7
  elif num >= 10**6:
    scal = 6
  elif num >= 10**5:
    scal = 5
  elif num >= 10**4:
    scal = 4
  elif num >= 10**3:
    scal = 3
  elif num >= 10**2:
    scal = 2
  else:
    scal = 1
    
  print(cal(scal, num))

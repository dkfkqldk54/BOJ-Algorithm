channel = [str(i) for i in range(501)]
target = input()
n = int(input())
ban = list(input().split())

for i in range(n):
  for j in range(501):
    if channel[j].find(ban[i]) >= 0:
      channel[j] = '0'

if target == '100':
  print(0)
elif target in ban:
  print(len(target))
else:
  target = int(target)
  i = 0
  j = 0
  up = 999999
  down = 999999

  channel[100] = '100'
  
  while target + i < 501:
    i += 1
    if channel[target + i] != '0':
      up = i
      break

  while target - j > 0:
    j += 1
    if channel[target-j] != '0':
      down = j
      break

  res = len

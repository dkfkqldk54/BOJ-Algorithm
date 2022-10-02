from collections import deque

def process(p):
  if p == 'R':
    if reversed[0]:
      reversed[0] = False
    else:
      reversed[0] = True
  else:
    if arr:
      if reversed[0]:
        arr.pop()
      else:
        arr.popleft()
    else:
      error[0] = True

n = int(input())

for _ in range(n):
  func_arr = list(input())
  number = int(input())
  make_arr = input()[1:-1]
  if make_arr:
    make_arr = list(make_arr.split(','))
  else:
    make_arr = []
  arr = deque([i for i in make_arr])

  reversed = [False]
  error = [False]

  for p in func_arr:
    process(p)


  if error[0]:
    print('error')
  else:
    ans = ''
    if reversed[0]:
      for i in range(len(arr)-1, -1, -1):
        ans += arr[i]
        ans += ','
    else:
      for i in range(len(arr)):
        ans += arr[i]
        ans += ','
    ans = ans[:-1]
    ans = '[' + ans + ']'
    print(ans)

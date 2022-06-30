n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

res = []

def rec(depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return
  avo_dup = 0

  for i in range(n):
    if avo_dup != num_list[i]:
      res.append(num_list[i])
      avo_dup = num_list[i]
      rec(depth+1)
      res.pop()
      
rec(0)

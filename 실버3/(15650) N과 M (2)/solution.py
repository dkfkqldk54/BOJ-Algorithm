n, m = map(int, input().split())
res = []

def rec(start, depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return

  for i in range(start, n+1):
      res.append(i)
      rec(i+1, depth+1)
      res.pop()
      
rec(1, 0)

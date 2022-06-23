n, m = map(int, input().split())
res = []
visited = [False for i in range(n+1)]

def rec(depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return

  for i in range(1, n+1):
    if visited[i] == False:
      visited[i] = True
      res.append(i)
      rec(depth+1)
      visited[i] = False
      res.pop()
      
rec(0)

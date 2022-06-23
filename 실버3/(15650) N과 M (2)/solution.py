n, m = map(int, input().split())

res = []
visited = [False for _ in range(n+1)]

def rec(start, depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return

  for i in range(start, n+1):
    if visited[i] == False:
      visited[i] = True
      res.append(i)
      rec(i+1, depth+1)
      visited[i] = False
      res.pop()

rec(1, 0)

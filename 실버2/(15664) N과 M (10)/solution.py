n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

res = []
visited = [False for i in range(n)]

def rec(start, depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return
  avo_dup = 0

  for i in range(start, n):
    if visited[i] == False and avo_dup != num_list[i]:
      visited[i] = True
      res.append(num_list[i])
      avo_dup = num_list[i]
      rec(i+1, depth+1)
      visited[i] = False
      res.pop()
      
rec(0, 0)

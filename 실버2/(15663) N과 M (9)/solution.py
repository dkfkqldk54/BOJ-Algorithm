n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

res = []
visited = [False for i in range(n)]

def rec(depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return
  avo_dup = 0

  for i in range(n):
    if visited[i] == False and avo_dup != num_list[i]:
      visited[i] = True
      res.append(num_list[i])
      avo_dup = num_list[i]
      rec(depth+1)
      visited[i] = False
      res.pop()
      
rec(0)

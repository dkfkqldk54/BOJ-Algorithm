n = int(input())
arr = list(map(int, input().split()))

res = []
visited = [False for i in range(n)]

plus_list = []

def rec(depth):
  if depth == n:
    ans = 0
    for j in range(n-1):
      ans += abs(arr[res[j]] - arr[res[j+1]])
      plus_list.append(ans)
    return

  for i in range(n):
    if visited[i] == False:
      visited[i] = True
      res.append(i)
      rec(depth+1)
      visited[i] = False
      res.pop()
      
rec(0)
print(max(plus_list))

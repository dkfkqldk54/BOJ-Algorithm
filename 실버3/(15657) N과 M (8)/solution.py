n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

res = []

def rec(start, depth):
  if depth == m:
    print(' '.join(map(str, res)))
    return

  for i in range(start, n):
    res.append(num_list[i])
    rec(i, depth+1)
    res.pop()
      
rec(0, 0)

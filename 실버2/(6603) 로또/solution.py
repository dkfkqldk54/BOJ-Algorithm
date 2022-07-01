def rec(start, depth, permutation, visited, arr):
  if depth == 6:
    print(' '.join(map(str, permutation)))
    return
      
  for i in range(start, n):
    if visited[i] == False:
      visited[i] = True
      permutation.append(arr[i])
      rec(i+1, depth+1, permutation, visited, arr)
      permutation.pop()
      visited[i] = False

first_case = True

while True:
  arr = list(map(int, input().split()))
  n = arr.pop(0)
  arr.sort()

  if first_case == False and n != 0:
    print('')

  if n == 0:
    break
  else:
    rec(0, 0 , [], [False for _ in range(n)], arr)
    if first_case == True:
      first_case = False

n = int(input())
sign = list(input().split())
visited = [False for _ in range(10)]

min_num = 10 ** 10
max_num = 0

min_res = ''
max_res = ''

def back_tracking(depth, permutation, visited):
  global min_num, max_num, min_res, max_res
  if depth == n:
    char = ''
    for i in permutation:
      char += str(i)
    num = int(char)
    if num < min_num:
      min_num = num
      min_res = char
    if num > max_num:
      max_num = num
      max_res = char
    return

  for i in range(10):
    if visited[i] == False:
      if sign[depth] == '<' and permutation[depth] < i:
        visited[i] = True
        permutation.append(i)
        back_tracking(depth+1, permutation, visited)
        permutation.pop()
        visited[i] = False
      elif sign[depth] == '>' and permutation[depth] > i:
        visited[i] = True
        permutation.append(i)
        back_tracking(depth+1, permutation, visited)
        permutation.pop()
        visited[i] = False        

for i in range(10):
  visited[i] = True
  back_tracking(0, [i], visited)
  visited[i] = False

print(max_res)
print(min_res)

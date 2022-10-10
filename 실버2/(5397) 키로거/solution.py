from collections import deque

n = int(input())

for _ in range(n):

  result = []
  repository = deque([])

  record = list(input())

  for char in record:
    if char == "<":
      if result:
        repository.appendleft(result.pop())
    elif char == ">":
      if repository:
        result.append(repository.popleft())
    elif char == '-':
      if result:
        result.pop()
    else:
      result.append(char)
  result.extend(repository)
  res = ''
  for i in result:
    res += i
  print(res)

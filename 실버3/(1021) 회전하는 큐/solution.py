from collections import deque

n, m = map(int, input().split())
order = list(input().split())
for i in range(m):
  order[i] = int(order[i])
rotation = deque([])
for i in range(1, n+1):
  rotation.append(i)
cnt = 0

def is_it_right(index, size):
  if index <= size - index:
    return True
  else:
    return False

for i in range(m):
  num = order[i]
  index = rotation.index(num)
  size = len(rotation)
  if is_it_right(index, size):
    for _ in range(index):
      rotation.append(rotation.popleft())
      cnt += 1
    rotation.popleft()
  else:
    for _ in range(size - index):
      rotation.appendleft(rotation.pop())
      cnt += 1
    rotation.popleft()

print(cnt)

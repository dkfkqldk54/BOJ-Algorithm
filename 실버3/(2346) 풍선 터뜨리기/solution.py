from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))

while q:
  tmp = q.popleft()
  print(tmp[0] + 1, end = " ")
  if tmp[1] > 0 and q:
    for i in range(tmp[1]-1):
      q.append(q.popleft())
  elif tmp[1] < 0 and q:
    for i in range(-tmp[1]):
      q.appendleft(q.pop())

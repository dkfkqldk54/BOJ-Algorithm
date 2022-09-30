import sys

n = int(input())
queue = []
cnt = 0

for i in range(n):
  line = sys.stdin.readline().strip()
  if line == 'pop':
    if len(queue)-cnt == 0:
      print(-1)
    else:
      print(queue[cnt])
      cnt += 1
  elif line == 'size':
    print(len(queue)-cnt)
  elif line == 'empty':
    if len(queue)-cnt == 0:
      print(1)
    else:
      print(0)
  elif line == 'front':
    if len(queue)-cnt == 0:
      print(-1)
    else:
      print(queue[cnt])
  elif line == 'back':
    if len(queue)-cnt == 0:
      print(-1)
    else:
      print(queue[-1])
  else:
    queue.append(line[5:])  

turn = int(input())

for _ in range(turn):
  n, m = map(int, input().split())
  waiting = list(input().split())
  priority = waiting.copy()
  priority.sort()
  find = False; i = 0; count = 0;
  while not find:
    if i == n:
      i = 0
    if waiting[i] == priority[-1]:
      priority.pop()
      count += 1
      if i == m:
        print(count)
        find = True
    i += 1

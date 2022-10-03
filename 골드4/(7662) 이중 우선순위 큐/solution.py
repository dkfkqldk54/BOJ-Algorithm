import sys
from heapq import heappush, heappop

total = int(input()) #sys.stdin.readline().strip()

for _ in range(total):
  turn = int(input())

  max_heap = []
  min_heap = []
  visited = [False for _ in range(turn)]

  for i in range(turn):

    op = input()

    if op[0] == 'I':
      num = int(op[2:])
      heappush(max_heap, (-num, num, i))
      heappush(min_heap, (num, num, i))
      visited[i] = True

    else:
      if op[2] == '1':
        while max_heap and not visited[max_heap[0][2]]:
          heappop(max_heap)
        if max_heap:
          visited[max_heap[0][2]] = False          
          heappop(max_heap)
      else:
        while min_heap and not visited[min_heap[0][2]]:
          heappop(min_heap)
        if min_heap: 
          visited[min_heap[0][2]] = False  
          heappop(min_heap)
    
  while max_heap and not visited[max_heap[0][2]]:
    heappop(max_heap)
  while min_heap and not visited[min_heap[0][2]]:
    heappop(min_heap)  

  if not max_heap and not min_heap:
    print('EMPTY')
  else:
    print(heappop(max_heap)[1], end = ' ')
    print(heappop(min_heap)[1])

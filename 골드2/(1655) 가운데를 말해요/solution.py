import sys
from heapq import heappush, heappop

turn = int(input())

left_heap = []
right_heap = []

for i in range(turn):
  num = int(sys.stdin.readline().strip())

  if i % 2 == 0:
    heappush(left_heap, (-num, num))
  else:
    heappush(right_heap, (num, num))
  
  if right_heap and left_heap[0][1] > right_heap[0][1]:
    left = heappop(left_heap)[1]
    right = heappop(right_heap)[1]
    heappush(left_heap, (-right, right))
    heappush(right_heap, (left, left))
  
  print(left_heap[0][1])

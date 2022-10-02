import sys
from heapq import heappush, heappop

n = int(input())
heap = []

for i in range(n):
  num = sys.stdin.readline().strip()
  if num == '0':
    if heap:
      print(heappop(heap)[1])
    else:
      print(0)
  else:
    abs_num = abs(int(num))
    if int(num) < 0:
      abs_num -= 0.1
    heappush(heap, (abs_num, int(num)))

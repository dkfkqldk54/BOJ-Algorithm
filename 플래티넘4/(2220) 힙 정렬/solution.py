heap = []
heap.append(-1)

n = int(input())

def percolateUp(child_index, queue):
  parent_index = (child_index - 1) // 2
  if child_index > 0 and queue[child_index] > queue[parent_index]:
    queue[child_index], queue[parent_index] = queue[parent_index], queue[child_index]
    percolateUp(parent_index, queue)

for i in range(2, n+1):
  percolateUp(i-2, heap)
  heap.append(-i)
  heap[0], heap[-1] = heap[-1], heap[0]

for i in heap:
  print(-i, end = ' ')

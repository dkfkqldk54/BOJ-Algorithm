import sys

n, m, r = map(int, sys.stdin.readline().rstrip().split())

nodes = [[] for i in range(n+1)]
nodes_order = [0 for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
  start, end = map(int, sys.stdin.readline().rstrip().split())
  nodes[start].append(end)
  nodes[end].append(start)
#nodes = [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]

for i in range(n+1):
  nodes[i].sort(reverse=True)
#nodes = [[], [4, 2], [4, 3, 1], [4, 2], [3, 2, 1], []]


order = 1
stack = []
stack.append(r)

while stack:
  next = stack.pop()
  visited[next] = True

  if nodes_order[next] == 0:
    nodes_order[next] = order
    order += 1

  for next_move in nodes[next]:
    if visited[next_move] == False:
      stack.append(next_move)

for i in nodes_order[1:]:
  print(i)

n = int(input())
travel_cost = [list(map(int, input().split())) for _ in range(n)]
min_cost = 10 ** 10

def backtracking(start, next, cost, visited):
  global min_cost
  
  if len(visited) == n:
    if travel_cost[next][start] != 0:
      min_cost = min(min_cost, cost + travel_cost[next][start])
    return

  for i in range(n):
    if travel_cost[next][i] != 0 and cost < min_cost and i not in visited:
      visited.append(i)
      backtracking(start, i, cost + travel_cost[next][i], visited)
      visited.pop()

for i in range(n):
  backtracking(i, i, 0, [i])

print(min_cost)

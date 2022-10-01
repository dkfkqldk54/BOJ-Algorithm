from collections import deque

n, k = map(int, input().split())
table = deque([])
ans = []
for i in range(1, n+1):
  table.append(i)

while table:
  for _ in range(k-1):
    table.append(table.popleft())
  ans.append(table.popleft())

ans_str = '<'
for i in range(len(ans)):
  ans_str += str(ans[i])
  ans_str += ', '
ans_str = ans_str[:-2]
ans_str += '>'
print(ans_str)

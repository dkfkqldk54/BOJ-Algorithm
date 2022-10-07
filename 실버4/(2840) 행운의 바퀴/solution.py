from collections import deque

n, k = map(int, input().split())

q = deque(['?' for _ in range(n)])

possible = True

for _ in range(k):
  rotation, char = input().split()
  for i in range(int(rotation)-1):
    q.appendleft(q.pop())
  poly = q.pop()
  if poly != '?' and poly != char:
    possible = False
  q.appendleft(char)

check_redundancy = [0 for _ in range(26)]
for char in q:
  if char != '?':
    check_redundancy[ord(char)-65] += 1

for i in check_redundancy:
  if i > 1:
    possible = False

if possible:
  for char in q:
    print(char, end='')
else:
  print('!')

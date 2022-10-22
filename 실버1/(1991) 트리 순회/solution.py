n = int(input())
nodes = []
for _ in range(n):
  nodes.append(input())
nodes = sorted(nodes)

def preOrder(char):
  global res
  if char != '.':
    index = ord(char) - 65
    if visited[index] == False:
      res += char
      visited[index] = True
    preOrder(nodes[index][2])
    preOrder(nodes[index][4])

def inOrder(char):
  global res
  if char != '.':
    index = ord(char) - 65
    inOrder(nodes[index][2])
    if visited[index] == False:
      res += char
      visited[index] = True
    inOrder(nodes[index][4])

def postOrder(char):
  global res
  if char != '.':
    index = ord(char) - 65
    postOrder(nodes[index][2])
    postOrder(nodes[index][4])
    if visited[index] == False:
      res += char
      visited[index] = True

visited = [False for _ in range(26)]
res = ''
preOrder('A')
print(res)

visited = [False for _ in range(26)]
res = ''
inOrder('A')
print(res)

visited = [False for _ in range(26)]
res = ''
postOrder('A')
print(res)

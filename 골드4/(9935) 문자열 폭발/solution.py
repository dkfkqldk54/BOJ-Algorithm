string = input()
explosion = list(input())
stack = []

for char in string:
  stack.append(char)
  if char == explosion[-1] and len(stack) >= len(explosion):

    if stack[-len(explosion):] == explosion:
      for _ in range(len(explosion)):
        stack.pop() 

ans = ''
for char in stack:
  ans += char

if ans == '':
  print('FRULA')
else:
  print(ans)

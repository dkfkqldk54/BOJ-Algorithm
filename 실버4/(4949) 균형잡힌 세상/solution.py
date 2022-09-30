def is_it_yes(line):
  for char in line:
    if char == '(' or char == '[':
      stack.append(char)
    elif char == ')':
      if len(stack) == 0:
        return False
      elif stack[-1] == '(':
        stack.pop()
      else:
        return False
    elif char == ']':
      if len(stack) == 0:
        return False
      elif stack[-1] == '[':
        stack.pop()
      else:
        return False
  if len(stack) == 0:
    return True

end = False
while not end:
  
  line = input()

  if line == '.':
    end = True
    break

  stack = []
  if is_it_yes(line):
    print('yes')
  else:
    print('no')
